"""Vocabulary utilities for dec2vec.

We follow the repo's existing convention:
- A huge global vocabulary: dataset/global_vocab_index.json (word -> global_index)
- Each client only knows a subset of global indices
- Central server builds an *internal* vocab: dataset/internal_central_vocab.json
  mapping global_index -> internal_index (0..V-1)

dec2vec trains over internal_index space for efficiency.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

from helper.global_vocab_processor import GlobalVocabProcessor
from helper.vocab_extractor import VocabExtractor


_INTERNAL_VOCAB_PATH = "dataset/internal_central_vocab.json"


@dataclass(frozen=True)
class InternalVocab:
    global_to_internal: Dict[int, int]

    @property
    def size(self) -> int:
        return len(self.global_to_internal)


def load_internal_vocab(path: str = _INTERNAL_VOCAB_PATH) -> InternalVocab:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # json keys are strings
    global_to_internal = {int(k): int(v) for k, v in data.items()}
    return InternalVocab(global_to_internal=global_to_internal)


def build_internal_vocab(
    *,
    client_list: List[str],
    output_path: str = _INTERNAL_VOCAB_PATH,
) -> InternalVocab:
    """Build internal vocab by union of all clients' known global indices.

    This mirrors central_server_program.get_all_client_vocabs() but avoids importing it.
    """
    # Ensure global vocab exists
    _ = GlobalVocabProcessor().get_global_vocab()

    full_vocab: Dict[int, int] = {}
    reserved_index = 0

    for client in client_list:
        extractor = VocabExtractor(client_name=client)
        _, known_global_indices, _ = extractor.get_vocab()
        for global_idx in known_global_indices:
            if global_idx not in full_vocab:
                full_vocab[global_idx] = reserved_index
                reserved_index += 1

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({str(k): v for k, v in full_vocab.items()}, f, ensure_ascii=False, indent=2)

    return InternalVocab(global_to_internal=full_vocab)


def get_or_create_internal_vocab(
    *,
    client_list: List[str],
    path: str = _INTERNAL_VOCAB_PATH,
) -> InternalVocab:
    if os.path.exists(path):
        return load_internal_vocab(path)
    return build_internal_vocab(client_list=client_list, output_path=path)
