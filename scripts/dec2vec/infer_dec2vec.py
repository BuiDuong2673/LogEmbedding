"""Infer / inspect a dec2vec checkpoint.

Moved under scripts/dec2vec/ to keep repo root tidy.

Example:
  python scripts/dec2vec/infer_dec2vec.py \
    --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
    --word error --topk 20
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Dict, List, Tuple

import numpy as np

# Ensure repo root is importable when running from scripts/
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from dec2vec.io import load_checkpoint
from dec2vec.vocab import load_internal_vocab


def _l2_normalize(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    n = float(np.linalg.norm(x))
    if n <= eps:
        return x
    return x / n


def load_global_vocab(path: str = "dataset/global_vocab_index.json") -> Dict[str, int]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {str(k): int(v) for k, v in data.items()}


def build_internal_id_to_word(
    *,
    global_vocab: Dict[str, int],
    global_to_internal: Dict[int, int],
) -> Dict[int, str]:
    global_to_word: Dict[int, str] = {}
    for w, gid in global_vocab.items():
        if gid not in global_to_word:
            global_to_word[gid] = w

    internal_to_word: Dict[int, str] = {}
    for gid, iid in global_to_internal.items():
        w = global_to_word.get(int(gid))
        if w is not None:
            internal_to_word[int(iid)] = w

    return internal_to_word


def nearest_neighbors(
    *,
    matrix: np.ndarray,
    query_id: int,
    topk: int,
) -> List[Tuple[int, float]]:
    q = _l2_normalize(matrix[query_id].astype(np.float32, copy=False))
    m = matrix.astype(np.float32, copy=False)

    norms = np.linalg.norm(m, axis=1, keepdims=True)
    norms = np.maximum(norms, 1e-12)
    m_norm = m / norms

    sims = m_norm @ q
    sims[query_id] = -np.inf

    if topk <= 0:
        topk = 10
    topk = min(topk, sims.shape[0] - 1)

    idx = np.argpartition(-sims, kth=topk)[:topk]
    idx = idx[np.argsort(-sims[idx])]
    return [(int(i), float(sims[i])) for i in idx]


def main() -> int:
    ap = argparse.ArgumentParser(description="Infer nearest neighbors from a dec2vec checkpoint")
    ap.add_argument("--checkpoint", required=True, help="Path to .npz checkpoint")
    ap.add_argument("--word", required=True, help="Query word (must exist in internal vocab)")
    ap.add_argument("--topk", type=int, default=20)
    ap.add_argument("--use-out", action="store_true", help="Use output embeddings instead of input")

    ap.add_argument("--global-vocab", default="dataset/global_vocab_index.json")
    ap.add_argument("--internal-vocab", default="dataset/internal_central_vocab.json")

    args = ap.parse_args()

    if not os.path.exists(args.checkpoint):
        raise FileNotFoundError(args.checkpoint)

    weights = load_checkpoint(args.checkpoint)
    internal_vocab = load_internal_vocab(args.internal_vocab)
    global_vocab = load_global_vocab(args.global_vocab)

    internal_to_word = build_internal_id_to_word(
        global_vocab=global_vocab,
        global_to_internal=internal_vocab.global_to_internal,
    )

    gid = global_vocab.get(args.word)
    if gid is None:
        print(f"Word not found in global vocab: {args.word}")
        return 2

    iid = internal_vocab.global_to_internal.get(int(gid))
    if iid is None:
        print(f"Word exists globally but not in internal vocab (not present in selected clients): {args.word}")
        return 2

    emb = weights.w_out if args.use_out else weights.w_in

    nn = nearest_neighbors(matrix=emb, query_id=int(iid), topk=args.topk)
    print(f"Query: {args.word} (global_id={gid}, internal_id={iid})")
    print(f"Matrix: {'w_out' if args.use_out else 'w_in'}  shape={emb.shape}")
    print("\nTop neighbors:")
    for rank, (nid, sim) in enumerate(nn, start=1):
        w = internal_to_word.get(nid, f"<internal:{nid}>")
        print(f"{rank:>2}. {w:<25}  cos={sim:.4f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
