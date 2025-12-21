# LogEmbedding

## Layout

Key folders/files:

```text
dec2vec/                 dec2vec core library (federated SGNS)
dec2vec/checkpoints/     dec2vec checkpoints (.npz + .json)
docs/                    design docs (see docs/dec2vec.md)
scripts/dec2vec/         runnable dec2vec utilities (train/infer/embed/retrieve)
helper/                  parsing + vocab helpers
models/                  existing Doc2Vec embedder (unchanged)
```

## Dataset
This file shows the sources of `dataset/` folder.

### maryangel101: ci-cd-failure-detector

Link: https://github.com/maryangel101/ci-cd-failure-detector/tree/main

```python
"dataset/maryangel101/"
```

### D2KLab: gha-dataset
Link: https://github.com/D2KLab/gha-dataset/tree/master

```python
"dataset/d2klab"
```

### dwyl: english-words
Link: https://github.com/dwyl/english-words

```python
"dataset/words_alpha.txt"
```

## Execution
```python
python central_server_program.py
```

## dec2vec

See `docs/dec2vec.md`. Quick start:

```bash
/home/zhaos/miniconda3/envs/nlp/bin/python scripts/dec2vec/train_dec2vec.py --clients maryangel101 d2klab --rounds 1
```