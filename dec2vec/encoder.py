"""Dec2VecEncoder: embed log lines using trained dec2vec weights.

This is the bridge from word embeddings (SGNS) to log-line embeddings.

Default strategy:
- tokenize a log line
- map tokens -> internal ids via global_vocab + internal_vocab
- mean-pool the corresponding word vectors

This gives a fixed-size vector per log line.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence

import numpy as np

from dec2vec.data import remove_timestamp, tokenize
from dec2vec.io import load_checkpoint
from dec2vec.vocab import InternalVocab, load_internal_vocab


def _l2_normalize_rows(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    norms = np.maximum(norms, eps)
    return x / norms


def _l2_normalize_vec(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    n = float(np.linalg.norm(x))
    if n <= eps:
        return x
    return x / n


@dataclass(frozen=True)
class Dec2VecEncoderConfig:
    use_out: bool = False
    pooling: str = "mean"  # mean only (for now)
    normalize: bool = True


class Dec2VecEncoder:
    def __init__(
        self,
        *,
        checkpoint_path: str,
        global_vocab_path: str = "dataset/global_vocab_index.json",
        internal_vocab_path: str = "dataset/internal_central_vocab.json",
        config: Optional[Dec2VecEncoderConfig] = None,
    ) -> None:
        self.config = config or Dec2VecEncoderConfig()

        self.weights = load_checkpoint(checkpoint_path)
        self.internal_vocab: InternalVocab = load_internal_vocab(internal_vocab_path)
        self.global_vocab: Dict[str, int] = self._load_global_vocab(global_vocab_path)

        self.embedding_matrix = self.weights.w_out if self.config.use_out else self.weights.w_in

        # Optional: pre-normalize word vectors for cosine-friendly means
        self._word_vecs = self.embedding_matrix.astype(np.float32, copy=False)

    @staticmethod
    def _load_global_vocab(path: str) -> Dict[str, int]:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {str(k): int(v) for k, v in data.items()}

    @property
    def dim(self) -> int:
        return int(self._word_vecs.shape[1])

    def tokens_to_internal_ids(self, tokens: Sequence[str]) -> List[int]:
        ids: List[int] = []
        g2i = self.internal_vocab.global_to_internal
        for t in tokens:
            gid = self.global_vocab.get(t)
            if gid is None:
                continue
            iid = g2i.get(int(gid))
            if iid is None:
                continue
            ids.append(int(iid))
        return ids

    def embed_token_ids(self, token_ids: Sequence[int]) -> np.ndarray:
        if not token_ids:
            return np.zeros((self.dim,), dtype=np.float32)

        vecs = self._word_vecs[np.asarray(token_ids, dtype=np.int64)]

        if self.config.pooling != "mean":
            raise ValueError(f"Unsupported pooling: {self.config.pooling}")

        pooled = vecs.mean(axis=0)
        if self.config.normalize:
            pooled = _l2_normalize_vec(pooled)
        return pooled.astype(np.float32, copy=False)

    def embed_log_line(self, line: str, *, strip_timestamp: bool = True) -> np.ndarray:
        s = str(line).strip()
        if strip_timestamp:
            s = remove_timestamp(s)
        toks = tokenize(s)
        ids = self.tokens_to_internal_ids(toks)
        return self.embed_token_ids(ids)

    def embed_log_lines(self, lines: Sequence[str], *, strip_timestamp: bool = True) -> np.ndarray:
        out = np.zeros((len(lines), self.dim), dtype=np.float32)
        for i, line in enumerate(lines):
            out[i] = self.embed_log_line(line, strip_timestamp=strip_timestamp)
        return out
