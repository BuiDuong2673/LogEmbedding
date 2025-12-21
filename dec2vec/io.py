"""I/O helpers for dec2vec checkpoints."""

from __future__ import annotations

import json
import os
from dataclasses import asdict
from typing import Any, Dict, Optional

import numpy as np

from dec2vec.model import Dec2VecWeights


def save_checkpoint(
    *,
    output_dir: str,
    weights: Dec2VecWeights,
    meta: Dict[str, Any],
    name: str,
) -> str:
    os.makedirs(output_dir, exist_ok=True)

    npz_path = os.path.join(output_dir, f"{name}.npz")
    np.savez_compressed(npz_path, w_in=weights.w_in, w_out=weights.w_out)

    meta_path = os.path.join(output_dir, f"{name}.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    return npz_path


def load_checkpoint(npz_path: str) -> Dec2VecWeights:
    data = np.load(npz_path)
    return Dec2VecWeights(w_in=data["w_in"], w_out=data["w_out"])
