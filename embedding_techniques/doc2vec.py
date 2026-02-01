"""Document-level embedding (Doc2Vec) for log lines.

This repo's existing Word2Vec is word->context-word within a line.
For Doc2Vec, we want sentence/log-line vectors that capture surrounding lines.

We implement a minimal PV-DBOW style model:
- Document vector D[d] predicts words in its (sentence-window) context.
- Negative sampling for efficiency.

Numpy-only to keep dependencies minimal.
"""

from __future__ import annotations

import numpy as np


class Doc2VecDBOW:
    """PV-DBOW Doc2Vec with negative sampling."""

    def __init__(self, D: np.ndarray, W: np.ndarray):
        """Initialize.

        Args:
            D: document embedding matrix (num_docs × dim)
            W: output word matrix (dim × vocab_size)
        """

        self.D = D
        self.W = W

    @staticmethod
    def sigmoid(x: float | np.ndarray):
        x = np.clip(x, -500, 500)
        return 1.0 / (1.0 + np.exp(-x))

    def train_with_negative_sampling(
        self,
        doc_id: int,
        word_idx: int,
        negative_samples: np.ndarray,
        learning_rate: float = 0.01,
    ):
        """Train a single (doc, word) with negative sampling."""

        doc_vec = self.D[doc_id, :]
        grad_doc = np.zeros_like(doc_vec)
        total_loss = 0.0

        # Positive sample
        pos_vec = self.W[:, word_idx]
        score = float(np.dot(doc_vec, pos_vec))
        score = float(np.clip(score, -10, 10))
        sig = float(self.sigmoid(score))
        loss = -np.log(sig + 1e-10)
        grad = sig - 1.0
        grad_doc += grad * pos_vec
        self.W[:, word_idx] -= learning_rate * grad * doc_vec
        total_loss += float(loss)

        # Negative samples
        for neg_idx in negative_samples:
            neg_idx_int = int(neg_idx)
            if neg_idx_int == word_idx:
                continue
            neg_vec = self.W[:, neg_idx_int]
            score = float(np.dot(doc_vec, neg_vec))
            score = float(np.clip(score, -10, 10))
            sig = float(self.sigmoid(score))
            loss = -np.log(1.0 - sig + 1e-10)
            grad = sig
            grad_doc += grad * neg_vec
            self.W[:, neg_idx_int] -= learning_rate * grad * doc_vec
            total_loss += float(loss)

        grad_doc = np.clip(grad_doc, -1, 1)
        self.D[doc_id, :] -= learning_rate * grad_doc

        return total_loss, self.D, self.W
