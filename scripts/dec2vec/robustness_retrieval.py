"""Mutate cluster examples and test dec2vec retrieval robustness.

This mirrors robustness_test.py, but evaluates **dec2vec cosine retrieval over templates**.

Ground truth: from *_cluster_examples.json (true_cluster_id)
Prediction: retrieve top-k templates; a test is correct if true_cluster_id appears in top-k.

Outputs:
- JSONL under dataset/test_logs/dec2vec/
- optional Markdown report for readability

Example:
  python scripts/dec2vec/robustness_retrieval.py \
    --client maryangel101 \
    --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
    --topk 5 \
    --clusters 50 --base-examples-per-cluster 1 --mutations-per-example 3 \
    --mutation-steps 2 --seed 0 --save --save-md
"""

from __future__ import annotations

import argparse
import json
import random
import re
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

# Ensure repo root is importable when running from scripts/
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from dec2vec.encoder import Dec2VecEncoder, Dec2VecEncoderConfig
from dec2vec.retrieval.template_retriever import Dec2VecTemplateRetriever, RetrievedTemplate


_VERSION_RE = re.compile(r"\b(?:v)?\d+\.\d+(?:\.\d+)*\b")
_IP_RE = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")
_UUID_RE = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b")
_HEX_RE = re.compile(r"\b[0-9a-fA-F]{16,64}\b")
_DIGITS_RE = re.compile(r"\d+")
_PATH_RE = re.compile(r"(?:/[^\s]+)+")


