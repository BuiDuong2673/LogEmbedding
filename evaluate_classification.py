"""Generate test logs from saved clusters and evaluate classification.

This script samples real log examples from `*_cluster_examples.json` and checks whether
classification via `*_templates.json` returns the expected cluster_id.

Examples:
  python evaluate_classification.py --client maryangel101 --clusters 50 --examples-per-cluster 5
  python evaluate_classification.py --templates dataset/templates/d2klab_templates.json \
      --examples dataset/templates/d2klab_cluster_examples.json --clusters 100 --examples-per-cluster 3

Outputs:
  - Prints summary accuracy to stdout.
  - Optionally saves JSONL records to dataset/test_logs/.
"""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

from helper.log_parser import LogParser


_DIGITS_RE = re.compile(r"\d+")


def _mutate_log(line: str, rng: random.Random) -> str:
    """Lightweight mutation to simulate unseen but similar logs."""

    def repl(match: re.Match[str]) -> str:
        token = match.group(0)
        # Preserve digit count to keep shape similar.
        return "".join(str(rng.randint(0, 9)) for _ in range(len(token)))

    mutated = _DIGITS_RE.sub(repl, line)
    # Small chance to tweak a single character (avoid empty string)
    if mutated and rng.random() < 0.15:
        pos = rng.randrange(len(mutated))
        mutated = mutated[:pos] + "_" + mutated[pos + 1 :]
    return mutated


def _iter_sampled_examples(
    clusters: Dict[str, Any],
    *,
    rng: random.Random,
    num_clusters: int,
    examples_per_cluster: int,
) -> Iterable[Tuple[int, str]]:
    cluster_ids = list(clusters.keys())
    if not cluster_ids:
        return

    # Prefer higher-count clusters first for stability.
    cluster_ids.sort(key=lambda cid: int(clusters[cid].get("count", 0)), reverse=True)
    cluster_ids = cluster_ids[: min(num_clusters, len(cluster_ids))]

    for cid in cluster_ids:
        payload = clusters[cid]
        examples: List[str] = payload.get("examples", [])
        if not examples:
            continue

        take = min(examples_per_cluster, len(examples))
        sampled = rng.sample(examples, k=take) if len(examples) >= take else list(examples)
        for line in sampled:
            yield int(cid), line


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate test logs and evaluate cluster classification")
    ap.add_argument("--client", default=None, help="Client name (infers template/example paths)")
    ap.add_argument("--templates", default=None, help="Path to *_templates.json")
    ap.add_argument("--examples", default=None, help="Path to *_cluster_examples.json")
    ap.add_argument("--clusters", type=int, default=50, help="How many clusters to sample")
    ap.add_argument("--examples-per-cluster", type=int, default=3, help="How many examples per cluster")
    ap.add_argument("--seed", type=int, default=0, help="Random seed")
    ap.add_argument("--mutate", action="store_true", help="Mutate sampled logs before classifying")
    ap.add_argument("--save", action="store_true", help="Save JSONL results into dataset/test_logs/")
    ap.add_argument(
        "--mode",
        choices=["templates", "examples"],
        default="templates",
        help="Matcher build mode: templates (fast) or examples (high coverage)",
    )
    ap.add_argument(
        "--rebuild-examples-per-cluster",
        type=int,
        default=20,
        help="When --mode examples: sample this many examples per cluster to rebuild the matcher",
    )
    ap.add_argument(
        "--rebuild-max-clusters",
        type=int,
        default=None,
        help="When --mode examples: cap number of clusters used to rebuild the matcher",
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
    correct_cluster_id = 0
    correct_template = 0
    no_match = 0

    records: List[Dict[str, Any]] = []

    for true_cluster_id, line in _iter_sampled_examples(
        clusters,
        rng=rng,
        num_clusters=args.clusters,
        examples_per_cluster=args.examples_per_cluster,
    ):
        true_template = str(clusters.get(str(true_cluster_id), {}).get("template", ""))
        test_line = _mutate_log(line, rng) if args.mutate else line
        template, predicted_cluster_id, confidence = lp.match_log_to_template(test_line)

        is_correct_cluster_id = predicted_cluster_id == true_cluster_id
        is_correct_template = bool(true_template) and template == true_template
        total += 1
        correct_cluster_id += 1 if is_correct_cluster_id else 0
        correct_template += 1 if is_correct_template else 0
        no_match += 1 if predicted_cluster_id == -1 else 0

        if args.save:
            records.append(
                {
                    "true_cluster_id": true_cluster_id,
                    "true_template": true_template,
                    "predicted_cluster_id": predicted_cluster_id,
                    "confidence": confidence,
                    "matched_template": template,
                    "log": test_line,
                    "mutated": args.mutate,
                    "source_templates": str(templates_path),
                    "source_examples": str(examples_path),
                }
            )

    acc_cluster = (correct_cluster_id / total) if total else 0.0
    acc_template = (correct_template / total) if total else 0.0
    print(f"templates: {templates_path}")
    print(f"examples:  {examples_path}")
    print(f"mode:      {args.mode}")
    print(f"sampled:   {total} logs from {min(args.clusters, len(clusters))} clusters")
    print(f"mutate:    {args.mutate}")
    print(f"correct(cluster_id): {correct_cluster_id}")
    print(f"correct(template):   {correct_template}")
    print(f"no_match:  {no_match}")
    print(f"accuracy(cluster_id): {acc_cluster:.4f}")
    print(f"accuracy(template):   {acc_template:.4f}")

    if args.save:
        out_dir = Path("dataset/test_logs")
        out_dir.mkdir(parents=True, exist_ok=True)
        tag = args.client or templates_path.stem.replace("_templates", "")
        out_path = out_dir / f"{tag}_classification_{'mutated' if args.mutate else 'raw'}_seed{args.seed}.jsonl"
        with out_path.open("w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"saved:     {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
