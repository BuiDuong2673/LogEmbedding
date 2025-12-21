"""dec2vec: Federated Word2Vec-style embeddings for logs.

This package implements a simple federated Skip-gram with Negative Sampling (SGNS)
trained across clients using FedAvg aggregation.

Design goals:
- Minimal dependencies (numpy only)
- Works with existing dataset/ layout
- Uses a fixed global vocab mapping (from dataset/internal_central_vocab.json)
"""
