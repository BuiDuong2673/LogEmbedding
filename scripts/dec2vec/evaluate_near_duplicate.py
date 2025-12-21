"""Evaluate near-duplicate detection with dec2vec cosine similarity (NO clusters).

This evaluation does NOT depend on Drain templates or Drain cluster labels.

How labels are created:
- Positive pairs: (base_log, mutate(base_log))
- Negative pairs: (base_log, other_random_log)

We then embed both sides with Dec2VecEncoder and score with cosine similarity.

Metrics:
- AUROC (approx, computed without sklearn)
- Best-F1 threshold (grid over unique scores)

Example:
  python scripts/dec2vec/evaluate_near_duplicate.py \
    --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
    --corpus-file dataset/some_logs.txt \
    --pairs 200 --neg-per-pos 1 --mutation-steps 2 --seed 0
"""

from __future__ import annotations

import argparse
import os
import random
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

import numpy as np

# Ensure repo root is importable when running from scripts/
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from dec2vec.encoder import Dec2VecEncoder, Dec2VecEncoderConfig


_VERSION_RE = re.compile(r"\b(?:v)?\d+\.\d+(?:\.\d+)*\b")
_IP_RE = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")
_UUID_RE = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b")
_HEX_RE = re.compile(r"\b[0-9a-fA-F]{16,64}\b")
_DIGITS_RE = re.compile(r"\d+")
_PATH_RE = re.compile(r"(?:/[^\s]+)+")


def _bump_version(text: str, rng: random.Random) -> str:
    matches = list(_VERSION_RE.finditer(text))
    if not matches:
        return text
    m = rng.choice(matches)
    old = m.group(0)
    prefix = ""
    core = old
    if core.startswith("v") and len(core) > 1:
        prefix, core = "v", core[1:]

    parts = core.split(".")
    idx = rng.randrange(len(parts))
    try:
        val = int(parts[idx])
        delta = rng.choice([-1, 1, 2])
        parts[idx] = str(max(0, val + delta))
    except ValueError:
        return text
    new = prefix + ".".join(parts)
    return text[: m.start()] + new + text[m.end() :]


def _swap_number(text: str, rng: random.Random) -> str:
    matches = list(_DIGITS_RE.finditer(text))
    if not matches:
        return text
    m = rng.choice(matches)
    old = m.group(0)
    new = "".join(str(rng.randint(0, 9)) for _ in range(len(old)))
    return text[: m.start()] + new + text[m.end() :]


def _swap_ip(text: str, rng: random.Random) -> str:
    matches = list(_IP_RE.finditer(text))
    if not matches:
        return text
    m = rng.choice(matches)
    octets = [str(rng.randint(0, 255)) for _ in range(4)]
    new = ".".join(octets)
    return text[: m.start()] + new + text[m.end() :]


def _swap_uuid(text: str, rng: random.Random) -> str:
    matches = list(_UUID_RE.finditer(text))
    if not matches:
        return text
    m = rng.choice(matches)
    hexchars = "0123456789abcdef"

    def rand_hex(n: int) -> str:
        return "".join(rng.choice(hexchars) for _ in range(n))

    new = f"{rand_hex(8)}-{rand_hex(4)}-{rand_hex(4)}-{rand_hex(4)}-{rand_hex(12)}"
    return text[: m.start()] + new + text[m.end() :]


def _swap_hex(text: str, rng: random.Random) -> str:
    matches = list(_HEX_RE.finditer(text))
    if not matches:
        return text
    m = rng.choice(matches)
    old = m.group(0)
    hexchars = "0123456789abcdef"
    new = "".join(rng.choice(hexchars) for _ in range(len(old)))
    return text[: m.start()] + new + text[m.end() :]


def _tweak_path(text: str, rng: random.Random) -> str:
    matches = list(_PATH_RE.finditer(text))
    if not matches:
        return text
    m = rng.choice(matches)
    path = m.group(0)
    parts = path.split("/")
    if len(parts) <= 2:
        return text

    idxs = [i for i, p in enumerate(parts) if p]
    idx = rng.choice(idxs)
    seg = parts[idx]
    if not seg:
        return text

    suffix = rng.choice(["_v2", "-new", "_backup", "-x86_64"])
    if len(seg) > 30:
        seg = seg[:30]
    parts[idx] = seg + suffix
    new_path = "/".join(parts)
    return text[: m.start()] + new_path + text[m.end() :]