def _extract_cluster_id_from_tag(tag: str) -> Optional[int]:
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
    for _ in range(max(1, steps)):
        mut = rng.choice(_MUTATORS)
        out2 = mut(out, rng)
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
    lines.append(f"# dec2vec Robustness Report: {jsonl_path.name}")
    lines.append("")
    lines.append(f"- total: {total}")
    lines.append(f"- hit@1: {hit1} ({(hit1/total):.4f})" if total else "- hit@1: 0")
    lines.append(f"- hit@k: {hitk} ({(hitk/total):.4f})" if total else "- hit@k: 0")
    lines.append("")

    for i, r in enumerate(records, 1):
        title_bits = [f"#{i}"]
        if r.get("hit_at_1") is True:
            title_bits.append("TOP1_OK")
        elif r.get("hit_at_k") is True:
            title_bits.append("TOPK_OK")
        else:
            title_bits.append("MISS")
        lines.append(f"## {' | '.join(title_bits)}")
        lines.append("")
        lines.append(f"- true_cluster_id: {r.get('true_cluster_id')}")
        lines.append(f"- predicted_cluster_id: {r.get('predicted_cluster_id')}")
        lines.append(f"- topk: {r.get('topk')}")
        lines.append("")

        base = str(r.get("base_log", ""))
        mutated = str(r.get("mutated_log", ""))

        if base and mutated and base != mutated:
            lines.append("**base_log**")
            lines.append("```")
            lines.append(base)
            lines.append("```")
            lines.append("")
            lines.append("**mutated_log**")
            lines.append("```")
            lines.append(mutated)
            lines.append("```")
        else:
            lines.append("**log**")
            lines.append("```")
            lines.append(mutated or base)
            lines.append("```")

        matches = r.get("top_matches")
        if isinstance(matches, list) and matches:
            lines.append("")
            lines.append("**top_matches**")
            for m in matches:
                tag = m.get("tag")
                cid = m.get("cluster_id")
                score = m.get("score")
                tmpl = str(m.get("template", ""))
                tmpl = tmpl if len(tmpl) <= 140 else tmpl[:140] + "..."
                lines.append(f"- score={score:.4f} tag={tag} cid={cid} tmpl=`{tmpl}`")

        pred_examples = r.get("predicted_cluster_examples")
        if isinstance(pred_examples, list) and pred_examples:
            lines.append("")
            lines.append("**predicted_cluster_examples (head)**")
            for ex in pred_examples:
                exs = str(ex).strip()
                if exs:
                    lines.append(f"- `{exs}`")

        lines.append("")

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Mutate cluster examples and test dec2vec retrieval robustness")
    ap.add_argument("--client", default=None)
    ap.add_argument("--templates", default=None)
    ap.add_argument("--examples", default=None)

    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--topk", type=int, default=5)

    ap.add_argument("--clusters", type=int, default=20)
    ap.add_argument("--base-examples-per-cluster", type=int, default=1)
    ap.add_argument("--mutations-per-example", type=int, default=3)
    ap.add_argument("--mutation-steps", type=int, default=2)

    ap.add_argument("--show-examples", type=int, default=3)
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--save", action="store_true")
    ap.add_argument("--save-md", action="store_true")
    ap.add_argument("--md-limit", type=int, default=200)
    ap.add_argument("--md-output", default=None)

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

    with examples_path.open("r", encoding="utf-8") as f:
        examples_data = json.load(f)
    clusters: Dict[str, Any] = examples_data.get("clusters", {})

    enc = Dec2VecEncoder(
        checkpoint_path=args.checkpoint,
        config=Dec2VecEncoderConfig(use_out=args.use_out, normalize=not args.no_normalize),
    )

    client_name = args.client or templates_path.stem.replace("_templates", "")
    retriever = Dec2VecTemplateRetriever(encoder=enc, template_dir=str(templates_path.parent), client_name=client_name)
    retriever.load_templates()
    retriever.build_index()

    rng = random.Random(args.seed)

    records: List[Dict[str, Any]] = []

    total = 0
    hit1 = 0
    hitk = 0

    for true_cid, base_log in iter_base_examples(
        clusters,
        rng=rng,
        num_clusters=args.clusters,
        base_examples_per_cluster=args.base_examples_per_cluster,
    ):
        for _ in range(max(1, int(args.mutations_per_example))):
            mutated = mutate_log(base_log, rng, steps=args.mutation_steps)

            matches = retriever.retrieve(mutated, top_k=args.topk)
            match_cids = [c for c in (_extract_cluster_id_from_tag(m.tag) for m in matches) if c is not None]

            predicted_cluster_id = match_cids[0] if match_cids else None

            is_hit1 = bool(match_cids) and match_cids[0] == true_cid
            is_hitk = true_cid in match_cids

            total += 1
            hit1 += 1 if is_hit1 else 0
            hitk += 1 if is_hitk else 0

            if args.save:
                pred_examples: List[str] = []
                if predicted_cluster_id is not None:
                    payload = clusters.get(str(predicted_cluster_id), {})
                    exs = payload.get("examples", [])
                    if isinstance(exs, list):
                        pred_examples = [str(x).strip() for x in exs[: max(0, int(args.show_examples))] if str(x).strip()]

                records.append(
                    {
                        "true_cluster_id": true_cid,
                        "predicted_cluster_id": predicted_cluster_id,
                        "hit_at_1": is_hit1,
                        "hit_at_k": is_hitk,
                        "topk": args.topk,
                        "base_log": base_log,
                        "mutated_log": mutated,
                        "mutation_steps": args.mutation_steps,
                        "top_matches": _to_jsonable_matches(matches, limit=args.topk),
                        "predicted_cluster_examples": pred_examples,
                        "source_templates": str(templates_path),
                        "source_examples": str(examples_path),
                        "checkpoint": args.checkpoint,
                    }
                )

    print(f"templates:   {templates_path}")
    print(f"examples:    {examples_path}")
    print(f"checkpoint:  {args.checkpoint}")
    print(f"topk:        {args.topk}")
    print(f"mutations:   clusters={args.clusters} base_per_cluster={args.base_examples_per_cluster} per_base={args.mutations_per_example}")
    print(f"total:       {total}")
    print(f"hit@1:       {hit1}  acc@1={(hit1/total):.4f}" if total else "hit@1: 0")
    print(f"hit@k:       {hitk}  recall@k={(hitk/total):.4f}" if total else "hit@k: 0")

    if args.save:
        out_dir = Path("dataset/test_logs/dec2vec")
        out_dir.mkdir(parents=True, exist_ok=True)
        tag = client_name
        out_jsonl = out_dir / f"{tag}_dec2vec_robustness_seed{args.seed}.jsonl"
        with out_jsonl.open("w", encoding="utf-8") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"saved:       {out_jsonl}")

        if args.save_md:
            out_md = Path(args.md_output) if args.md_output else out_jsonl.with_suffix(".md")
            _write_md_report(out_jsonl, out_md, limit=args.md_limit)
            print(f"saved(md):   {out_md}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
