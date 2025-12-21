"""Retrieve the most similar log lines to a query log using dec2vec.

This implements: "I input a new log; it should find the most similar log(s)."

Knowledge base (candidate set): a plain text file with one log line per row.
No Drain is involved.

Example:
  python scripts/dec2vec/retrieve_logs.py \
    --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
    --corpus-file dataset/some_logs.txt \
    --log "..." --topk 5

Or via stdin:
  echo "my query log" | python scripts/dec2vec/retrieve_logs.py --checkpoint ... --corpus-file ...
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import List, Optional, Tuple

# Ensure repo root is importable when running from scripts/
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from dec2vec.encoder import Dec2VecEncoder, Dec2VecEncoderConfig
from dec2vec.retrieval.text_retriever import Dec2VecTextRetriever
from dec2vec.data import remove_timestamp


def _read_query(args: argparse.Namespace) -> str:
    if args.log is not None and str(args.log).strip():
        return str(args.log).strip()

    if args.log_file:
        p = Path(args.log_file)
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        for line in lines:
            s = line.strip()
            if s:
                return s
        return ""

    if sys.stdin.isatty():
        raise SystemExit("Provide --log/--log-file, or pipe query log via stdin")

    # stdin: first non-empty line
    for line in sys.stdin.read().splitlines():
        s = str(line).strip("\r\n")
        if s.strip():
            return s.strip()

    return ""


def _load_corpus(path: Path, *, max_lines: Optional[int], dedup: bool) -> List[str]:
    raw = path.read_text(encoding="utf-8", errors="replace").splitlines()
    out: List[str] = []
    seen = set()

    limit = None if max_lines is None else max(0, int(max_lines))

    for line in raw:
        s = str(line).strip("\r\n")
        s = s.strip()
        if not s:
            continue
        if dedup:
            if s in seen:
                continue
            seen.add(s)
        out.append(s)
        if limit is not None and len(out) >= limit:
            break

    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Retrieve nearest log lines to a query using dec2vec cosine similarity")
    ap.add_argument("--checkpoint", required=True, help="dec2vec checkpoint .npz")

    ap.add_argument("--corpus-file", required=True, help="Text file with one log line per row")
    ap.add_argument("--max-lines", type=int, default=None, help="Optional cap on corpus lines loaded")
    ap.add_argument("--dedup", action="store_true", help="Deduplicate identical corpus lines")

    ap.add_argument("--log", default=None, help="Query log line")
    ap.add_argument("--log-file", default=None, help="Read query log from file")

    ap.add_argument("--topk", type=int, default=5)
    ap.add_argument("--threshold", type=float, default=None, help="If set, only print matches with score >= threshold")

    ap.add_argument("--strip-timestamp", action="store_true", help="Remove timestamp prefix before tokenization")
    ap.add_argument("--use-out", action="store_true")
    ap.add_argument("--no-normalize", action="store_true", help="Disable L2-normalization of pooled embedding")

    ap.add_argument("--show-text", type=int, default=220, help="Max chars of matched text to print")

    args = ap.parse_args()

    corpus_path = Path(args.corpus_file)
    if not corpus_path.exists():
        raise FileNotFoundError(f"corpus file not found: {corpus_path}")

    query = _read_query(args)
    if not query:
        raise SystemExit("Empty query log")

    corpus = _load_corpus(corpus_path, max_lines=args.max_lines, dedup=bool(args.dedup))
    if not corpus:
        raise SystemExit("Empty corpus")

    enc = Dec2VecEncoder(
        checkpoint_path=args.checkpoint,
        config=Dec2VecEncoderConfig(use_out=args.use_out, normalize=not args.no_normalize),
    )

    strip_ts = bool(args.strip_timestamp)

    retriever = Dec2VecTextRetriever(encoder=enc)
    # tag is line index in the loaded corpus
    retriever.set_items(((str(i), line) for i, line in enumerate(corpus)))
    retriever.build_index(strip_timestamp=strip_ts)

    matches = retriever.retrieve(query, top_k=int(args.topk), strip_timestamp=strip_ts)

    thr = float(args.threshold) if args.threshold is not None else None

    print(f"checkpoint:   {args.checkpoint}")
    print(f"corpus_file:  {corpus_path}")
    print(f"corpus_size:  {len(corpus)}")
    print(f"dim:          {enc.dim}")
    print(f"strip_ts:     {strip_ts}")
    print(f"normalize:    {not args.no_normalize}")
    print(f"use_out:      {bool(args.use_out)}")
    print(f"topk:         {int(args.topk)}")
    if thr is not None:
        print(f"threshold:    {thr:.6f}")
    print("\nquery:")
    print(remove_timestamp(query) if strip_ts else query)

    print("\nmatches:")
    shown = 0
    for m in matches:
        if thr is not None and m.score < thr:
            continue
        text = remove_timestamp(m.text) if strip_ts else m.text
        cap = max(0, int(args.show_text))
        if cap and len(text) > cap:
            text = text[:cap] + "..."
        print(f"- score={m.score:.6f} idx={m.tag} text={text}")
        shown += 1

    if shown == 0:
        print("(no matches above threshold)" if thr is not None else "(no matches)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
