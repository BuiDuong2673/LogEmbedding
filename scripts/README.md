# Scripts

This folder contains runnable utilities grouped by topic.

## dec2vec

- `dec2vec/train_dec2vec.py`: federated training (SGNS + FedAvg)
- `dec2vec/infer_dec2vec.py`: sanity inference on a checkpoint
- `dec2vec/embed_log_dec2vec.py`: embed a single log line
- `dec2vec/near_duplicate.py`: compare two log lines by cosine similarity (no KB)
- `dec2vec/retrieve_logs.py`: query log → top-k similar log lines from a corpus file
- `dec2vec/build_corpus.py`: build a corpus file (one log per line) from dataset directories
- `dec2vec/evaluate_near_duplicate.py`: evaluate near-duplicate detection (no clusters; base vs mutated)
- `dec2vec/retrieve_templates.py`: retrieve nearest templates by cosine similarity
- `dec2vec/evaluate_retrieval.py`: evaluate template retrieval using cluster examples (hit@k)
- `dec2vec/robustness_retrieval.py`: mutate cluster examples and test retrieval robustness
- `dec2vec/evaluate_retrieval_raw_kb.py`: evaluate retrieval when KB is raw cluster examples (no templateization)
- `dec2vec/robustness_retrieval_raw_kb.py`: robustness test when KB is raw cluster examples (no templateization)

## drain

This repo already has Drain-related scripts at repo root.
This folder is reserved for future wrappers without breaking existing entrypoints.

# test code

cd /home/zhaos/projects/decentralized/LogEmbedding && /home/zhaos/miniconda3/envs/nlp/bin/python scripts/dec2vec/retrieve_logs.py --checkpoint dec2vec/checkpoints/dec2vec_round1.npz --corpus-file dataset/corpus/d2klab_logs.txt --log "2023-09-21T17:21:33.6471522Z Requested labels: ubuntu-latest" --topk 3 --strip-timestamp --show-text 140