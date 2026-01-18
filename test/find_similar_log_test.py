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

    def word_embedding_model(self, text: str, client_name: str) -> np.ndarray:
        """Embed the text using the word embedding model.

        Args:
            text (str): The input text to embed.
            client_name (str): which client can we read their internal vocabs

        Returns:
            np.ndarray: The embedded vector of the text.
        """
        # Read the model weights
        W1 = np.load("models/W1_word2vec.npy")
        W2 = np.load("models/W2_word2vec.npy")

        # Split text into words
        # Split on spaces, underscores, hyphens
        word_list = re.split(r'[\s_-]+', text)
        # Split camelCase
        words = []
        for part in word_list:
            split_camel = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', part)
            words.extend(split_camel)
        word_list = words

        # Read the client vocabulary
        with open(f"dataset/{client_name}_new_word_dict.json", "r", encoding="utf-8") as file:
            client_vocab = json.load(file)

        word_index = None
        # Initialize the overall vector for the text
        embedding_dim = W1.shape[1]  # number of dimensions in your word embeddings
        text_vector = np.zeros(embedding_dim)
        # Loop through each word in the text and add its vector into text vector
        for word in word_list:
            # Find index representation of the word
            for client_word, client_word_info in client_vocab.items():
                if word == client_word:
                    # Found the word, get its index
                    word_index = client_word_info["index"]
                    break
                elif word.lower() == client_word.lower():
                    # Found the word, get its index
                    word_index = client_word_info["index"]
                    break
            if word_index is None:
                print(f"Word '{word}' not found in client vocabulary.")
                continue
            word_embedding = W1[word_index, :]
            text_vector += word_embedding
        # Average the vectors to get the final text vector
        if word_list:
            text_vector /= len(word_list)
        return text_vector
    
    def doc_embedding_model(self, text: str) -> np.ndarray:
        """Embed the document using the document embedding model.

        Args:
            text (str): The input text to embed.

        Returns:
            np.ndarray: The embedded vector of the document.
        """
        pass

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
    
    def run_test_for_client(self, client_name: str, model_name: str) -> None:
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
                original_vec = self.word_embedding_model(original_log, client_name)

                test_logs_vec = []
                for test_path, test_log in test_logs:
                    # Calculate vector representation of the logs
                    test_vec = self.word_embedding_model(test_log, client_name)
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
            print(f"Accuracy rate for client {client_name} using {model_name}:\n{accuracy_count / len(training_data_paths):.4f}")
        elif model_name == "Sentence2Vec":
            return
        elif model_name == "Doc2Vec":
            return
        else:
            print(f"Model {model_name} not supported.")


if __name__ == "__main__":
    tester = FindSimilarLogTester()
    for client in CLIENT_LIST:
        tester.run_test_for_client(client, model_name="Word2Vec")
