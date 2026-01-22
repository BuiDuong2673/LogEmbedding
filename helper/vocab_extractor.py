"""Extract vocabulary from the dataset."""
import os
import re
import json

from helper.global_vocab_processor import GlobalVocabProcessor
from helper.create_training_dataset import TrainingDatasetCreator


NUM_CONTEXT_WORDS = 2
CLIENT_LIST = ["d2klab", "maryangel101"]


class VocabExtractor:
    def __init__(self, client_name: str) -> None:
        """Initialize the VocabExtractor with a client name.

        Args:
            client_name (str): The name of the client.
        """
        self.client_name = client_name
        self.global_vocab_processor = GlobalVocabProcessor()
        # Extract the vocab indices if not extracted yet
        self.global_vocab = self.global_vocab_processor.get_global_vocab()
        # Initialize unknown words variable
        self.unknown_words = []
    
    def read_dataset_file(self, file_path: str) -> list:
        """Read a dataset file and return its lines.
        
        Args:
            file_path (str): The path to the dataset file. Should be .txt.
        """
        # Check if file exists
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            return []
        # If exists, read the file
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
            return lines
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return []

    def load_client_dataset(self) -> None:
        """Load the dataset for the specified client, maryangel101."""
        # Collect list of training log files
        training_paths = TrainingDatasetCreator().get_file_list_from_folder(os.path.join("dataset", "training", self.client_name))
        # Combine all log lines into a list
        all_lines = []
        for file_path in training_paths:
            lines = self.read_dataset_file(file_path)
            if lines:  # Only add if lines are not empty
                all_lines.extend(lines)
        return all_lines

    def create_word_dict(self, log_lines: list, num_context_words: int=NUM_CONTEXT_WORDS) -> dict:
        """Store unique words, their neighbors within num_context_words, and frequency

        Args:
            log_lines (list): The list of log lines
            num_context_words (int): The number of context words to consider
        Returns:
            dict: The word dictionary
        """
        # Initialize the unique words dict
        word_dict = {}
        for line in log_lines:
            # Split on spaces, underscores, hyphens
            parts = re.split(r'[\s_-]+', line)
            # Split camelCase
            words = []
            for part in parts:
                split_camel = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', part)
                words.extend(split_camel)
            # Store the word into the word_dict
            for i, word in enumerate(words):
                # Only add unique words
                if word_dict.get(word):
                    word_dict[word]["freq"] += 1
                else:
                    # Initialize word
                    word_dict[word] = {"freq": 1, "context_words": set()}
                # Add context words within num_context_words
                start_idx = max(0, i - num_context_words)
                end_idx = min(len(words), i + num_context_words + 1)
                for j in range(start_idx, end_idx):
                    if j == i:
                        continue
                    context_word = words[j]
                    # Optional: skip empty or special tokens
                    if not context_word.strip():
                        continue
                    # Use a set to avoid excessive growth
                    word_dict[word]["context_words"].add(context_word)
        # Sort word_dict
        word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1]["freq"], reverse=True))
        return word_dict
    
    def add_word_global_index(self, word_dict: dict) -> dict:
        """Add global word index to each word in the word dictionary

        Args:
            word_dict (dict): The word dictionary
        Returns:
            dict: The word dictionary with global word index
            list: The list of known words' indices
            list: The list of unknown words
        """
        unknown_num = 0
        unknown_words = []
        unknown_words_indices = []
        known_words_indices = []
        for word in word_dict.keys():
            word_index = self.global_vocab.get(word.lower(), -1)
            if word_index == -1:  # if word not found
                word_dict[word]["index"] = f"unk_{unknown_num}"
                # Store unknown words
                unknown_words.append(word)
                unknown_words_indices.append(f"unk_{unknown_num}")
                unknown_num += 1
            else:
                word_dict[word]["index"] = f"{word_index}"
                known_words_indices.append(f"{word_index}")
        # Join the known words and unknown words indices lists
        words_indices = known_words_indices + unknown_words_indices
        # Store unknown words (for analysis)
        self.unknown_words = unknown_words
        return word_dict, words_indices

    def change_context_words_to_indices(self, word_dict: dict) -> dict:
        """Change context words to indices in the word dictionary

        Args:
            word_dict (dict): The word dictionary
        Returns:
            dict: The word dictionary with context words as indices
        """
        for word, value in word_dict.items():
            context_words = value["context_words"]
            context_indices = []
            for context_word in context_words:
                context_index = word_dict[context_word]["index"]
                context_indices.append(context_index)
            word_dict[word]["context_words"] = context_indices
        return word_dict
    
    def get_vocab(self, num_context_words: int=NUM_CONTEXT_WORDS) -> tuple[dict, list]:
        """Run the Word2Vec embedding process

        Args:
            num_context_words (int): The number of context words to consider.

        Returns:
            dict: The word dictionary with context words as indices
            list: The list of known words' indices
            list: The list of unknown words
        """
        data = self.load_client_dataset()
        # Create word dictionary
        word_dict = self.create_word_dict(data, num_context_words)
        # Add index to each word
        word_dict, words_indices = self.add_word_global_index(word_dict)
        # Change context words to indices
        word_dict = self.change_context_words_to_indices(word_dict)
        return word_dict, words_indices


if __name__ == "__main__":
    extractor = VocabExtractor(client_name="maryangel101")
    vocab_dict, words_indices = extractor.get_vocab()
    # Temporary store the vocab in a json file
    with open("vocab.json", "w") as f:
        json.dump(vocab_dict, f)
    # Visualize the known, unknown words info
    known_count = 0
    unknown_count = 0
    for index in words_indices:
        if index.startswith("unk_"):
            unknown_count += 1
        else:
            known_count += 1
    print(f"Num known words: {known_count}")
    print(f"Num unknown words: {unknown_count}")

    print(f"First 10 unknown words: {extractor.unknown_words[:10]}")
