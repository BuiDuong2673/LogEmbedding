"""Extract vocabulary from the dataset."""
import os
import re
import json

from helper.global_vocab_processor import GlobalVocabProcessor


class VocabExtractor:
    def __init__(self, client_name: str) -> None:
        """Initialize the VocabExtractor with a client name.
        
        Args:
            client_name (str): The name of the client.
        """
        self.client_name = client_name
        self.global_vocab_processor = GlobalVocabProcessor()
        # Extract the vocab indices if not extracted yet
        _ = self.global_vocab_processor.get_global_vocab()
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
        # Implementation to load dataset
        # Read all file in the dataset folder
        all_lines = []
        client_dataset_path = os.path.join("dataset", self.client_name)
        dataset_paths = []
        for subdir in os.listdir(client_dataset_path):
            full_path = os.path.join(client_dataset_path, subdir)

            if os.path.isdir(full_path):
                dataset_paths.append(full_path)

        for dataset_path in dataset_paths:
            for filename in os.listdir(dataset_path):
                file_path = os.path.join(dataset_path, filename)
                lines = self.read_dataset_file(file_path)
                if lines:  # Only add if lines are not empty
                    all_lines.extend(lines)
        return all_lines        
    
    def delete_time_stamp(self, log_lines: list) -> list:
        """Delete the time stamp from each log line.
        Args:
            log_lines (list): The list of log lines.
        Returns:
            list: The list of log lines without the time stamp.
        """
        # Initialize new list
        new_log_lines = []
        # Initialize timestamp patterns
        # Matches almost all ISO-8601 timestamps
        timestamp_pattern = re.compile(
            r'\d{4}-\d{2}-\d{2}'                   # YYYY-MM-DD
            r'[T\s]'                               # T or space
            r'\d{2}:\d{2}:\d{2}'                   # HH:MM:SS
            r'(?:\.\d+)?'                          # optional .fractional seconds
            r'(?:Z|[+-]\d{2}:\d{2})?'              # optional timezone (Z or +hh:mm)
            r'\s*'                                 # trailing spaces
        )

        for line in log_lines:
            new_line = timestamp_pattern.sub('', line)
            # Only add unique lines
            if new_line not in new_log_lines:
                new_log_lines.append(new_line)
        return new_log_lines
    
    def create_word_dict(self, log_lines: list, window_size: int=1) -> dict:
        """Store unique words, their neighbors within window size, and frequency

        Args:
            log_lines (list): The list of log lines
            window_size (int): The size of the context window
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
                # # Check if the word have singular form
                # p = inflect.engine()
                # singular_word = p.singular_noun(word)
                # # If yes, replace the word with its singular form
                # if singular_word:
                #     print(f"Singular word: {singular_word}")
                #     word = singular_word
                #     words[i] = word
                # Only add unique words
                if word_dict.get(word):
                    word_dict[word]["freq"] += 1
                else:
                    # Initialize word
                    word_dict[word] = {"freq": 1, "context_words": []}
                # Add context words within window size
                start_idx = max(0, i - window_size)
                end_idx = min(len(words), i + window_size + 1)
                for j in range(start_idx, end_idx):
                    if j != i:
                        context_word = words[j]
                        if context_word not in word_dict[word]["context_words"]:
                            word_dict[word]["context_words"].append(context_word)
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
            word_index = self.global_vocab_processor.get_word_index(word.lower())
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
    
    def get_vocab(self):
        """Run the Word2Vec embedding process
        
        Returns:
            dict: The word dictionary with context words as indices
            list: The list of known words' indices
            list: The list of unknown words
        """
        data = self.load_client_dataset()
        # Delete time stamps
        data = self.delete_time_stamp(data)
        # Create word dictionary
        word_dict = self.create_word_dict(data)
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
