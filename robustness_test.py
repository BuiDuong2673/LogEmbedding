"""Generate mutated test logs from cluster examples and evaluate robustness.

Goal
- Start from real examples in `*_cluster_examples.json`
- Generate mutation variants (numbers, versions, paths, error/warning)
- Classify each mutated log into an existing cluster
- Save a detailed JSONL report including predicted cluster and sample examples

Examples
  python robustness_test.py --client maryangel101 --mode examples \
      --rebuild-max-clusters 200 --rebuild-examples-per-cluster 30 \
      --clusters 20 --base-examples-per-cluster 2 --mutations-per-example 3 \
    --show-examples 3 --seed 0 --save --save-md

  python robustness_test.py --client d2klab --mode examples \
      --rebuild-max-clusters 1000 --rebuild-examples-per-cluster 20 \
      --clusters 30 --base-examples-per-cluster 1 --mutations-per-example 2 \
      --show-examples 2 --seed 0 --save
"""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from helper.log_parser import LogParser
from format_test_logs import format_jsonl_file


_VERSION_RE = re.compile(r"\b(?:v)?\d+\.\d+(?:\.\d+)*\b")
_IP_RE = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")
_UUID_RE = re.compile(
    r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"
)
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
    # bump a random component
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
    # Keep UUID shape; random hex is fine for robustness testing.
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

    # Choose a segment (ignore leading empty due to absolute path)
    idxs = [i for i, p in enumerate(parts) if p]
    idx = rng.choice(idxs)
    seg = parts[idx]
    if not seg:
        return text

    # Insert a small suffix/prefix
    suffix = rng.choice(["_v2", "-new", "_backup", "-x86_64"])
    if len(seg) > 30:
        seg = seg[:30]
    parts[idx] = seg + suffix
    new_path = "/".join(parts)
    return text[: m.start()] + new_path + text[m.end() :]


def _errorize(text: str, rng: random.Random) -> str:
    lower = text.lower()
    if "warning" in lower and rng.random() < 0.7:
        # Replace the first occurrence in a case-insensitive-ish way
        return re.sub(r"warning", "error", text, count=1, flags=re.IGNORECASE)
    if "error" in lower:
        return text
    if rng.random() < 0.35:
        return "Error: " + text
    return text


_MUTATORS = [
    _bump_version,
    _swap_number,
    _swap_ip,
    _swap_uuid,
    _swap_hex,
    _tweak_path,
    _errorize,
]


def mutate_log(base: str, rng: random.Random, steps: int = 2) -> str:
    out = base
    for _ in range(max(1, steps)):
        mut = rng.choice(_MUTATORS)
        out2 = mut(out, rng)
        # ensure progress if possible
        if out2 != out:
            out = out2
    return out


def iter_base_examples(
    clusters: Dict[str, Any],
    *,
    rng: random.Random,
    num_clusters: int,
    base_examples_per_cluster: int,
) -> Iterable[Tuple[int, str]]:
    cluster_ids = list(clusters.keys())
    if not cluster_ids:
        return

    # Prefer higher-count clusters first.
    cluster_ids.sort(key=lambda cid: int(clusters[cid].get("count", 0)), reverse=True)
    cluster_ids = cluster_ids[: min(num_clusters, len(cluster_ids))]

    for cid in cluster_ids:
        payload = clusters[cid]
        examples: List[str] = payload.get("examples", [])
        if not examples:
            continue

        take = min(base_examples_per_cluster, len(examples))
        sampled = rng.sample(examples, k=take) if len(examples) >= take else list(examples)
        for line in sampled:
            if line and str(line).strip():
                yield int(cid), str(line).strip()


