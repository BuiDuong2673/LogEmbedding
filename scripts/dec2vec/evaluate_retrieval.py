"""Evaluate dec2vec template retrieval on saved cluster examples.

This mirrors evaluate_classification.py, but for dec2vec cosine retrieval:
- true labels come from *_cluster_examples.json (cluster_id)
- predictions come from top-k template retrieval

Metrics:
- hit@1: top-1 retrieved template's cluster_id == true_cluster_id
- hit@k: true_cluster_id appears anywhere in the top-k list

Outputs:
- prints summary
- optionally saves JSONL to dataset/test_logs/dec2vec/

Example:
  python scripts/dec2vec/evaluate_retrieval.py \
    --client maryangel101 \
    --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
    --topk 5 --clusters 100 --examples-per-cluster 3 --save --save-md
"""

from __future__ import annotations

import argparse
import json
import random
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

# Ensure repo root is importable when running from scripts/
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from dec2vec.encoder import Dec2VecEncoder, Dec2VecEncoderConfig
from dec2vec.retrieval.template_retriever import Dec2VecTemplateRetriever, RetrievedTemplate


def _extract_cluster_id_from_tag(tag: str) -> Optional[int]:
    # Handles: "123" or "pass_123" / "fail_123"
    if not tag:
        return None
    if "_" in tag:
        tail = tag.split("_")[-1]
    else:
        tail = tag
    try:
        return int(tail)
    except ValueError:
        return None


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
            s = str(line).strip()
            if s:
                yield int(cid), s


def _to_jsonable_matches(matches: List[RetrievedTemplate], limit: int) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for m in matches[: max(0, int(limit))]:
        out.append(
            {
                "tag": m.tag,
                "cluster_id": _extract_cluster_id_from_tag(m.tag),
                "score": m.score,
                "template": m.template,
            }
        )
    return out


def _write_md_report(jsonl_path: Path, md_path: Path, limit: int = 200) -> None:
    records: List[Dict[str, Any]] = []
    with jsonl_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))

    if limit > 0:
        records = records[:limit]

    total = len(records)
    hit1 = sum(1 for r in records if r.get("hit_at_1") is True)
    hitk = sum(1 for r in records if r.get("hit_at_k") is True)

    lines: List[str] = []
    lines.append(f"# dec2vec Retrieval Report: {jsonl_path.name}")
    lines.append("")
    lines.append(f"- total: {total}")
    lines.append(f"- hit@1: {hit1} ({(hit1/total):.4f})" if total else "- hit@1: 0")
    lines.append(f"- hit@k: {hitk} ({(hitk/total):.4f})" if total else "- hit@k: 0")
    lines.append("")

    for i, r in enumerate(records, 1):
        lines.append(f"## #{i}")
        lines.append("")
        lines.append(f"- true_cluster_id: {r.get('true_cluster_id')}")
        lines.append(f"- hit@1: {r.get('hit_at_1')}")
        lines.append(f"- hit@k: {r.get('hit_at_k')}")
        lines.append("")
        lines.append("**log**")
        lines.append("```")
        lines.append(str(r.get("log", "")))
        lines.append("```")
        lines.append("")
        matches = r.get("top_matches")
        if isinstance(matches, list) and matches:
            lines.append("**top_matches**")
            for m in matches:
                tag = m.get("tag")
                cid = m.get("cluster_id")
                score = m.get("score")
                tmpl = str(m.get("template", ""))
                tmpl = tmpl if len(tmpl) <= 140 else tmpl[:140] + "..."
                lines.append(f"- score={score:.4f} tag={tag} cid={cid} tmpl=`{tmpl}`")
            lines.append("")

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Evaluate dec2vec template retrieval")
    ap.add_argument("--client", default=None, help="Client name (infers template/example paths)")
    ap.add_argument("--templates", default=None, help="Path to *_templates.json")
    ap.add_argument("--examples", default=None, help="Path to *_cluster_examples.json")

    ap.add_argument("--checkpoint", required=True, help="dec2vec checkpoint .npz")
    ap.add_argument("--topk", type=int, default=5)

    ap.add_argument("--clusters", type=int, default=50)
    ap.add_argument("--examples-per-cluster", type=int, default=3)
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--save", action="store_true")
    ap.add_argument("--save-md", action="store_true")
    ap.add_argument("--md-limit", type=int, default=200)

    ap.add_argument("--use-out", action="store_true")
    ap.add_argument("--no-normalize", action="store_true")

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

    enc = Dec2VecEncoder(
        checkpoint_path=args.checkpoint,
        config=Dec2VecEncoderConfig(use_out=args.use_out, normalize=not args.no_normalize),
    )

    retriever = Dec2VecTemplateRetriever(encoder=enc, template_dir=str(templates_path.parent), client_name=(args.client or templates_path.stem.replace("_templates", "")))
    retriever.load_templates()
    retriever.build_index()

    with examples_path.open("r", encoding="utf-8") as f:
        examples_data = json.load(f)
    clusters: Dict[str, Any] = examples_data.get("clusters", {})

    rng = random.Random(args.seed)

    total = 0
    hit1 = 0
    hitk = 0
    records: List[Dict[str, Any]] = []

    for true_cid, line in _iter_sampled_examples(
        clusters,
        rng=rng,
        num_clusters=args.clusters,
        examples_per_cluster=args.examples_per_cluster,
    ):
        matches = retriever.retrieve(line, top_k=args.topk)
        match_cids = [c for c in (_extract_cluster_id_from_tag(m.tag) for m in matches) if c is not None]

        is_hit1 = bool(match_cids) and match_cids[0] == true_cid
        is_hitk = true_cid in match_cids

        total += 1
        hit1 += 1 if is_hit1 else 0
        hitk += 1 if is_hitk else 0

        if args.save:
            records.append(
                {
                    "true_cluster_id": true_cid,
                    "log": line,
                    "topk": args.topk,
                    "hit_at_1": is_hit1,
                    "hit_at_k": is_hitk,
                    "top_matches": _to_jsonable_matches(matches, limit=args.topk),
                    "source_templates": str(templates_path),
                    "source_examples": str(examples_path),
                    "checkpoint": args.checkpoint,
                }
            )

    print(f"templates:   {templates_path}")
    print(f"examples:    {examples_path}")
    print(f"checkpoint:  {args.checkpoint}")
    print(f"sampled:     {total} logs")
    print(f"topk:        {args.topk}")
    print(f"hit@1:       {hit1}  acc@1={(hit1/total):.4f}" if total else "hit@1: 0")
    print(f"hit@k:       {hitk}  recall@k={(hitk/total):.4f}" if total else "hit@k: 0")

    if args.save:
        out_dir = Path("dataset/test_logs/dec2vec")
        out_dir.mkdir(parents=True, exist_ok=True)
        tag = args.client or templates_path.stem.replace("_templates", "")
        out_jsonl = out_dir / f"{tag}_dec2vec_retrieval_seed{args.seed}.jsonl"
        with out_jsonl.open("w", encoding="utf-8") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"saved:       {out_jsonl}")

        if args.save_md:
            out_md = out_jsonl.with_suffix(".md")
            _write_md_report(out_jsonl, out_md, limit=args.md_limit)
            print(f"saved(md):   {out_md}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
