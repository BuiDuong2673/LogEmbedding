"""Build a plain-text log corpus file from one or more dataset directories.

This is intended for retrieval / near-duplicate detection WITHOUT using Drain.
It reads *.txt (configurable) files recursively and writes one log line per row.

Example:
  python scripts/dec2vec/build_corpus.py \
    --input-dir dataset/d2klab --input-dir dataset/maryangel101 \
    --glob "*.txt" --dedup --max-lines 200000 \
    --output-file dataset/corpus/all_logs.txt
"""

from __future__ import annotations

import argparse
import os
import random
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Sequence


def _iter_files(input_dirs: Sequence[Path], pattern: str) -> List[Path]:
    files: List[Path] = []
    for d in input_dirs:
        if not d.exists():
            continue
        if d.is_file():
            files.append(d)
            continue
        files.extend(sorted(d.rglob(pattern)))
    # Keep only regular files
    files = [p for p in files if p.is_file()]
    return files


def _iter_lines_from_file(path: Path) -> Iterable[str]:
    # Read with replacement to be robust
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    for line in text.splitlines():
        s = str(line).strip("\r\n")
        s = s.strip()
        if not s:
            continue
        yield s


def main() -> int:
    ap = argparse.ArgumentParser(description="Build a corpus file from dataset directories")
    ap.add_argument("--input-dir", action="append", required=True, help="Directory (or file) to scan; can be repeated")
    ap.add_argument("--glob", default="*.txt", help="File glob pattern to include (recursive)")

    ap.add_argument("--output-file", required=True, help="Where to write the corpus (one line per log)")

    ap.add_argument("--max-files", type=int, default=None, help="Optional cap on number of files scanned")
    ap.add_argument("--max-lines", type=int, default=None, help="Optional cap on number of lines written")

    ap.add_argument("--dedup", action="store_true", help="Deduplicate identical lines")
    ap.add_argument("--shuffle", action="store_true", help="Shuffle output lines")
    ap.add_argument("--seed", type=int, default=0)

    args = ap.parse_args()

    input_dirs = [Path(x) for x in args.input_dir]
    out_path = Path(args.output_file)

    files = _iter_files(input_dirs, str(args.glob))
    if not files:
        raise SystemExit("No input files matched")

    if args.max_files is not None:
        files = files[: max(0, int(args.max_files))]

    seen = set()
    lines: List[str] = []

    max_lines = None if args.max_lines is None else max(0, int(args.max_lines))

    for fp in files:
        for s in _iter_lines_from_file(fp):
            if args.dedup:
                if s in seen:
                    continue
                seen.add(s)
            lines.append(s)
            if max_lines is not None and len(lines) >= max_lines:
                break
        if max_lines is not None and len(lines) >= max_lines:
            break

    if args.shuffle and lines:
        rng = random.Random(int(args.seed))
        rng.shuffle(lines)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")

    print(f"inputs:      {[str(p) for p in input_dirs]}")
    print(f"glob:        {args.glob}")
    print(f"files:       {len(files)}")
    print(f"lines:       {len(lines)}")
    print(f"dedup:       {bool(args.dedup)}")
    print(f"shuffle:     {bool(args.shuffle)}")
    print(f"output:      {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
