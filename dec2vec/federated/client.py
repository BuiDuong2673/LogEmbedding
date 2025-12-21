"""Federated client training loop for dec2vec."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

import numpy as np

from dec2vec.data import ClientCorpus, iter_skipgram_pairs
from dec2vec.model import Dec2VecWeights, sgns_step


@dataclass
class ClientTrainConfig:
    window: int = 2
    negative_k: int = 5
    lr: float = 0.025
    local_epochs: int = 1
    max_pairs: int | None = None
    seed: int = 0


class NegativeSampler:
    """Unigram^0.75 negative sampler from a client's word frequency."""

    def __init__(self, freq: Dict[int, int], vocab_size: int, seed: int = 0):
        self.vocab_size = vocab_size
        self.rng = random.Random(seed)

        # Build distribution array over all vocab ids; unseen words get tiny mass.
        probs = np.full((vocab_size,), 1e-12, dtype=np.float64)
        for wid, c in freq.items():
            if 0 <= wid < vocab_size:
                probs[wid] = float(c) ** 0.75
        probs /= probs.sum()

        self.probs = probs

    def sample(self, k: int, avoid: int | None = None) -> List[int]:
        out: List[int] = []
        # numpy choice is faster but keep deps minimal; we already use numpy.
        while len(out) < k:
            wid = int(np.random.choice(self.vocab_size, p=self.probs))
            if avoid is not None and wid == avoid:
                continue
            out.append(wid)
        return out


def local_train(
    *,
    weights: Dec2VecWeights,
    corpus: ClientCorpus,
    config: ClientTrainConfig,
) -> tuple[Dec2VecWeights, int]:
    """Train on a client's corpus and return updated weights + number of pairs."""
    vocab_size = weights.w_in.shape[0]
    sampler = NegativeSampler(corpus.freq, vocab_size=vocab_size, seed=config.seed)

    pairs = list(iter_skipgram_pairs(corpus.token_ids, window=config.window))

    # Optionally cap to speed up
    if config.max_pairs is not None and len(pairs) > config.max_pairs:
        rnd = random.Random(config.seed)
        pairs = rnd.sample(pairs, k=config.max_pairs)

    num_pairs = len(pairs)

    for epoch in range(max(1, config.local_epochs)):
        rnd = random.Random(config.seed + epoch)
        rnd.shuffle(pairs)

        for center, context in pairs:
            negs = sampler.sample(config.negative_k, avoid=context)
            sgns_step(weights, center=center, context=context, negatives=negs, lr=config.lr)

    return weights, num_pairs
