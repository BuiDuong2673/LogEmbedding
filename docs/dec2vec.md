# dec2vec (Federated Word2Vec / SGNS)

## What is dec2vec?

`dec2vec` is a **federated-learning** variant of Word2Vec-style embeddings for this repo.

- Base algorithm: **Skip-gram with Negative Sampling (SGNS)**
- Federated strategy: **FedAvg** (weighted by number of skip-gram pairs)
- Training data: tokenized log lines from each client dataset
- Vocabulary: **fixed global/internal vocabulary** shared by all clients

In this repo we previously used **Doc2Vec** (see `models/log_embedder.py`).
Now we build **word embeddings** from scratch (Word2Vec-like) across clients.

## Vocabulary design (important)

This repo already has a global vocabulary file:
- `dataset/global_vocab_index.json` (word -> global_index)

Clients only know a subset. The central server builds an *internal* vocabulary:
- `dataset/internal_central_vocab.json` (global_index -> internal_index)

`dec2vec` trains over `internal_index` space to keep a compact embedding matrix.

## Folder structure

- `dec2vec/`
  - `data.py`: tokenize + generate skip-gram pairs
  - `model.py`: numpy SGNS updates (no PyTorch dependency)
  - `vocab.py`: build/load internal vocab
  - `io.py`: save/load `.npz` checkpoints
  - `federated/`
    - `client.py`: local SGNS training on a client
    - `aggregator.py`: FedAvg aggregation
- `scripts/dec2vec/`
  - `train_dec2vec.py`: runnable federated trainer (MVP)
  - `infer_dec2vec.py`: nearest-neighbor inspection
  - `embed_log_dec2vec.py`: log → vector embedding
  - `retrieve_templates.py`: similar template retrieval

## How training works

Each federated round:
1. Server broadcasts current global weights `(W_in, W_out)`
2. Each client:
   - loads its dataset `dataset/<client>/.../*.txt`
   - tokenizes each log line
   - builds skip-gram pairs within a window
   - trains local SGNS for `local_epochs`
3. Server aggregates client weights with **FedAvg**

We currently weight by `num_pairs` (the number of skip-gram pairs used by a client).

## Run (from scratch)

### 1) Train dec2vec

From repo root:

```bash
/home/zhaos/miniconda3/envs/nlp/bin/python scripts/dec2vec/train_dec2vec.py \
  --clients maryangel101 d2klab \
  --rounds 3 \
  --dim 64 \
  --window 2 \
  --negative-k 5 \
  --lr 0.03 \
  --local-epochs 1 \
  --max-lines 20000 \
  --max-pairs 200000
```

Outputs:
- `dec2vec/checkpoints/dec2vec_round1.npz` (+ `.json`)
- `dec2vec/checkpoints/dec2vec_round2.npz` ...

## Inspect / nearest neighbors

After training, you can query nearest neighbors for a token using:

```bash
/home/zhaos/miniconda3/envs/nlp/bin/python scripts/dec2vec/infer_dec2vec.py \
  --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
  --word error --topk 20
```

Notes:
- The word must exist in `dataset/global_vocab_index.json` and also be present in the current `dataset/internal_central_vocab.json`.
- By default it uses `W_in` (input embeddings). Use `--use-out` to query `W_out`.

## Log → vector (mean pooling)

`dec2vec` trains **word vectors**. To embed a full log line, we do:
- tokenize the log line
- map tokens to internal ids via the vocab files
- mean-pool the word vectors into a single fixed-size vector

CLI:

```bash
/home/zhaos/miniconda3/envs/nlp/bin/python scripts/dec2vec/embed_log_dec2vec.py \
  --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
  --log "warning Resolution field is incompatible"
```

Batch from a file (one log per line) to JSONL:

```bash
/home/zhaos/miniconda3/envs/nlp/bin/python scripts/dec2vec/embed_log_dec2vec.py \
  --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
  --input-file dataset/maryangel101/some_file.txt \
  --output dec2vec/checkpoints/maryangel101_vectors.jsonl
```

Or save a numpy matrix:

```bash
/home/zhaos/miniconda3/envs/nlp/bin/python scripts/dec2vec/embed_log_dec2vec.py \
  --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
  --input-file dataset/maryangel101/some_file.txt \
  --output dec2vec/checkpoints/maryangel101_vectors.npy
```

## Similar template retrieval (cosine)

Given a query log line, retrieve the most similar **Drain templates** for a client:

```bash
/home/zhaos/miniconda3/envs/nlp/bin/python scripts/dec2vec/retrieve_templates.py \
  --checkpoint dec2vec/checkpoints/dec2vec_round1.npz \
  --client maryangel101 \
  --log "warning Resolution field is incompatible" \
  --topk 5
```

### 2) (Optional) Rebuild internal vocab

If you want to force rebuilding `internal_central_vocab.json`:

```bash
/home/zhaos/miniconda3/envs/nlp/bin/python scripts/dec2vec/train_dec2vec.py --rebuild-internal-vocab
```

## Next steps (not implemented yet)

This MVP provides a working federated SGNS training loop.
Potential follow-ups:
- Add an inference script for nearest-neighbor queries
- Add socket-based server/client training (integrate with `central_server_program.py`)
- Add privacy mechanisms (DP, secure aggregation)
- Add subword modeling / OOV handling
