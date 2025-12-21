"""Classify a log line into an existing cluster.

Usage examples:
    python classify_log.py --templates dataset/templates/d2klab_templates.json --log "CC H5detect.o"
    python classify_log.py --templates dataset/templates/maryangel101_templates.json

High-coverage mode (recommended):
    python classify_log.py --templates dataset/templates/d2klab_templates.json \
            --examples dataset/templates/d2klab_cluster_examples.json --mode examples \
            --examples-per-cluster 20 --max-clusters 2000 --log "CC H5detect.o"

Interactive mode (no --log):
  - Paste one log line per prompt
  - Empty line to exit
"""

from __future__ import annotations

import argparse

from helper.log_parser import LogParser


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify a log line into an existing cluster")
    parser.add_argument(
        "--templates",
        required=True,
        help="Path to *_templates.json produced by the parser",
    )
    parser.add_argument(
        "--examples",
        default=None,
        help="Path to *_cluster_examples.json (required for --mode examples)",
    )
    parser.add_argument(
        "--mode",
        choices=["templates", "examples"],
        default="templates",
        help="Matcher build mode: templates (fast) or examples (high coverage)",
    )
    parser.add_argument(
        "--examples-per-cluster",
        type=int,
        default=20,
        help="When --mode examples: sample this many examples per cluster",
    )
    parser.add_argument(
        "--max-clusters",
        type=int,
        default=None,
        help="When --mode examples: cap number of clusters used to rebuild matcher",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="When --mode examples: sampling seed",
    )
    parser.add_argument(
        "--log",
        default=None,
        help="A single log line to classify. If omitted, runs interactively.",
    )

    args = parser.parse_args()

    lp = LogParser()
    lp.load_templates(args.templates)
    if args.mode == "examples":
        if not args.examples:
            raise SystemExit("--examples is required when --mode examples")
        clusters = lp.load_cluster_examples(args.examples)
        lp.rebuild_matcher_from_cluster_examples(
            clusters,
            examples_per_cluster=args.examples_per_cluster,
            max_clusters=args.max_clusters,
            seed=args.seed,
        )

    def classify(line: str) -> None:
        template, cluster_id, confidence = lp.match_log_to_template(line)
        print(f"cluster_id={cluster_id} confidence={confidence}")
        print(f"template={template}")

    if args.log is not None:
        classify(args.log)
        return 0

    while True:
        try:
            line = input("log> ").strip("\n")
        except EOFError:
            break

        if not line.strip():
            break

        classify(line)
        print("-")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
