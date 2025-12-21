"""Retrieve similar Drain templates using dec2vec embeddings.

This script does NOT replace the Doc2Vec embedder; it provides an alternative.

Example:
  python scripts/dec2vec/retrieve_templates.py \
    --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
    --client maryangel101 \
    --log "warning Resolution field is incompatible" \
    --topk 5
"""

from __future__ import annotations

import argparse
import os
import sys

# Ensure repo root is importable when running from scripts/
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from dec2vec.encoder import Dec2VecEncoder, Dec2VecEncoderConfig
from dec2vec.retrieval.template_retriever import Dec2VecTemplateRetriever


def main() -> int:
    ap = argparse.ArgumentParser(description="dec2vec template retrieval (cosine) ")
    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--client", required=True, help="Client name (templates under dataset/templates)")
    ap.add_argument("--template-dir", default="dataset/templates")
    ap.add_argument("--log", required=True, help="Query log line")
    ap.add_argument("--topk", type=int, default=5)

    ap.add_argument("--use-out", action="store_true", help="Use W_out word embeddings")
    ap.add_argument("--no-normalize", action="store_true", help="Disable L2 normalization of log vectors")
    ap.add_argument("--global-vocab", default="dataset/global_vocab_index.json")
    ap.add_argument("--internal-vocab", default="dataset/internal_central_vocab.json")

    args = ap.parse_args()

    enc = Dec2VecEncoder(
        checkpoint_path=args.checkpoint,
        global_vocab_path=args.global_vocab,
        internal_vocab_path=args.internal_vocab,
        config=Dec2VecEncoderConfig(use_out=args.use_out, normalize=not args.no_normalize),
    )

    retriever = Dec2VecTemplateRetriever(
        encoder=enc,
        template_dir=args.template_dir,
        client_name=args.client,
    )

    retriever.load_templates()
    retriever.build_index()

    results = retriever.retrieve(args.log, top_k=args.topk)

    print(f"Query: {args.log}")
    print(f"Client: {args.client}  topk={args.topk}")
    print("\nTop matches:")
    for i, r in enumerate(results, start=1):
        tmpl = r.template
        show = tmpl if len(tmpl) <= 120 else tmpl[:120] + "..."
        print(f"{i:>2}. score={r.score:.4f}  tag={r.tag}  template={show}")

    if not results:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
