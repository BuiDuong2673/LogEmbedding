"""Generic dec2vec cosine retrieval over arbitrary texts.

This is used by scripts that want retrieval without Drain templateization,
for example indexing raw cluster examples as the knowledge base.

Design:
- embed each text via Dec2VecEncoder (mean pooled word vectors)
- pre-normalize matrix rows for fast cosine similarity
- retrieve top-k with partial argpartition
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional, Sequence, Tuple

import numpy as np

from dec2vec.encoder import Dec2VecEncoder


@dataclass(frozen=True)
class RetrievedText:
    text: str
    score: float
    tag: str


def _l2_normalize_rows(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    norms = np.maximum(norms, eps)
    return x / norms


class Dec2VecTextRetriever:
    def __init__(self, *, encoder: Dec2VecEncoder) -> None:
        self.encoder = encoder
        self._items: List[Tuple[str, str]] = []  # (tag, text)
        self._matrix: Optional[np.ndarray] = None

    @property
    def dim(self) -> int:
        return self.encoder.dim

    def set_items(self, items: Iterable[Tuple[str, str]]) -> int:
        self._items = [(str(tag), str(text)) for tag, text in items if str(text).strip()]
        self._matrix = None
        return len(self._items)

    def build_index(self, *, strip_timestamp: bool = True) -> None:
        if not self._items:
            self._matrix = np.zeros((0, self.dim), dtype=np.float32)
            return

        mat = np.zeros((len(self._items), self.dim), dtype=np.float32)
        for i, (_, text) in enumerate(self._items):
            mat[i] = self.encoder.embed_log_line(text, strip_timestamp=strip_timestamp)
        self._matrix = _l2_normalize_rows(mat)

    def retrieve(self, query: str, *, top_k: int = 5, strip_timestamp: bool = True) -> List[RetrievedText]:
        if self._matrix is None:
            self.build_index(strip_timestamp=strip_timestamp)

        assert self._matrix is not None
        if self._matrix.shape[0] == 0:
            return []

        q = self.encoder.embed_log_line(str(query), strip_timestamp=strip_timestamp).astype(np.float32, copy=False)
        qn = float(np.linalg.norm(q))
        if qn <= 1e-12:
            return []
        q = q / qn

        sims = self._matrix @ q

        top_k = max(1, int(top_k))
        top_k = min(top_k, sims.shape[0])

        idx = np.argpartition(-sims, kth=top_k - 1)[:top_k]
        idx = idx[np.argsort(-sims[idx])]

        out: List[RetrievedText] = []
        for j in idx:
            tag, text = self._items[int(j)]
            out.append(RetrievedText(text=text, score=float(sims[int(j)]), tag=tag))
        return out
