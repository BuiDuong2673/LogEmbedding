"""Train dec2vec (federated Word2Vec-style SGNS) from scratch.

Moved under scripts/dec2vec/ to keep repo root tidy.

Example:
  python scripts/dec2vec/train_dec2vec.py --clients maryangel101 d2klab --rounds 3 \
      --dim 64 --window 2 --negative-k 5 --lr 0.03 --local-epochs 1
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from typing import List

# Ensure repo root is importable when running from scripts/
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

from helper.vocab_extractor import VocabExtractor

from dec2vec.data import build_client_corpus
from dec2vec.federated.aggregator import ClientUpdate, fedavg
from dec2vec.federated.client import ClientTrainConfig, local_train
from dec2vec.io import save_checkpoint
from dec2vec.model import init_weights
from dec2vec.vocab import build_internal_vocab, get_or_create_internal_vocab


def main() -> int:
    ap = argparse.ArgumentParser(description="Federated dec2vec trainer (SGNS + FedAvg)")
    ap.add_argument("--clients", nargs="+", default=["maryangel101", "d2klab"], help="Client names")
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--dim", type=int, default=64)
    ap.add_argument("--window", type=int, default=2)
    ap.add_argument("--negative-k", type=int, default=5)
    ap.add_argument("--lr", type=float, default=0.03)
    ap.add_argument("--local-epochs", type=int, default=1)
    ap.add_argument("--max-lines", type=int, default=20000, help="Cap lines per client for speed")
    ap.add_argument("--max-pairs", type=int, default=200000, help="Cap skip-gram pairs per client")
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--rebuild-internal-vocab", action="store_true", help="Force rebuild internal vocab")
    ap.add_argument("--output-dir", default="dec2vec/checkpoints")

    args = ap.parse_args()

    clients: List[str] = list(args.clients)

    if args.rebuild_internal_vocab:
        internal_vocab = build_internal_vocab(client_list=clients)
    else:
        internal_vocab = get_or_create_internal_vocab(client_list=clients)

    print(f"Internal vocab size: {internal_vocab.size}")

    weights = init_weights(vocab_size=internal_vocab.size, dim=args.dim, seed=args.seed)

    for rnd in range(1, args.rounds + 1):
        t0 = time.time()
        updates: List[ClientUpdate] = []

        print(f"\n=== Round {rnd}/{args.rounds} ===")

        for i, client in enumerate(clients):
            print(f"Client: {client}")

            extractor = VocabExtractor(client_name=client)
            raw_lines = extractor.load_client_dataset()

            corpus = build_client_corpus(
                log_lines=raw_lines,
                internal_vocab=internal_vocab,
                max_lines=args.max_lines,
                min_tokens_per_line=2,
            )

            cfg = ClientTrainConfig(
                window=args.window,
                negative_k=args.negative_k,
                lr=args.lr,
                local_epochs=args.local_epochs,
                max_pairs=args.max_pairs,
                seed=args.seed + rnd * 100 + i,
            )

            local_w = init_weights(vocab_size=internal_vocab.size, dim=args.dim, seed=0)
            local_w.w_in[:] = weights.w_in
            local_w.w_out[:] = weights.w_out

            local_w, num_pairs = local_train(weights=local_w, corpus=corpus, config=cfg)
            print(f"  sentences={len(corpus.token_ids)} pairs={num_pairs} unique_words={len(corpus.freq)}")

            updates.append(ClientUpdate(weights=local_w, num_examples=num_pairs))

        weights = fedavg(updates)

        dt = time.time() - t0
        print(f"Round {rnd} done in {dt:.1f}s")

        meta = {
            "round": rnd,
            "clients": clients,
            "dim": args.dim,
            "window": args.window,
            "negative_k": args.negative_k,
            "lr": args.lr,
            "local_epochs": args.local_epochs,
            "max_lines": args.max_lines,
            "max_pairs": args.max_pairs,
            "seed": args.seed,
            "internal_vocab_size": internal_vocab.size,
        }
        save_checkpoint(output_dir=args.output_dir, weights=weights, meta=meta, name=f"dec2vec_round{rnd}")

    print(f"\n✓ Saved checkpoints to: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
