"""Extract the word dictionary for client."""
import re
import os
import json
from helper.global_vocab_processor import GlobalVocabProcessor


NUM_CONTEXT_WORDS = 2


class VocabExtractor:
    """Extract initial word dictionary for client, with indices as global indices."""
    def __init__(self, client_name: str, which_train_set: str) -> None:
        """Initialize VocabExtractor class.
        
        Args:
            client_name (str): the name of the client.
            which_train_set (str): the name of the train_test set we want to use.
        """
        self.client_name = client_name
        self.which_train_set = which_train_set
        # Initialize unknown words variable
        self.unknown_words = []
    
    def get_all_client_files(self) -> dict:
        """Get all log file paths contains inside client dataset."""
        client_dataset = f"dataset/{self.which_train_set}/{self.client_name}/train"
        # Read all log file in the client_dataset folder
        dataset_paths = []  # Collect all folders inside client's overall dataset folder
        for subdir in os.listdir(client_dataset):
            full_path = os.path.join(client_dataset, subdir)
            if os.path.isdir(full_path):
                dataset_paths.append(full_path)
        file_path_list = []  # Collect all file paths in client_dataset folder
        for dataset_path in dataset_paths:
            for filename in os.listdir(dataset_path):
                file_path = os.path.join(dataset_path, filename)
                file_path_list.append(file_path)
        return file_path_list
    
    def collect_all_log_lines(self) -> None:
        """Get all log lines in all log files in client dataset."""
        all_log_lines = set()
        # Get all the log file paths in client's dataset.
        file_paths = self.get_all_client_files()
        # Read each file to extract the log lines
        for file_path in file_paths:
            with open(file_path, "r", encoding="utf-8") as log_file:
                for line in log_file:
                    # Delete timestampt
                    timestamp_pattern = re.compile(
                        r'\d{4}-\d{2}-\d{2}'                   # YYYY-MM-DD
                        r'[T\s]'                               # T or space
                        r'\d{2}:\d{2}:\d{2}'                   # HH:MM:SS
                        r'(?:\.\d+)?'                          # optional .fractional seconds
                        r'(?:Z|[+-]\d{2}:\d{2})?'              # optional timezone (Z or +hh:mm)
                        r'\s*'                                 # trailing spaces
                    )
                    line = timestamp_pattern.sub('', line).strip('\n')
                    all_log_lines.add(line)
        return list(all_log_lines)
    
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
                word = word.lower()
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
                    if j == i: # Skip adding central word.
                        continue
                    context_word = words[j].lower()
                    # Skip empty or special tokens
                    if not context_word.strip():
                        continue
                    # Use a set to avoid excessive growth
                    word_dict[word]["context_words"].add(context_word)
        # Sort word_dict
        word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1]["freq"], reverse=True))
        return word_dict
    
    def add_word_global_index(self, global_vocab_dict: dict, client_word_dict: dict) -> dict:
        """Add global index to each word in the word dictionary.

        Args:
            global_vocab_dict (dict): the dictionary maping global words to global indices.
            client_word_dict (dict): The client word dictionary with the word as the key.
        Returns:
            new word_dict (dict): The word dictionary with global word index.
            word_indices (list): The list of indices of words, only this will be shared with central server.
        """
        unknown_num = 0
        unknown_words = []
        unknown_words_indices = []
        known_words_indices = []
        for word in client_word_dict.keys():
            word_index = global_vocab_dict.get(word.lower(), -1)
            if word_index == -1:  # if word not found in global dictionaryc
                client_word_dict[word]["index"] = f"unk_{unknown_num}"
                # Store unknown words
                unknown_words.append(word)
                unknown_words_indices.append(f"unk_{unknown_num}")
                unknown_num += 1
            else:  # if word found in global dictionary
                client_word_dict[word]["index"] = f"{word_index}"
                known_words_indices.append(f"{word_index}")
        # Join the known words and unknown words indices lists
        words_indices = known_words_indices + unknown_words_indices
        # Store unknown words (for analysis)
        self.unknown_words = unknown_words
        return client_word_dict, words_indices
    
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
    
    def get_vocab(self, num_context_words: int=NUM_CONTEXT_WORDS):
        """Run the Word2Vec embedding process."""
        # Collect all unique log lines in client dataset.
        log_lines = self.collect_all_log_lines()
        # Create client word dict
        word_dict = self.create_word_dict(log_lines=log_lines, num_context_words=num_context_words)
        # Get global vocab maping global words to global indices
        global_vocab_processor = GlobalVocabProcessor()
        global_vocab = global_vocab_processor.get_global_vocab()
        # Add indice representation of the words
        word_dict, word_indices = self.add_word_global_index(global_vocab, word_dict)
        # Change context words to indices
        word_dict = self.change_context_words_to_indices(word_dict)
        print(f"Client {self.client_name}: num unknown words: {len(self.unknown_words)}")
        return word_dict, word_indices


if __name__ == "__main__":
    client_name = "d2klab"
    which_train_set = "train_test_internal"
    vocab_extractor = VocabExtractor(client_name=client_name, which_train_set=which_train_set)
    word_dict, word_indices = vocab_extractor.get_vocab(num_context_words=NUM_CONTEXT_WORDS)
    # Save word dict to a json file for checking
    with open(f"dataset/{client_name}_word_dict.json", "w", encoding="utf-8") as json_file:
        json.dump(word_dict, json_file, indent=4, ensure_ascii=False)
    print(f"Saved the word dict into file: dataset/{client_name}_word_dict.json")
    print(f"Word indices:\n{word_indices}")