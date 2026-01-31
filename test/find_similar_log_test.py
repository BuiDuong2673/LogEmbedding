"""Test the embedding models accuracy in finding the right similar log."""
import json
import re
import numpy as np
from pathlib import Path

from helper.create_training_dataset import TrainingDatasetCreator


NUM_LOGS_SELECTED = 5
CLIENT_LIST = ["d2klab", "maryangel101"]


class FindSimilarLogTester:
    """Test the embedding models accuracy in finding the right similar log."""
    def __init__(self):
        """Initialize the FindSimilarLogTester."""
        pass

    def split_text_to_word(self, text: str) -> list[str]:
        """Split the given text to word so that it is searchable in the dictionary.
        
        Args:
            text (str): the text which need extracting words.
        """
        # Initialize the collection
        words = set()
        # Split text into list of lines
        lines = text.splitlines()
        # Define timestampt pattern to be deleted
        timestamp_pattern = re.compile(
            r'\d{4}-\d{2}-\d{2}'                   # YYYY-MM-DD
            r'[T\s]'                               # T or space
            r'\d{2}:\d{2}:\d{2}'                   # HH:MM:SS
            r'(?:\.\d+)?'                          # optional .fractional seconds
            r'(?:Z|[+-]\d{2}:\d{2})?'              # optional timezone (Z or +hh:mm)
            r'\s*'                                 # trailing spaces
        )
        for line in lines:
            # Delete timestampt
            line = timestamp_pattern.sub('', line).strip('\n')
            # Split on spaces, underscores, hyphens
            parts = re.split(r'[\s_-]+', line)
            # Split camelCase
            for part in parts:
                split_camel = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', part)
                words.update(split_camel)
        # Change the words from set to list
        words = [word.lower() for word in words if word]
        return words
    
    def find_internal_index_of_word(self, word: str, client_name: str) -> int:
        """Find the internal index representation of a word.
        
        Args:
            word (str): the word which we want to find its internal index.
            client_name (str): the name of client whose dataset the word is taken.
        """
        # Get the client word dict
        word_dict_path = Path("dataset") / Path(f"{client_name}")
        with open(word_dict_path, "r", encoding="utf-8") as json_file:
            word_dict = json.load(json_file)
        # Get the word index
        word_info = word_dict.get(word)
        if not word_info:
            print(f"WARNING: word: {word} is not found.")
            return -1
        word_index = word_info.get("index", -1)
        return word_index

    def word_embedding_model(self, W1: np.ndarray, text: str, client_name: str) -> np.ndarray:
        """Embed the text using the word embedding model.

        Args:
            text (str): The input text to embed.
            client_name (str): which client whose test set is running.

        Returns:
            np.ndarray: The embedded vector of the text.
        """
        # Get all the words from the text
        word_list = self.split_text_to_word(text=text)
        if not word_list:
            print("WARNING: the text contain no word.")
            return np.zeros(W1.shape[1], dtype=np.float32)
        # Initialize the overall vector for the text
        embedding_dim = W1.shape[1]  # number of dimensions in your word embeddings
        text_vector = np.zeros(embedding_dim)
        # Find the embedding of each word
        for word in word_list:
            # Get the internal index representing the word
            word_index = self.find_internal_index_of_word(word=word, client_name=client_name)
            if word_index == -1:
                print(f"WARNING: word: {word} is not found.")
            # Get the embedding vector of the word
            word_embedding = W1[word_index, :]
            # Aggregate the embedding vector of the word to the vector of the whole text
            text_vector += word_embedding
        # Average the vectors to get the final text vector
        if word_list:
            text_vector /= len(word_list)
        return text_vector

    def cosine_similarity(self, vector1: np.ndarray, vector2: np.ndarray) -> float:
        """Compute the distance between two text embeddings.

        Args:
            vector1 (np.ndarray): The first text embedding to compare.
            vector2 (np.ndarray): The second text embedding to compare.
        """
        norm1 = np.linalg.norm(vector1)
        norm2 = np.linalg.norm(vector2)
        if norm1 > 0 and norm2 > 0:
            cosine_sim = np.dot(vector1, vector2) / (norm1 * norm2)
        else:
            cosine_sim = 0
        return cosine_sim

    def find_k_similar_logs(self, original_vec: np.ndarray, generated_vecs: list[tuple[str, np.ndarray]], k: int=NUM_LOGS_SELECTED) -> str:
        """Find the most similar log in the generated logs.
        
        Args:
            original_vec (np.ndarray): The vector representation of the original log.
            generated_vecs (list[tuple[str, np.ndarray]]): The list of (file_path, generated log vector) to compare against.
            k (int): The number of top similar logs to return.
        """
        similarity_list = []
        for file_path, generated_vec in generated_vecs:
            # Calculate the cosine similarity between 2 logs
            similarity = self.cosine_similarity(original_vec, generated_vec)
            similarity_list.append((file_path, similarity))
        # Sort the similarity list so that the most similar log is first
        similarity_list.sort(key=lambda x: x[1], reverse=True)
        return similarity_list[:k]
    
    def run_test_for_client(self, W1, W2, client_name: str, model_name: str) -> float:
        # Read the list of file path of client training and testing data
        training_data_paths = TrainingDatasetCreator().get_file_list_from_folder(f"dataset/training/{client_name}")
        testing_data_paths = TrainingDatasetCreator().get_file_list_from_folder(f"dataset/testing/{client_name}")
        
        # Collect all training logs
        train_logs = []
        for train_path in training_data_paths:
            # Read the training log
            with open(train_path, "r", encoding="utf-8") as file:
                original_log = file.read()
            train_logs.append((train_path, original_log))

        # Collect all testing logs
        test_logs = []
        for test_path in testing_data_paths:
            with open(test_path, "r", encoding="utf-8") as file:
                test_log = file.read()
            test_logs.append((test_path, test_log))

        if model_name == "Word2Vec":
            # Initialize variables to count the accuracy time
            accuracy_count = 0
            for original_path, original_log in train_logs:
                # Calculate vector representation of original log
                original_vec = self.word_embedding_model(W1, W2, original_log, client_name)

                test_logs_vec = []
                for test_path, test_log in test_logs:
                    # Calculate vector representation of the logs
                    test_vec = self.word_embedding_model(W1, W2, test_log, client_name)
                    test_logs_vec.append((test_path, test_vec))

                similar_logs = self.find_k_similar_logs(original_vec, test_logs_vec, k=NUM_LOGS_SELECTED)

                actual_similar_log_path = original_path.replace("training", "testing")

                print("--------------------------------------------------")
                print(f"Finding similar logs for {original_path}:")
                for i, (file_path, similarity) in enumerate(similar_logs):
                    if file_path == actual_similar_log_path:
                        accuracy_count += 1
                        print(f"TRUE: included at rank {i + 1} with similarity {similarity:.4f}")
                    print(f"Rank {i + 1}: {Path(file_path).name} with similarity {similarity:.4f}")
                # if similar_logs[0][0] == actual_similar_log_path:
                #     accuracy_count += 1
                #     print(f"TRUE: with similarity {similar_logs[0][1]:.4f}")
                print("--------------------------------------------------")
            accuracy_rate = accuracy_count / len(training_data_paths)
            print(f"Accuracy rate for client {client_name} using {model_name}:\n{accuracy_rate:.4f}")
            return accuracy_rate
        elif model_name == "Sentence2Vec":
            return -1.0
        elif model_name == "Doc2Vec":
            return -1.0
        else:
            print(f"Model {model_name} not supported.")


if __name__ == "__main__":
    tester = FindSimilarLogTester()
    for client in CLIENT_LIST:
        tester.run_test_for_client(client, model_name="Word2Vec")