def _errorize(text: str, rng: random.Random) -> str:
    lower = text.lower()
    if "warning" in lower and rng.random() < 0.7:
        return re.sub(r"warning", "error", text, count=1, flags=re.IGNORECASE)
    if "error" in lower:
        return text
    if rng.random() < 0.35:
        return "Error: " + text
    return text


_MUTATORS = [_bump_version, _swap_number, _swap_ip, _swap_uuid, _swap_hex, _tweak_path, _errorize]


def mutate_log(base: str, rng: random.Random, steps: int = 2) -> str:
    out = base
    for _ in range(max(1, int(steps))):
        mut = rng.choice(_MUTATORS)
        out2 = mut(out, rng)
        if out2 != out:
            out = out2
    return out


def _load_corpus(path: Path, *, max_lines: Optional[int], dedup: bool) -> List[str]:
    raw = path.read_text(encoding="utf-8", errors="replace").splitlines()
    out: List[str] = []
    seen = set()

    limit = None if max_lines is None else max(0, int(max_lines))

    for line in raw:
        s = str(line).strip("\r\n").strip()
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


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    an = float(np.linalg.norm(a))
    bn = float(np.linalg.norm(b))
    if an <= 1e-12 or bn <= 1e-12:
        return 0.0
    return float((a @ b) / (an * bn))


def _auc_roc(scores: Sequence[float], labels: Sequence[int]) -> float:
    # Computes AUROC by ranking. labels: 1 positive, 0 negative.
    pairs = sorted(zip(scores, labels), key=lambda x: x[0])
    n_pos = sum(1 for _, y in pairs if y == 1)
    n_neg = len(pairs) - n_pos
    if n_pos == 0 or n_neg == 0:
        return 0.0

    # Mann–Whitney U: probability that a random positive ranks above a random negative.
    # Handle ties by average rank.
    ranks = [0.0] * len(pairs)
    i = 0
    r = 1
    while i < len(pairs):
        j = i
        while j < len(pairs) and pairs[j][0] == pairs[i][0]:
            j += 1
        avg_rank = (r + (r + (j - i) - 1)) / 2.0
        for k in range(i, j):
            ranks[k] = avg_rank
        r += (j - i)
        i = j

    sum_ranks_pos = sum(rank for rank, (_, y) in zip(ranks, pairs) if y == 1)
    u_pos = sum_ranks_pos - (n_pos * (n_pos + 1)) / 2.0
    return float(u_pos / (n_pos * n_neg))


@dataclass(frozen=True)
class ThresholdResult:
    threshold: float
    f1: float
    precision: float
    recall: float
    accuracy: float


def _best_f1_threshold(scores: Sequence[float], labels: Sequence[int]) -> ThresholdResult:
    # Scan thresholds at unique scores (descending) for best F1.
    items = list(zip(scores, labels))
    if not items:
        return ThresholdResult(threshold=0.0, f1=0.0, precision=0.0, recall=0.0, accuracy=0.0)

    uniq = sorted(set(scores), reverse=True)
    best = ThresholdResult(threshold=uniq[0], f1=-1.0, precision=0.0, recall=0.0, accuracy=0.0)

    total = len(labels)
    pos_total = sum(1 for y in labels if y == 1)

    for thr in uniq:
        tp = fp = tn = fn = 0
        for s, y in items:
            pred = 1 if s >= thr else 0
            if pred == 1 and y == 1:
                tp += 1
            elif pred == 1 and y == 0:
                fp += 1
            elif pred == 0 and y == 0:
                tn += 1
            else:
                fn += 1

        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
        acc = (tp + tn) / total if total else 0.0

        if f1 > best.f1:
            best = ThresholdResult(threshold=float(thr), f1=float(f1), precision=float(precision), recall=float(recall), accuracy=float(acc))

    return best


