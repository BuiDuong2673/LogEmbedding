"""Dec2Vec-based similarity retrieval over Drain templates.

This does NOT replace the existing Doc2Vec embedder.
It provides an alternative retrieval path:
- embed templates via Dec2VecEncoder (mean pooled word vectors)
- embed query log line
- cosine similarity to return top-k templates

Input templates file format matches dataset/templates/*_templates.json:
{
  "client": "...",
  "templates": {
    "<cluster_id>": {"template": "...", "count": 123, ...},
    ...
  }
}

It also supports *_pass_templates.json and *_fail_templates.json.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np

from dec2vec.encoder import Dec2VecEncoder


@dataclass(frozen=True)
class RetrievedTemplate:
    template: str
    score: float
    tag: str


def _l2_normalize_rows(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    norms = np.maximum(norms, eps)
    return x / norms


class Dec2VecTemplateRetriever:
    def __init__(
        self,
        *,
        encoder: Dec2VecEncoder,
        template_dir: str = "dataset/templates",
        client_name: str,
    ) -> None:
        self.encoder = encoder
        self.template_dir = template_dir
        self.client_name = client_name

        self._templates: Dict[str, str] = {}  # tag -> template
        self._matrix: Optional[np.ndarray] = None  # [N, D]
        self._tags: List[str] = []

    @property
    def dim(self) -> int:
        return self.encoder.dim

    def _load_templates_file(self, path: str, *, label: Optional[str]) -> None:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        templates = data.get("templates", {})

        for cluster_id, info in templates.items():
            tmpl = info.get("template")
            if not tmpl:
                continue
            if label:
                tag = f"{label}_{cluster_id}"
            else:
                tag = str(cluster_id)
            self._templates[tag] = str(tmpl)

    def load_templates(self) -> int:
        """Load templates for client_name from template_dir.

        Priority:
        - if pass/fail files exist, load both
        - else load single <client>_templates.json
        """
        base = self.template_dir
        client = self.client_name

        pass_path = os.path.join(base, f"{client}_pass_templates.json")
        fail_path = os.path.join(base, f"{client}_fail_templates.json")
        single_path = os.path.join(base, f"{client}_templates.json")

        self._templates = {}

        loaded_any = False
        if os.path.exists(pass_path):
            self._load_templates_file(pass_path, label="pass")
            loaded_any = True
        if os.path.exists(fail_path):
            self._load_templates_file(fail_path, label="fail")
            loaded_any = True

        if not loaded_any:
            if not os.path.exists(single_path):
                raise FileNotFoundError(f"No template files found for client={client} under {base}")
            self._load_templates_file(single_path, label=None)

        return len(self._templates)

    def build_index(self) -> None:
        if not self._templates:
            self.load_templates()

        tags = list(self._templates.keys())
        mat = np.zeros((len(tags), self.dim), dtype=np.float32)

        for i, tag in enumerate(tags):
            mat[i] = self.encoder.embed_log_line(self._templates[tag], strip_timestamp=True)

        # Pre-normalize for fast cosine
        mat = _l2_normalize_rows(mat)

        self._tags = tags
        self._matrix = mat

    def retrieve(self, query_log: str, top_k: int = 5) -> List[RetrievedTemplate]:
        if self._matrix is None:
            self.build_index()

        assert self._matrix is not None

        q = self.encoder.embed_log_line(query_log, strip_timestamp=True).astype(np.float32, copy=False)
        qn = float(np.linalg.norm(q))
        if qn <= 1e-12:
            return []
        q = q / qn

        sims = self._matrix @ q

        top_k = max(1, int(top_k))
        top_k = min(top_k, sims.shape[0])

        idx = np.argpartition(-sims, kth=top_k - 1)[:top_k]
        idx = idx[np.argsort(-sims[idx])]

        out: List[RetrievedTemplate] = []
        for i in idx:
            tag = self._tags[int(i)]
            out.append(
                RetrievedTemplate(
                    template=self._templates[tag],
                    score=float(sims[int(i)]),
                    tag=tag,
                )
            )
        return out
