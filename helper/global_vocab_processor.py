"""Every actions with global vocabulary."""
from typing import Dict
import json
import os


class GlobalVocabProcessor:
    """Process global vocabulary."""
    def __init__(self):
        """Initialize the GlobalVocabProcessor."""
        self.global_vocab = {}
        self.original_vocab_file_path = "dataset/words_alpha.txt"

    def set_indices_for_global_vocab(self) -> Dict[str, int]:
        """Load vocabulary from a text file and return a mapping word -> index."""
        # Link to store the vocabulary
        out_path = "dataset/global_vocab_index_0.json"
        # Check if the vocab index already extracted
        if os.path.exists(out_path):
            try:
                with open(out_path, "r", encoding="utf-8") as json_file:
                    self.global_vocab = json.load(json_file)
                print(f"Loaded already extracted global vocab from {out_path}")
                return self.global_vocab
            except json.JSONDecodeError:
                self.global_vocab = {}
        # If not, create the vocab index from the text file
        print(f"Extracting global vocab from {self.original_vocab_file_path}...")
        vocab = {}
        with open(self.original_vocab_file_path, 'r', encoding='utf-8') as f:
            for index, line in enumerate(f):
                word = line.strip()
                if word:
                    vocab[word] = index
        self.global_vocab = vocab
        # Store the vocab indices in JSON format for later use
        with open(out_path, "w", encoding="utf-8") as json_file:
            json.dump(self.global_vocab, json_file, ensure_ascii=False, indent=4)
        return self.global_vocab

    def get_word_index(self, word: str) -> int:
        """Get the index of a word in the global vocabulary.

        Args:
            word (str): The word to look up.
        """
        return self.global_vocab.get(word, -1)  # Return -1 if word not found

    def add_common_words_to_global_vocab(self) -> None:
        """Add common words of all clients into the global vocabulary."""
        # Check if global_vocab_index.json exists
        if os.path.exists("dataset/global_vocab_index.json"):
            return
        # Get unknown word list of dk2lab
        dk2lab_unknown_word = []
        with open("dataset/d2klab_new_word_dict.json", "r", encoding="utf-8") as json_file:
            client_words_dict = json.load(json_file)
        for word in client_words_dict.keys():
            if self.global_vocab.get(word) is None:
                dk2lab_unknown_word.append(word)
        # Get unknown word list of maryangel101
        maryangel101_unknown_word = []
        with open("dataset/maryangel101_new_word_dict.json", "r", encoding="utf-8") as json_file:
            client_words_dict = json.load(json_file)
        for word in client_words_dict.keys():
            if self.global_vocab.get(word) is None:
                maryangel101_unknown_word.append(word.lower())
        # Find common unknown words between clients
        common_unknown_words = []
        for word in dk2lab_unknown_word:
            if word in maryangel101_unknown_word:
                common_unknown_words.append(word.lower())
        # Add common unknown words into dictionary
        for word in common_unknown_words:
            self.global_vocab[word] = len(self.global_vocab)
        # Store the updated vocab indices in JSON format for later use
        out_path = "dataset/global_vocab_index.json"
        with open(out_path, "w", encoding="utf-8") as json_file:
            json.dump(self.global_vocab, json_file, ensure_ascii=False, indent=4)
        print("Updated global vocab with common words. Stored in", out_path)

    def get_global_vocab(self) -> Dict[str, int]:
        """Get the global vocabulary."""
        self.set_indices_for_global_vocab()
        self.add_common_words_to_global_vocab()
        return self.global_vocab

if __name__ == "__main__":
    processor = GlobalVocabProcessor()
    processor.get_global_vocab()