def main() -> int:
    ap = argparse.ArgumentParser(description="Mutate cluster examples and test classification robustness")
    ap.add_argument("--client", default=None, help="Client name (infers paths)")
    ap.add_argument("--templates", default=None, help="Path to *_templates.json")
    ap.add_argument("--examples", default=None, help="Path to *_cluster_examples.json")

    ap.add_argument("--mode", choices=["templates", "examples"], default="examples")
    ap.add_argument("--rebuild-examples-per-cluster", type=int, default=20)
    ap.add_argument("--rebuild-max-clusters", type=int, default=200)

    ap.add_argument("--clusters", type=int, default=20, help="How many clusters to sample from")
    ap.add_argument("--base-examples-per-cluster", type=int, default=1)
    ap.add_argument("--mutations-per-example", type=int, default=3)
    ap.add_argument("--mutation-steps", type=int, default=2, help="How many mutator steps per mutation")

    ap.add_argument("--show-examples", type=int, default=3, help="How many examples to include in report")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--save", action="store_true")
    ap.add_argument("--save-md", action="store_true", help="When --save: also write a Markdown report")
    ap.add_argument("--md-limit", type=int, default=200, help="When --save-md: max records to render")
    ap.add_argument(
        "--md-output",
        default=None,
        help="When --save-md: output .md path (default next to .jsonl)",
    )

    args = ap.parse_args()

    if args.client:
        templates_path = Path("dataset/templates") / f"{args.client}_templates.json"
        examples_path = Path("dataset/templates") / f"{args.client}_cluster_examples.json"
    else:
        if not args.templates or not args.examples:
            ap.error("Provide --client OR both --templates and --examples")
        templates_path = Path(args.templates)
        examples_path = Path(args.examples)

    if not templates_path.exists():
        raise FileNotFoundError(f"templates not found: {templates_path}")
    if not examples_path.exists():
        raise FileNotFoundError(f"examples not found: {examples_path}")

    lp = LogParser()
    lp.load_templates(str(templates_path))

    with examples_path.open("r", encoding="utf-8") as f:
        examples_data = json.load(f)

    clusters: Dict[str, Any] = examples_data.get("clusters", {})

    if args.mode == "examples":
        lp.rebuild_matcher_from_cluster_examples(
            clusters,
            examples_per_cluster=args.rebuild_examples_per_cluster,
            max_clusters=args.rebuild_max_clusters,
            seed=args.seed,
        )

    rng = random.Random(args.seed)

    total = 0
    correct_cluster = 0
    no_match = 0

    records: List[Dict[str, Any]] = []

    for true_cluster_id, base in iter_base_examples(
        clusters,
        rng=rng,
        num_clusters=args.clusters,
        base_examples_per_cluster=args.base_examples_per_cluster,
    ):
        for _ in range(max(1, args.mutations_per_example)):
            mutated = mutate_log(base, rng, steps=args.mutation_steps)
            matched_template, predicted_cluster_id, confidence = lp.match_log_to_template(mutated)

            total += 1
            is_correct = predicted_cluster_id == true_cluster_id
            correct_cluster += 1 if is_correct else 0
            no_match += 1 if predicted_cluster_id == -1 else 0

            pred_examples: List[str] = []
            pred_count: Optional[int] = None
            if predicted_cluster_id != -1:
                pred_payload = clusters.get(str(predicted_cluster_id), {})
                pred_count = int(pred_payload.get("count", 0)) if pred_payload else None
                all_examples = list(pred_payload.get("examples", [])) if pred_payload else []
                pred_examples = all_examples[: max(0, args.show_examples)]

            records.append(
                {
                    "true_cluster_id": true_cluster_id,
                    "true_template": str(clusters.get(str(true_cluster_id), {}).get("template", "")),
                    "base_log": base,
                    "mutated_log": mutated,
                    "predicted_cluster_id": predicted_cluster_id,
                    "confidence": confidence,
                    "matched_template": matched_template,
                    "predicted_cluster_count": pred_count,
                    "predicted_cluster_examples": pred_examples,
                    "mode": args.mode,
                    "rebuild_examples_per_cluster": args.rebuild_examples_per_cluster if args.mode == "examples" else None,
                    "rebuild_max_clusters": args.rebuild_max_clusters if args.mode == "examples" else None,
                    "seed": args.seed,
                    "correct": is_correct,
                }
            )

    acc = (correct_cluster / total) if total else 0.0
    print(f"templates: {templates_path}")
    print(f"examples:  {examples_path}")
    print(f"mode:      {args.mode}")
    print(f"total:     {total}")
    print(f"correct(cluster_id): {correct_cluster}")
    print(f"no_match:  {no_match}")
    print(f"accuracy:  {acc:.4f}")

    if args.save:
        out_dir = Path("dataset/test_logs")
        out_dir.mkdir(parents=True, exist_ok=True)
        tag = args.client or templates_path.stem.replace("_templates", "")
        out_path = out_dir / f"{tag}_robustness_mode-{args.mode}_seed{args.seed}.jsonl"
        with out_path.open("w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"saved:     {out_path}")

        if args.save_md:
            md_path = Path(args.md_output) if args.md_output else out_path.with_suffix(".md")
            format_jsonl_file(
                input_path=out_path,
                output_path=md_path,
                fmt="md",
                limit=args.md_limit,
                quiet=False,
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())