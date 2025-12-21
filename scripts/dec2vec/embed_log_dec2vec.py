"""Embed logs using a trained dec2vec checkpoint.

Moved under scripts/dec2vec/ to keep repo root tidy.

Examples:
  python scripts/dec2vec/embed_log_dec2vec.py --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
    --log "warning Resolution field is incompatible"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import List, Optional

import numpy as np

# Ensure repo root is importable when running from scripts/
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from dec2vec.encoder import Dec2VecEncoder, Dec2VecEncoderConfig


def _read_lines(path: str, max_lines: Optional[int] = None) -> List[str]:
    out: List[str] = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for i, line in enumerate(f):
            if max_lines is not None and i >= max_lines:
                break
            out.append(line.rstrip("\n"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Embed logs with dec2vec")
    ap.add_argument("--checkpoint", required=True, help="Path to dec2vec .npz checkpoint")

    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--log", help="Single log line to embed")
    src.add_argument("--input-file", help="Text file with one log per line")

    ap.add_argument("--output", help="Write outputs to .jsonl or .npy (optional)")
    ap.add_argument("--max-lines", type=int, default=None)

    ap.add_argument("--use-out", action="store_true", help="Use output embeddings W_out")
    ap.add_argument("--no-normalize", action="store_true", help="Disable L2 normalization of log vectors")

    ap.add_argument("--global-vocab", default="dataset/global_vocab_index.json")
    ap.add_argument("--internal-vocab", default="dataset/internal_central_vocab.json")

    args = ap.parse_args()

    enc = Dec2VecEncoder(
        checkpoint_path=args.checkpoint,
        global_vocab_path=args.global_vocab,
        internal_vocab_path=args.internal_vocab,
        config=Dec2VecEncoderConfig(use_out=args.use_out, normalize=not args.no_normalize),
    )

    if args.log is not None:
        v = enc.embed_log_line(args.log)
        payload = {"dim": int(v.shape[0]), "vector": v.tolist(), "log": args.log}
        if args.output:
            if args.output.endswith(".json"):
                with open(args.output, "w", encoding="utf-8") as f:
                    json.dump(payload, f, ensure_ascii=False, indent=2)
            else:
                with open(args.output, "w", encoding="utf-8") as f:
                    json.dump(payload, f, ensure_ascii=False)
            print(f"✓ Wrote: {args.output}")
        else:
            print(json.dumps(payload, ensure_ascii=False))
        return 0

    assert args.input_file is not None
    lines = _read_lines(args.input_file, max_lines=args.max_lines)
    mat = enc.embed_log_lines(lines)

    if not args.output:
        print(f"Embedded {mat.shape[0]} lines -> matrix shape {mat.shape}")
        print("Tip: pass --output out.jsonl or --output out.npy")
        return 0

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)

    if args.output.endswith(".npy"):
        np.save(args.output, mat)
        print(f"✓ Wrote: {args.output}  shape={mat.shape}")
        return 0

    with open(args.output, "w", encoding="utf-8") as f:
        for line, vec in zip(lines, mat):
            rec = {"log": line, "vector": vec.tolist()}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"✓ Wrote: {args.output}  lines={len(lines)} dim={mat.shape[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
