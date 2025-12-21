"""Format JSONL test-log reports into readable Markdown or text.

Supports outputs produced by:
- evaluate_classification.py (classification_*.jsonl)
- robustness_test.py (robustness_*.jsonl)

Examples:
  python format_test_logs.py \
    --input dataset/test_logs/d2klab_robustness_mode-examples_seed0.jsonl \
    --output dataset/test_logs/d2klab_robustness_mode-examples_seed0.md \
    --format md --limit 200

  python format_test_logs.py \
    --input dataset/test_logs/d2klab_classification_raw_seed0.jsonl \
    --format text --limit 50
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


def _read_jsonl(path: Path) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def _summarize(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(records)
    no_match = sum(1 for r in records if r.get("predicted_cluster_id") == -1)
    correct = sum(1 for r in records if r.get("correct") is True)

    # If `correct` isn't present (evaluate_classification outputs), compute when possible.
    if correct == 0:
        computed = 0
        possible = 0
        for r in records:
            if "true_cluster_id" in r and "predicted_cluster_id" in r:
                possible += 1
                if r.get("true_cluster_id") == r.get("predicted_cluster_id"):
                    computed += 1
        if possible:
            correct = computed

    acc = (correct / total) if total else 0.0
    return {
        "total": total,
        "correct": correct,
        "no_match": no_match,
        "accuracy": acc,
    }


def _safe_str(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return str(value)


def _pick_log_fields(r: Dict[str, Any]) -> Tuple[str, str]:
    # robustness_test.py uses base_log/mutated_log; evaluate uses log
    base = _safe_str(r.get("base_log") or r.get("log") or "")
    mutated = _safe_str(r.get("mutated_log") or r.get("log") or "")
    return base, mutated


def _format_record_md(idx: int, r: Dict[str, Any]) -> str:
    true_cid = r.get("true_cluster_id")
    pred_cid = r.get("predicted_cluster_id")
    conf = r.get("confidence")
    correct = r.get("correct")

    base, mutated = _pick_log_fields(r)

    true_tmpl = _safe_str(r.get("true_template"))
    matched_tmpl = _safe_str(r.get("matched_template"))

    pred_examples = r.get("predicted_cluster_examples")
    if not isinstance(pred_examples, list):
        pred_examples = []

    lines: List[str] = []
    title_bits = [f"#{idx}"]
    if correct is True:
        title_bits.append("OK")
    elif correct is False:
        title_bits.append("WRONG")
    elif pred_cid == -1:
        title_bits.append("NO_MATCH")
    lines.append(f"### {' | '.join(title_bits)}")

    lines.append("")
    lines.append(f"- true_cluster_id: {true_cid}")
    lines.append(f"- predicted_cluster_id: {pred_cid}")
    if conf is not None:
        lines.append(f"- confidence: {conf}")

    if true_tmpl:
        lines.append(f"- true_template: `{true_tmpl}`")
    if matched_tmpl:
        lines.append(f"- matched_template: `{matched_tmpl}`")

    lines.append("")
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

    if pred_examples:
        lines.append("")
        lines.append("**predicted_cluster_examples (head)**")
        for ex in pred_examples:
            ex_s = _safe_str(ex)
            if not ex_s:
                continue
            lines.append(f"- `{ex_s}`")

    lines.append("")
    return "\n".join(lines)


def _format_record_text(idx: int, r: Dict[str, Any]) -> str:
    true_cid = r.get("true_cluster_id")
    pred_cid = r.get("predicted_cluster_id")
    conf = r.get("confidence")
    correct = r.get("correct")

    base, mutated = _pick_log_fields(r)
    true_tmpl = _safe_str(r.get("true_template"))
    matched_tmpl = _safe_str(r.get("matched_template"))

    pred_examples = r.get("predicted_cluster_examples")
    if not isinstance(pred_examples, list):
        pred_examples = []

    header = [f"[{idx}]", f"true={true_cid}", f"pred={pred_cid}"]
    if conf is not None:
        header.append(f"conf={conf}")
    if correct is True:
        header.append("OK")
    elif correct is False:
        header.append("WRONG")
    elif pred_cid == -1:
        header.append("NO_MATCH")

    out: List[str] = []
    out.append(" ".join(header))
    if true_tmpl:
        out.append(f"true_template: {true_tmpl}")
    if matched_tmpl:
        out.append(f"matched_template: {matched_tmpl}")

    if base and mutated and base != mutated:
        out.append("base_log:")
        out.append(base)
        out.append("mutated_log:")
        out.append(mutated)
    else:
        out.append("log:")
        out.append(mutated or base)

    if pred_examples:
        out.append("predicted_cluster_examples(head):")
        for ex in pred_examples:
            ex_s = _safe_str(ex)
            if ex_s:
                out.append(f"- {ex_s}")

    out.append("-" * 60)
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Format JSONL test logs into readable report")
    ap.add_argument("--input", required=True, help="Path to .jsonl file")
    ap.add_argument("--output", default=None, help="Output path (optional; prints to stdout if omitted)")
    ap.add_argument("--format", choices=["md", "text"], default="md")
    ap.add_argument("--limit", type=int, default=200, help="Max records to format")

    args = ap.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else None
    out_path = format_jsonl_file(
        input_path=input_path,
        output_path=output_path,
        fmt=args.format,
        limit=args.limit,
        quiet=False,
    )

    if out_path is None:
        return 0

    return 0


def format_jsonl_file(
    *,
    input_path: Path,
    output_path: Optional[Path] = None,
    fmt: str = "md",
    limit: int = 200,
    quiet: bool = True,
) -> Optional[Path]:
    """Format a JSONL report file and optionally write it to disk.

    Args:
        input_path: Path to the .jsonl file.
        output_path: Where to write formatted output. If None, prints to stdout.
        fmt: "md" or "text".
        limit: Max number of records.
        quiet: If False, prints a short 'wrote: ...' message when writing.

    Returns:
        The output path if written, else None.
    """
    records = _read_jsonl(input_path)

    n = max(0, int(limit))
    records = records[:n] if n else records

    summary = _summarize(records)

    chunks: List[str] = []
    if fmt == "md":
        chunks.append(f"# Test Log Report: {input_path.name}")
        chunks.append("")
        chunks.append(
            f"- total: {summary['total']}\n- correct: {summary['correct']}\n- no_match: {summary['no_match']}\n- accuracy: {summary['accuracy']:.4f}"
        )
        chunks.append("")
        for i, r in enumerate(records, 1):
            chunks.append(_format_record_md(i, r))
    else:
        chunks.append(f"Test Log Report: {input_path.name}")
        chunks.append(
            f"total={summary['total']} correct={summary['correct']} no_match={summary['no_match']} accuracy={summary['accuracy']:.4f}"
        )
        chunks.append("=" * 60)
        for i, r in enumerate(records, 1):
            chunks.append(_format_record_text(i, r))

    out_text = "\n".join(chunks).rstrip() + "\n"

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(out_text, encoding="utf-8")
        if not quiet:
            print(f"wrote: {output_path}")
        return output_path

    print(out_text)
    return None


if __name__ == "__main__":
    raise SystemExit(main())
