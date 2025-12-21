"""Evaluate dec2vec retrieval when the knowledge base is **raw cluster examples**.

This answers the question: "If we do NOT do Drain templateization, how bad is retrieval?"

Ground truth:
- true labels come from *_cluster_examples.json (cluster_id)

Knowledge base:
- built from sampled examples per cluster (raw text, no Drain templates)

Prediction:
- retrieve top-k raw KB entries via cosine similarity of dec2vec embeddings
- hit@1: top-1 retrieved entry's cluster_id == true_cluster_id
- hit@k: true_cluster_id appears anywhere in top-k

Outputs:
- optional JSONL under dataset/test_logs/dec2vec/
- optional Markdown report for readability

Example:
  python scripts/dec2vec/evaluate_retrieval_raw_kb.py \
    --client maryangel101 \
    --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
    --topk 5 --clusters 50 --kb-examples-per-cluster 3 --eval-examples-per-cluster 2 \
    --seed 0 --save --save-md
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

# Ensure repo root is importable when running from scripts/
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from dec2vec.encoder import Dec2VecEncoder, Dec2VecEncoderConfig
from dec2vec.retrieval.text_retriever import Dec2VecTextRetriever, RetrievedText


def _extract_cluster_id_from_tag(tag: str) -> Optional[int]:
    # tag format: "<cluster_id>:<sample_index>"
    if not tag:
        return None
    head = tag.split(":", 1)[0]
    try:
        return int(head)
    except ValueError:
        return None


def _to_jsonable_matches(matches: List[RetrievedText], limit: int) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for m in matches[: max(0, int(limit))]:
        out.append(
            {
                "tag": m.tag,
                "cluster_id": _extract_cluster_id_from_tag(m.tag),
                "score": m.score,
                "text": m.text,
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
    lines.append(f"# dec2vec Retrieval Report (RAW KB): {jsonl_path.name}")
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
                text = str(m.get("text", ""))
                text = text if len(text) <= 140 else text[:140] + "..."
                lines.append(f"- score={score:.4f} tag={tag} cid={cid} text=`{text}`")
            lines.append("")

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(lines), encoding="utf-8")


def _iter_selected_clusters(
    clusters: Dict[str, Any],
    *,
    num_clusters: int,
) -> List[Tuple[int, Dict[str, Any]]]:
    cluster_ids = list(clusters.keys())
    if not cluster_ids:
        return []

    cluster_ids.sort(key=lambda cid: int(clusters[cid].get("count", 0)), reverse=True)
    cluster_ids = cluster_ids[: min(int(num_clusters), len(cluster_ids))]

    out: List[Tuple[int, Dict[str, Any]]] = []
    for cid in cluster_ids:
        try:
            out.append((int(cid), clusters[cid]))
        except ValueError:
            continue
    return out


def _split_kb_eval_examples(
    examples: List[str],
    *,
    rng: random.Random,
    kb_take: int,
    eval_take: int,
) -> Tuple[List[str], List[str]]:
    xs = [str(x).strip() for x in examples if str(x).strip()]
    if not xs:
        return [], []

    rng.shuffle(xs)

    kb = xs[: max(0, kb_take)]
    rest = xs[max(0, kb_take) :]
    if len(rest) >= eval_take:
        ev = rest[:eval_take]
    else:
        # Not enough; allow overlap by sampling from full list
        take = min(max(0, eval_take), len(xs))
        ev = rng.sample(xs, k=take) if len(xs) >= take else list(xs)
    return kb, ev


def main() -> int:
    ap = argparse.ArgumentParser(description="Evaluate dec2vec retrieval with RAW examples as KB")
    ap.add_argument("--client", default=None)
    ap.add_argument("--examples", default=None, help="Path to *_cluster_examples.json")

    ap.add_argument("--checkpoint", required=True, help="dec2vec checkpoint .npz")
    ap.add_argument("--topk", type=int, default=5)

    ap.add_argument("--clusters", type=int, default=50)
    ap.add_argument("--kb-examples-per-cluster", type=int, default=3)
    ap.add_argument("--eval-examples-per-cluster", type=int, default=2)
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--save", action="store_true")
    ap.add_argument("--save-md", action="store_true")
    ap.add_argument("--md-limit", type=int, default=200)

    ap.add_argument("--use-out", action="store_true")
    ap.add_argument("--no-normalize", action="store_true")

    args = ap.parse_args()

    if args.client:
        examples_path = Path("dataset/templates") / f"{args.client}_cluster_examples.json"
    else:
        if not args.examples:
            ap.error("Provide --client OR --examples")
        examples_path = Path(args.examples)

    if not examples_path.exists():
        raise FileNotFoundError(f"examples not found: {examples_path}")

    with examples_path.open("r", encoding="utf-8") as f:
        examples_data = json.load(f)
    clusters: Dict[str, Any] = examples_data.get("clusters", {})

    rng = random.Random(args.seed)

    # Build KB items and evaluation queries (try to keep them disjoint per cluster)
    kb_items: List[Tuple[str, str]] = []
    eval_queries: List[Tuple[int, str]] = []

    for cid, payload in _iter_selected_clusters(clusters, num_clusters=args.clusters):
        exs = payload.get("examples", [])
        if not isinstance(exs, list) or not exs:
            continue

        kb, ev = _split_kb_eval_examples(
            exs,
            rng=rng,
            kb_take=int(args.kb_examples_per_cluster),
            eval_take=int(args.eval_examples_per_cluster),
        )

        for i, line in enumerate(kb):
            kb_items.append((f"{cid}:{i}", line))
        for line in ev:
            eval_queries.append((cid, line))

    enc = Dec2VecEncoder(
        checkpoint_path=args.checkpoint,
        config=Dec2VecEncoderConfig(use_out=args.use_out, normalize=not args.no_normalize),
    )

    retriever = Dec2VecTextRetriever(encoder=enc)
    retriever.set_items(kb_items)
    retriever.build_index()

    total = 0
    hit1 = 0
    hitk = 0
    records: List[Dict[str, Any]] = []

    for true_cid, line in eval_queries:
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
                    "kb": {
                        "clusters": int(args.clusters),
                        "kb_examples_per_cluster": int(args.kb_examples_per_cluster),
                        "size": len(kb_items),
                    },
                    "checkpoint": args.checkpoint,
                    "source_examples": str(examples_path),
                }
            )

    print(f"examples:    {examples_path}")
    print(f"checkpoint:  {args.checkpoint}")
    print(f"kb_size:     {len(kb_items)} (clusters={args.clusters}, kb_per_cluster={args.kb_examples_per_cluster})")
    print(f"queries:     {total} (eval_per_cluster={args.eval_examples_per_cluster})")
    print(f"topk:        {args.topk}")
    print(f"hit@1:       {hit1}  acc@1={(hit1/total):.4f}" if total else "hit@1: 0")
    print(f"hit@k:       {hitk}  recall@k={(hitk/total):.4f}" if total else "hit@k: 0")

    if args.save:
        out_dir = Path("dataset/test_logs/dec2vec")
        out_dir.mkdir(parents=True, exist_ok=True)
        tag = args.client or examples_path.stem.replace("_cluster_examples", "")
        out_jsonl = out_dir / f"{tag}_dec2vec_retrieval_rawkb_seed{args.seed}.jsonl"
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
