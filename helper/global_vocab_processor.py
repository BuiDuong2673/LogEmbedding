"""Extend the publish vocabulary with common words between all clients and assign indices to all words."""
import os
import re
import json
from collections import Counter


class GlobalVocabProcessor:
    """Establish global vocab for first word transfering before aggregation."""
    def __init__(self):
        """Initalize GlobalVocabProcess class."""
        self.client_list = ["d2klab", "logsage", "maryangel101"]

    def get_english_word_dict(self) -> dict:
        """Change the public english word dictionary dataset to dict."""
        english_word_dictionary_path = "dataset/english_word_dictionary.txt"
        vocab = {}
        with open(english_word_dictionary_path, 'r', encoding='utf-8') as f:
            for index, line in enumerate(f):
                word = line.strip()
                if word:
                    vocab[word] = index
        return vocab
    
    def get_all_client_files(self, client_name: str) -> dict:
        """Get all log file paths contains inside client dataset.
        
        Args:
            client_name (str): the name of the client who we want to get their words.
        """
        client_dataset = f"dataset/{client_name}"
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

    def get_client_words(self, client_name: str) -> list[str]:
        """Get all words of client.
        
        Args:
            client_name (str): the name of the client whose words we want to extract.
        """
        client_log_files = self.get_all_client_files(client_name=client_name)

        all_words = set()  # use a set to only add unique word

        for log_file in client_log_files:
            with open(log_file, "r", encoding="utf-8") as f:
                log_lines = f.readlines()

            for line in log_lines:
                # Split on spaces, underscores, hyphens
                parts = re.split(r'[\s_-]+', line)
                # Split camelCase
                for part in parts:
                    split_camel = re.findall(
                        r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])',
                        part
                    )
                    for word in split_camel:
                        # Lowercase the word and add it to the word collection.
                        all_words.add(word.lower())
        print(f"Client {client_name}, number of words {len(all_words)}")
        return list(all_words)
    
    def get_client_common_words(self, client_list: list[str]) -> list[str]:
        """Get the list of common words between at least two clients.
        
        Args:
            client_list (list[str]): the list of client names.
        """
        # Track the number of appearance of the word across different clients
        word_counter = Counter()
        for client in client_list:
            client_words = set(self.get_client_words(client_name=client))
            # Update the count of the words
            word_counter.update(client_words)

        # Keep words that appear in at least 2 clients
        common_words = [word for word, count in word_counter.items() if count >= 2]
        print(f"Number of common words between at least 2 clients {len(common_words)}")
        return common_words
    
    def create_global_vocab(self) -> dict:
        """Add common words into global vocab and assign index for each word."""
        # Get the public english word dataset
        initial_vocab = self.get_english_word_dict()
        # Get clients' common words
        common_words = self.get_client_common_words(client_list=self.client_list)
        # Track number of unknown common words
        num_unknown_words = 0
        # Analyze each client words
        for client in self.client_list:
            # Get client vocab
            client_words = self.get_client_words(client)
            # Check if each client word exist in initial vocab
            for word in client_words:
                if not initial_vocab.get(word):
                    # Check if the word is common word
                    if word in common_words:
                        num_unknown_words += 1
                        # If yes, add it to the vocab. If no, ignore.
                        word_index = int(list(initial_vocab.values())[-1]) + 1
                        initial_vocab[word] = word_index
        print(f"The number of unknown common words: {num_unknown_words}")
        # Save the vocab to a json file for later use
        save_path = "dataset/global_vocab.json"
        with open(save_path, "w", encoding="utf-8") as json_file:
            json.dump(initial_vocab, json_file, indent=4, ensure_ascii=False)
        print(f"Saved the global vocab to {save_path}")
        return initial_vocab
    
    def get_global_vocab(self) -> dict:
        """For other class to call to get global vocab."""
        global_vocab_path = "dataset/global_vocab.json"
        # If the global vocab has not been created, create it
        if not os.path.exists(global_vocab_path):
            global_vocab = self.create_global_vocab()
            return global_vocab
        # If the global vocab is already create, read that file
        with open(global_vocab_path, "r", encoding="utf-8") as json_file:
            global_vocab = json.load(json_file)
        return global_vocab


if __name__ == "__main__":
    global_vocab_processor = GlobalVocabProcessor()
    _ = global_vocab_processor.get_global_vocab()
