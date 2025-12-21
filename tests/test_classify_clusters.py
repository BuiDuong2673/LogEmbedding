"""Minimal, deterministic tests for cluster classification.

These tests avoid sampling raw examples (which can be fuzzy), and instead ensure that
classifying the template text itself maps back to the same saved cluster_id.

Run:
  python tests/test_classify_clusters.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from helper.log_parser import LogParser


def _load_cluster_ids(templates_path: Path) -> list[int]:
    data = json.loads(templates_path.read_text(encoding="utf-8"))
    templates = data.get("templates", {})
    return [int(cid) for cid in templates.keys()]


def _test_templates_self_match(client: str, limit: int = 50) -> None:
    templates_path = Path("dataset/templates") / f"{client}_templates.json"
    assert templates_path.exists(), f"missing {templates_path}"

    lp = LogParser()
    lp.load_templates(str(templates_path))

    data = json.loads(templates_path.read_text(encoding="utf-8"))
    templates = data.get("templates", {})

    # Sort by highest count for stability, then take a small subset
    items = sorted(
        ((int(cid), payload) for cid, payload in templates.items()),
        key=lambda x: int(x[1].get("count", 0)),
        reverse=True,
    )[:limit]

    for cluster_id, payload in items:
        template_text = payload.get("template")
        assert isinstance(template_text, str) and template_text

        matched_template, _, _ = lp.match_log_to_template(template_text)
        assert (
            matched_template == template_text
        ), f"client={client} template mismatch for cluster_id={cluster_id}"


def main() -> int:
    _test_templates_self_match("maryangel101", limit=50)
    _test_templates_self_match("d2klab", limit=50)
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
