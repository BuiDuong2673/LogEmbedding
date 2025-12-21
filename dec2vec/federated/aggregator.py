"""Federated aggregation for dec2vec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

import numpy as np

from dec2vec.model import Dec2VecWeights


@dataclass
class ClientUpdate:
    weights: Dec2VecWeights
    num_examples: int


def fedavg(updates: List[ClientUpdate]) -> Dec2VecWeights:
    if not updates:
        raise ValueError("No client updates")

    total = sum(max(0, u.num_examples) for u in updates)
    if total <= 0:
        # fallback to simple average
        total = len(updates)
        weights = [1.0 / total] * len(updates)
    else:
        weights = [u.num_examples / total for u in updates]

    w_in = np.zeros_like(updates[0].weights.w_in)
    w_out = np.zeros_like(updates[0].weights.w_out)

    for u, alpha in zip(updates, weights):
        w_in += alpha * u.weights.w_in
        w_out += alpha * u.weights.w_out

    return Dec2VecWeights(w_in=w_in, w_out=w_out)
