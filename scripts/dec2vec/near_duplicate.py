"""Near-duplicate detection via dec2vec cosine similarity.

This script compares TWO log lines by embedding them with Dec2VecEncoder and
computing cosine similarity. No knowledge base is used.

Typical usage:
  python scripts/dec2vec/near_duplicate.py \
    --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
    --log1 "..." --log2 "..." --threshold 0.85

You can also pipe two lines via stdin:
  printf "line1\nline2\n" | python scripts/dec2vec/near_duplicate.py --checkpoint ...
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Optional, Tuple

import numpy as np

# Ensure repo root is importable when running from scripts/
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from dec2vec.encoder import Dec2VecEncoder, Dec2VecEncoderConfig
from dec2vec.data import remove_timestamp


def _read_two_lines_from_stdin() -> Tuple[str, str]:
    data = sys.stdin.read().splitlines()
    data = [x for x in (d.strip("\r") for d in data) if x is not None]
    # Keep empty lines out
    data = [x for x in data if x.strip()]
    if len(data) < 2:
        raise SystemExit("stdin requires at least 2 non-empty lines (log1, log2)")
    return data[0], data[1]


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    an = float(np.linalg.norm(a))
    bn = float(np.linalg.norm(b))
    if an <= 1e-12 or bn <= 1e-12:
        return 0.0
    return float((a @ b) / (an * bn))


def main() -> int:
    ap = argparse.ArgumentParser(description="Near-duplicate detection with dec2vec cosine similarity")

    ap.add_argument("--checkpoint", required=True, help="dec2vec checkpoint .npz")

    ap.add_argument("--log1", default=None, help="First log line")
    ap.add_argument("--log2", default=None, help="Second log line")

    ap.add_argument("--log1-file", default=None, help="Read first log line from file")
    ap.add_argument("--log2-file", default=None, help="Read second log line from file")

    ap.add_argument("--threshold", type=float, default=None, help="If set, print decision based on score >= threshold")

    ap.add_argument("--strip-timestamp", action="store_true", help="Remove timestamp prefix before tokenization")
    ap.add_argument("--use-out", action="store_true")
    ap.add_argument("--no-normalize", action="store_true", help="Disable L2-normalization of pooled embedding")

    args = ap.parse_args()

    def read_file_line(p: Optional[str]) -> Optional[str]:
        if not p:
            return None
        path = Path(p)
        txt = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for line in txt:
            s = line.strip()
            if s:
                return s
        return ""

    log1 = args.log1 or read_file_line(args.log1_file)
    log2 = args.log2 or read_file_line(args.log2_file)

    if (log1 is None or not str(log1).strip()) or (log2 is None or not str(log2).strip()):
        if sys.stdin.isatty():
            raise SystemExit("Provide --log1/--log2 or --log1-file/--log2-file, or pipe two lines via stdin")
        log1, log2 = _read_two_lines_from_stdin()

    enc = Dec2VecEncoder(
        checkpoint_path=args.checkpoint,
        config=Dec2VecEncoderConfig(use_out=args.use_out, normalize=not args.no_normalize),
    )

    v1 = enc.embed_log_line(str(log1), strip_timestamp=bool(args.strip_timestamp))
    v2 = enc.embed_log_line(str(log2), strip_timestamp=bool(args.strip_timestamp))

    score = _cosine(v1.astype(np.float32, copy=False), v2.astype(np.float32, copy=False))

    print(f"checkpoint:  {args.checkpoint}")
    print(f"dim:         {enc.dim}")
    print(f"strip_ts:    {bool(args.strip_timestamp)}")
    print(f"normalize:   {not args.no_normalize}")
    print(f"use_out:     {bool(args.use_out)}")
    print(f"cosine:      {score:.6f}")

    if bool(args.strip_timestamp):
        print("\nlog1(stripped):")
        print(remove_timestamp(str(log1)))
        print("\nlog2(stripped):")
        print(remove_timestamp(str(log2)))

    if args.threshold is not None:
        thr = float(args.threshold)
        decision = "NEAR_DUP" if score >= thr else "NOT_DUP"
        print(f"threshold:   {thr:.6f}")
        print(f"decision:    {decision}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
