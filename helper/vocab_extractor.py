"""Extract words, and its context and negative samples from the dataset."""

import re
import os
import json
import random
from helper.global_vocab_processor import GlobalVocabProcessor

class VocabExtractor:
    """Extract initial word dictionary for client, with indices as global indices."""
    def __init__(self, client_name: str, which_train_set: str, num_context_words: int, num_negative_samples: int) -> None:
        """Initialize VocabExtractor class.
        
        Args:
            client_name (str): the name of the client.
            which_train_set (str): the name of the train_test set we want to use.
        """
        self.client_name = client_name
        self.which_train_set = which_train_set
        self.num_context_words = num_context_words
        self.num_negative_samples = num_negative_samples
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

    def collect_all_log_lines(self):
        """Get all log lines in all log files in client dataset
        and store mapping (log_line_index, file_path).
        """

        all_log_lines = {}
        # Get all the log file paths in client's dataset.
        file_paths = self.get_all_client_files()
        # Define timestamp pattern to be filtered from each log line
        timestamp_pattern = re.compile(
            r'\d{4}-\d{2}-\d{2}'                   # YYYY-MM-DD
            r'[T\s]'                               # T or space
            r'\d{2}:\d{2}:\d{2}'                   # HH:MM:SS
            r'(?:\.\d+)?'                          # optional .fractional seconds
            r'(?:Z|[+-]\d{2}:\d{2})?'              # optional timezone
            r'\s*'
        )
        # Map the log line with its file path
        temp_lines = []
        # Read each file to extract the log lines
        for file_path in file_paths:
            all_log_lines[file_path] = set()
            with open(file_path, "r", encoding="utf-8") as log_file:
                for line in log_file:
                    # Delete the timestamp
                    line = timestamp_pattern.sub('', line).strip('\n')
                    all_log_lines[file_path].add(line)

        return all_log_lines

    def create_word_dict(self, log_line_dict: dict) -> dict:
        """Store unique words, frequencies, their context words, and negative samples.

        Args:
            log_line_dict (dict): A dictionary mapping file paths to sets of log lines.
        """
        # Initialize the unique words dict
        word_dict = {}
        # Get all words into a set
        file_words = {}
        for file_path, log_lines in log_line_dict.items():
            file_words[file_path] = set()
            for line in log_lines:
                # Split on spaces, underscores, hyphens
                parts = re.split(r'[\s_-]+', line)
                # Split camelCase
                words = []
                for part in parts:
                    split_camel = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', part)
                    words.extend(split_camel)
                # Change words to lower cases
                words = [word.lower() for word in words]
                file_words[file_path].update(words)
                # Store the word into word_dict
                for i, word in enumerate(words):
                    # Only add unique words
                    if word_dict.get(word):
                        word_dict[word]["freq"] += 1
                    else:
                        # Initialize word
                        word_dict[word] = {"freq": 1, "context_words": set(), "negative_samples": set()}
                    # Add context words within num_context_words
                    start_idx = max(0, i - self.num_context_words)
                    end_idx = min(len(words), i + self.num_context_words + 1)
                    for j in range(start_idx, end_idx):
                        if j == i: # Skip adding central word.
                            continue
                        context_word = words[j].lower()
                        # Skip empty or special tokens
                        if not context_word.strip():
                            continue
                        word_dict[word]["context_words"].add(context_word)       
        # Get negative samples
        for file_path in log_line_dict.keys():
            other_files = [p for p in log_line_dict.keys() if p != file_path]
            if not other_files:
                continue
            neg_sample_file_path = random.choice(other_files)

            neg_candidates = list(file_words[neg_sample_file_path])
            k = min(self.num_negative_samples, len(neg_candidates))

            negative_samples = random.sample(neg_candidates, k)

            for word in file_words[file_path]:
                word_dict[word]["negative_samples"].update(negative_samples)

        # Sort the word_dict by frequency
        word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1]["freq"], reverse=True))
        return word_dict

    def create_word_dict_2(self, log_line_dict: dict) -> dict:
        """Store unique words, frequencies, their context words, and negative samples.

        Args:
            log_line_dict (dict): A dictionary mapping file paths to sets of log lines.
        """
        # Initialize the unique words dict
        word_dict = {}
        # Get all words into a set
        all_words = set()
        for file_path, log_lines in log_line_dict.items():
            # Words that won't be regared as negative samples
            non_negative_words = set()
            for line in log_lines:
                # Split on spaces, underscores, hyphens
                parts = re.split(r'[\s_-]+', line)
                # Split camelCase
                words = []
                for part in parts:
                    split_camel = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', part)
                    words.extend(split_camel)
                # Change words to lower cases
                words = [word.lower() for word in words]
                # Update all_words set
                all_words.update(words)
                # Update the non_negative_words
                non_negative_words.update(words)
                # Number of words in the line
                num_words = len(words)
                # Store the word into word_dict
                for i, word in enumerate(words):
                    word = word.lower()
                    # Only add unique words
                    if word_dict.get(word):
                        word_dict[word]["freq"] += 1
                    else:
                        # Initialize word
                        word_dict[word] = {"freq": 1, "context_words": [], "negative_samples": set()}
                    # Define word context words, nearer words appear first
                    context_words = []
                    for idx in range(1, num_words):
                        if i-idx >= 0:
                            potential_context_word = words[i-idx].lower()
                            if potential_context_word not in context_words:
                                context_words.append(potential_context_word)
                        if i+idx < num_words:
                            potential_context_word = words[i+idx].lower()
                            if potential_context_word not in context_words:
                                context_words.append(potential_context_word)
                    word_dict[word]["context_words"] = context_words
            # Get negative sample
            negative_samples = all_words - non_negative_words
            for word in non_negative_words:
                word_dict[word]["negative_samples"] = negative_samples
        # Sort the word_dict by frequency
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

    def change_negative_samples_to_indices(self, word_dict: dict) -> dict:
        """Change negative samples to indices in the word dictionary

        Args:
            word_dict (dict): The word dictionary
        Returns:
            dict: The word dictionary with negative samples as indices
        """
        for word, value in word_dict.items():
            negative_samples = value["negative_samples"]
            negative_indices = []
            for negative_word in negative_samples:
                negative_index = word_dict[negative_word]["index"]
                negative_indices.append(negative_index)
            word_dict[word]["negative_samples"] = negative_indices
        return word_dict

    def get_vocab(self) -> dict:
        """Get the vocabulary dictionary."""
        # Collect all unique log lines in client dataset.
        log_line_dict = self.collect_all_log_lines()
        print("Got all log lines")
        # Create client word dict
        word_dict = self.create_word_dict(log_line_dict=log_line_dict)
        print("Got client word dict")
        # Get global vocab maping global words to global indices
        global_vocab_processor = GlobalVocabProcessor()
        global_vocab = global_vocab_processor.get_global_vocab()
        # Add indice representation of the words
        word_dict, word_indices = self.add_word_global_index(global_vocab, word_dict)
        print("Added global word indices")
        # Change context words to indices
        word_dict = self.change_context_words_to_indices(word_dict)
        print("Changed context words to indices")
        # Change negative samples to indices
        word_dict = self.change_negative_samples_to_indices(word_dict)
        print("Changed negative samples to indices")
        print(f"Client {self.client_name}: num unknown words: {len(self.unknown_words)}")
        return word_dict, word_indices


if __name__ == "__main__":
    client_name = "client_1"
    which_train_set = "train_test_balanced"
    vocab_extractor = VocabExtractor(
        client_name=client_name, which_train_set=which_train_set, num_context_words=2, num_negative_samples=5)
    word_dict, word_indices = vocab_extractor.get_vocab()
    # Save word dict to a json file for checking
    with open(f"example_{client_name}_word_dict.json", "w", encoding="utf-8") as json_file:
        json.dump(word_dict, json_file, indent=4, ensure_ascii=False)
    print(f"Saved the word dict into file: example_{client_name}_word_dict.json")
    print(f"Word indices:\n{word_indices}")
