"""Dataset utilities for dec2vec (tokenization + training pairs).

We tokenize log lines similarly to helper/vocab_extractor.py:
- split on whitespace, underscores, hyphens
- split camelCase tokens

We map tokens -> global vocab index -> internal vocab index.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from helper.global_vocab_processor import GlobalVocabProcessor

from dec2vec.vocab import InternalVocab


_LEADING_TIMESTAMP_RES: List[re.Pattern[str]] = [
    # ISO-8601-ish (Drain masking compatible), anchored at start.
    # Examples:
    #   2023-09-21T17:21:43.5181300Z ...
    #   2023-09-21 17:21:43,123 ...
    re.compile(
        r"^\s*"
        r"\[?"  # optional leading [
        r"\d{4}-\d{2}-\d{2}"
        r"[T\s]"
        r"\d{2}:\d{2}:\d{2}"
        r"(?:[\.,]\d+)?"  # optional fractional seconds with . or ,
        r"(?:Z|[+-]\d{2}:\d{2})?"
        r"\]?"  # optional trailing ]
        r"(?:\s+|\s*[-|:]\s*)"  # separator
    ),
    # Date with slashes.
    #   2023/09/21 17:21:43 ...
    re.compile(
        r"^\s*"
        r"\[?"
        r"\d{4}/\d{2}/\d{2}"
        r"\s+"
        r"\d{2}:\d{2}:\d{2}"
        r"(?:[\.,]\d+)?"
        r"\]?"
        r"(?:\s+|\s*[-|:]\s*)"
    ),
    # Syslog style:
    #   Sep 21 17:21:43 ...
    re.compile(
        r"^\s*"
        r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
        r"\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}"
        r"(?:\s+|\s*[-|:]\s*)"
    ),
    # Time-only prefix:
    #   17:21:43 ...
    re.compile(
        r"^\s*"
        r"\d{2}:\d{2}:\d{2}"
        r"(?:[\.,]\d+)?"
        r"(?:\s+|\s*[-|:]\s*)"
    ),
]


def remove_timestamp(line: str) -> str:
    """Remove a leading timestamp / time axis from a log line.

    This is deliberately more conservative than a global substitution:
    it only strips timestamps at the beginning of the line.
    """
    s = str(line)
    # Some logs can have multiple leading time axes; strip repeatedly up to a small cap.
    for _ in range(3):
        before = s
        for rx in _LEADING_TIMESTAMP_RES:
            s = rx.sub("", s)
        if s == before:
            break
    return s


_CAMEL_RE = re.compile(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])")
_SPLIT_RE = re.compile(r"[\s_-]+")


def tokenize(line: str) -> List[str]:
    parts = _SPLIT_RE.split(line)
    tokens: List[str] = []
    for part in parts:
        if not part:
            continue
        tokens.extend(_CAMEL_RE.findall(part))
    return [t.lower() for t in tokens if t]


@dataclass
class ClientCorpus:
    token_ids: List[List[int]]  # list of sentences (token internal ids)
    freq: Dict[int, int]  # internal_id -> count


def build_client_corpus(
    *,
    log_lines: Sequence[str],
    internal_vocab: InternalVocab,
    max_lines: Optional[int] = None,
    min_tokens_per_line: int = 2,
) -> ClientCorpus:
    gvp = GlobalVocabProcessor()
    global_vocab = gvp.get_global_vocab()

    global_to_internal = internal_vocab.global_to_internal

    token_ids: List[List[int]] = []
    freq: Dict[int, int] = {}

    n = 0
    for raw in log_lines:
        if max_lines is not None and n >= max_lines:
            break
        n += 1

        line = remove_timestamp(str(raw).strip())
        if not line:
            continue

        words = tokenize(line)
        if len(words) < min_tokens_per_line:
            continue

        sent: List[int] = []
        for w in words:
            global_idx = global_vocab.get(w)
            if global_idx is None:
                continue
            internal_idx = global_to_internal.get(int(global_idx))
            if internal_idx is None:
                continue
            sent.append(int(internal_idx))

        if len(sent) < min_tokens_per_line:
            continue

        token_ids.append(sent)
        for wid in sent:
            freq[wid] = freq.get(wid, 0) + 1

    return ClientCorpus(token_ids=token_ids, freq=freq)


def iter_skipgram_pairs(
    token_ids: List[List[int]],
    *,
    window: int,
) -> Iterable[Tuple[int, int]]:
    for sent in token_ids:
        for i, center in enumerate(sent):
            start = max(0, i - window)
            end = min(len(sent), i + window + 1)
            for j in range(start, end):
                if j == i:
                    continue
                yield center, sent[j]