def main() -> int:
    ap = argparse.ArgumentParser(description="Evaluate near-duplicate detection with dec2vec (no clusters)")
    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--corpus-file", required=True)

    ap.add_argument("--pairs", type=int, default=200, help="Number of base logs sampled")
    ap.add_argument("--neg-per-pos", type=int, default=1)

    ap.add_argument("--mutation-steps", type=int, default=2)
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--max-lines", type=int, default=None)
    ap.add_argument("--dedup", action="store_true")

    ap.add_argument("--strip-timestamp", action="store_true")
    ap.add_argument("--use-out", action="store_true")
    ap.add_argument("--no-normalize", action="store_true")

    args = ap.parse_args()

    corpus_path = Path(args.corpus_file)
    if not corpus_path.exists():
        raise FileNotFoundError(f"corpus file not found: {corpus_path}")

    rng = random.Random(args.seed)

    corpus = _load_corpus(corpus_path, max_lines=args.max_lines, dedup=bool(args.dedup))
    if len(corpus) < 3:
        raise SystemExit("Corpus too small; need at least 3 non-empty lines")

    pairs_n = min(max(1, int(args.pairs)), len(corpus))
    base_logs = rng.sample(corpus, k=pairs_n) if len(corpus) >= pairs_n else list(corpus)

    enc = Dec2VecEncoder(
        checkpoint_path=args.checkpoint,
        config=Dec2VecEncoderConfig(use_out=args.use_out, normalize=not args.no_normalize),
    )

    strip_ts = bool(args.strip_timestamp)

    scores: List[float] = []
    labels: List[int] = []

    # Pre-embed all corpus lines for speed on negatives
    corpus_vecs = enc.embed_log_lines(corpus, strip_timestamp=strip_ts)

    for base in base_logs:
        base_vec = enc.embed_log_line(base, strip_timestamp=strip_ts)

        # Positive
        mutated = mutate_log(base, rng, steps=int(args.mutation_steps))
        mut_vec = enc.embed_log_line(mutated, strip_timestamp=strip_ts)
        scores.append(_cosine(base_vec, mut_vec))
        labels.append(1)

        # Negatives
        for _ in range(max(1, int(args.neg_per_pos))):
            # choose a random different line
            j = rng.randrange(len(corpus))
            other = corpus[j]
            if other == base:
                j = (j + 1) % len(corpus)
            other_vec = corpus_vecs[j]
            scores.append(_cosine(base_vec, other_vec))
            labels.append(0)

    auc = _auc_roc(scores, labels)
    best = _best_f1_threshold(scores, labels)

    pos_scores = [s for s, y in zip(scores, labels) if y == 1]
    neg_scores = [s for s, y in zip(scores, labels) if y == 0]

    def pct(xs: List[float], p: float) -> float:
        if not xs:
            return 0.0
        xs2 = sorted(xs)
        k = int(round((len(xs2) - 1) * p))
        return float(xs2[max(0, min(len(xs2) - 1, k))])

    print(f"checkpoint:    {args.checkpoint}")
    print(f"corpus_file:   {corpus_path}")
    print(f"corpus_size:   {len(corpus)}")
    print(f"pairs:         {pairs_n} (pos={pairs_n}, neg={pairs_n*max(1,int(args.neg_per_pos))})")
    print(f"dim:           {enc.dim}")
    print(f"strip_ts:      {strip_ts}")
    print(f"normalize:     {not args.no_normalize}")
    print(f"use_out:       {bool(args.use_out)}")
    print("")
    print(f"AUROC:         {auc:.4f}")
    print(f"best_f1:       {best.f1:.4f} @ thr={best.threshold:.6f}")
    print(f"precision:     {best.precision:.4f}")
    print(f"recall:        {best.recall:.4f}")
    print(f"accuracy:      {best.accuracy:.4f}")
    print("")
    print("score_stats:")
    print(f"  pos_p10/p50/p90: {pct(pos_scores,0.10):.4f} / {pct(pos_scores,0.50):.4f} / {pct(pos_scores,0.90):.4f}")
    print(f"  neg_p10/p50/p90: {pct(neg_scores,0.10):.4f} / {pct(neg_scores,0.50):.4f} / {pct(neg_scores,0.90):.4f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
