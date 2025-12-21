"""dec2vec model: Skip-gram with Negative Sampling (SGNS) in numpy."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np


def _sigmoid(x: float) -> float:
    # numerically stable-ish for typical dot ranges
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)


@dataclass
class Dec2VecWeights:
    w_in: np.ndarray  # [V, D]
    w_out: np.ndarray  # [V, D]


def init_weights(vocab_size: int, dim: int, seed: int = 0) -> Dec2VecWeights:
    rng = np.random.default_rng(seed)
    # Small random init
    w_in = (rng.random((vocab_size, dim), dtype=np.float32) - 0.5) / dim
    w_out = np.zeros((vocab_size, dim), dtype=np.float32)
    return Dec2VecWeights(w_in=w_in, w_out=w_out)


def sgns_step(
    weights: Dec2VecWeights,
    *,
    center: int,
    context: int,
    negatives: List[int],
    lr: float,
) -> None:
    """One SGNS update for (center, context) with K negatives."""
    w_in = weights.w_in
    w_out = weights.w_out

    v = w_in[center]

    # Positive
    u_pos = w_out[context]
    dot_pos = float(np.dot(u_pos, v))
    p_pos = _sigmoid(dot_pos)
    g_pos = (1.0 - p_pos) * lr

    # Save old vectors needed for v update
    u_pos_old = u_pos.copy()

    w_out[context] = u_pos + g_pos * v
    v_update = g_pos * u_pos_old

    # Negatives
    for neg in negatives:
        u_neg = w_out[neg]
        dot_neg = float(np.dot(u_neg, v))
        p_neg = _sigmoid(dot_neg)
        g_neg = (0.0 - p_neg) * lr  # negative label is 0

        u_neg_old = u_neg.copy()
        w_out[neg] = u_neg + g_neg * v
        v_update += g_neg * u_neg_old

    w_in[center] = v + v_update


def get_word_embedding(weights: Dec2VecWeights, wid: int, use_out: bool = False) -> np.ndarray:
    if use_out:
        return weights.w_out[wid]
    return weights.w_in[wid]
