"""Test the embedding models accuracy in finding the right similar log."""
import json
import re
import numpy as np
from pathlib import Path
import gensim.downloader as api
import fasttext
from sentence_transformers import SentenceTransformer


NUM_LOGS_SELECTED = 5


class FindSimilarLogTester:
    """Test the embedding model accuracy in finding the right similar log."""
    def __init__(self, model_path: str, num_train_clients: int=2, which_model: str="fasttext") -> None:
        """Initialize the FindSimilarLogTester.
        
        Args:
            num_train_clients (int): the number of clients involve in the training process.
            which_model (str): the name of the pretrained model being tested
        """
        self.num_train_clients = num_train_clients
        self.which_model = which_model

        if which_model == "fasttext":
            self._pretrained_model = fasttext.load_model("cc.en.300.bin")
        elif which_model == "glove":
            self._pretrained_model = api.load("glove-wiki-gigaword-100")
        elif which_model == "sentence_transformer":
            self._pretrained_model = SentenceTransformer(
                "sentence-transformers/average_word_embeddings_glove.6B.300d"
            )
        

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
    
    def find_index_for_unknown_clients(self, word: str, model_path: str) -> int:
        """Try to find an index (if exist) for client whose does not involve in training process.
        
        Args:
            word (str): the client word which we try to search.
            model_path (str): the path to the model folder.
        """
        # Read the global vocab dictionary
        with open("dataset/global_vocab.json", "r", encoding="utf-8") as json_file:
            global_vocab = json.load(json_file)
        # Search for the word in the global vocab if exist
        global_index = global_vocab.get(word, -1)
        if global_index == -1:
            print(f"WARNING: word: {word} is not found in global vocab.")
            return -1
        # Read the all_indice_map which map global indices to internal indices
        all_indice_map_path = Path(model_path) / Path("all_indice_map.json")
        with open(all_indice_map_path, "r", encoding="utf-8") as json_file_1:
            indice_map = json.load(json_file_1)
        # Search for the global index in indices map if exist
        global_index = str(global_index)
        internal_index = indice_map.get(global_index, -1)
        if internal_index == -1:
            print(f"WARNING: word: {word} is not found in internal index.")
        return internal_index
    
    def find_internal_index_of_word(self, model_path: str, word: str, client_name: str) -> int:
        """Find the internal index representation of a word.
        
        Args:
            model_path (str): the path to the model folder.
            word (str): the word which we want to find its internal index.
            client_name (str): the name of client whose dataset the word is taken.
        """
        if self.num_train_clients == 3:
            train_clients = ["d2klab", "maryangel101"]
        else:
            train_clients = ["d2klab", "maryangel101", "logsage"]
        if client_name not in train_clients:
            return self.find_index_for_unknown_clients(word=word, model_path=model_path)
        # Get the client word dict
        base_path = Path(model_path)
        word_dict_path = base_path / Path(f"{client_name}_word_dict.json")
        with open(word_dict_path, "r", encoding="utf-8") as json_file:
            word_dict = json.load(json_file)
        # Get the word index
        word_info = word_dict.get(word)
        if not word_info:
            print(f"WARNING: word: {word} is not found.")
            return -1
        word_index = word_info.get("index", -1)
        return word_index

    def word_embedding_model(self, model_path: str, W1: np.ndarray, text: str, client_name: str) -> np.ndarray:
        """Embed the text using the word embedding model.

        Args:
            model_path (str): the path to the model folder.
            W1 (np.array): embedding matrix to embed words into vectors.
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
            word_index = self.find_internal_index_of_word(
                model_path=model_path, word=word, client_name=client_name)
            if word_index == -1:
                continue  # if the word embedding not found, skip
            # Get the embedding vector of the word
            word_embedding = W1[word_index, :]
            # Aggregate the embedding vector of the word to the vector of the whole text
            text_vector += word_embedding
        # Average the vectors to get the final text vector
        if word_list:
            text_vector /= len(word_list)
        return text_vector

    def fasttext_embedding(self, text: str) -> np.ndarray:
        words = self.split_text_to_word(text)
        vectors = [self._pretrained_model.get_word_vector(w) for w in words]

        if not vectors:
            return np.zeros(300, dtype=np.float32)

        return np.mean(vectors, axis=0)
    
    def sentence_transformer_embedding(self, text: str) -> np.ndarray:
        sentences = [s for s in text.splitlines() if s.strip()]
        if not sentences:
            return np.zeros(300, dtype=np.float32)

        embeddings = self._pretrained_model.encode(sentences)
        return embeddings.mean(axis=0)
    
    def pretrained_embedding_model(self, text: str) -> np.ndarray:

        if self.which_model == "glove":
            model = self._pretrained_models
            words = self.split_text_to_word(text=text)
            vectors = [model[w] for w in words if w in model]
            if not vectors:
                return np.zeros(300, dtype=np.float32)
            return np.mean(vectors, axis=0)
        elif self.which_model == "fasttext":
            return self.fasttext_embedding(text=text)
        elif self.which_model == "sentence_transformer":
            return self.sentence_transformer_embedding(text=text)
        else:
            raise ValueError(f"Unknown model: {which_model}")
    

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
    
    def collect_all_files_from_folder(self, folder_path: str) -> list[str]:
        """Get paths to all files in a folder.
        
        Args:
            folder_path (str): the path to the folder which we want to get all of its file paths.
        """
        folder_path = Path(folder_path)
        if not folder_path.exists():
            return []

        # Recursively collect all files
        file_paths = [
            str(path)
            for path in folder_path.rglob("*")
            if path.is_file()
        ]

        return file_paths
    
    def find_actual_similar_log_path(self, original_log_path: str) -> Path:
        """From the original log path, find the path to the generated log file which is actual similar.
        
        Args:
            original_log_path (str): the path to the original log file.
        """
        original_path = Path(original_log_path)

        parts = original_path.parts
        test_idx = parts.index("test")

        actual_similar_log_path = Path(
            *parts[:test_idx],
            "generate_test_log",
            *parts[test_idx + 1:]
        ).resolve()
        return actual_similar_log_path

    
    def run_test_for_client(self, model_path: str, W1, client_name: str) -> float:
        """Run the finding similar log test for a client test data.
        
        Args:
            model_path (str): the path to the model path.
            W1 (np.array): embedding matrix to embed words into vectors.
            client_name (str): the name of the client which test data is being used.
        """
        # Read the list of all test log files and generated test log files
        test_paths = self.collect_all_files_from_folder(f"dataset/train_test_internal/{client_name}/test")
        generated_log_paths = self.collect_all_files_from_folder(
            f"dataset/train_test_internal/{client_name}/generate_test_log")
        
        # Collect all original logs
        original_logs = []
        for test_path in test_paths:
            # Read the training log
            with open(test_path, "r", encoding="utf-8") as file:
                original_log = file.read()
            original_logs.append((test_path, original_log))

        # Collect all testing logs
        generated_logs = []
        for generated_path in generated_log_paths:
            with open(generated_path, "r", encoding="utf-8") as file:
                generated_log = file.read()
            generated_logs.append((generated_path, generated_log))

        if self.num_train_clients == 3:
            train_clients = ["d2klab", "maryangel101", "logsage"]
        else:
            train_clients = ["d2klab", "maryangel101"]
        # If the client involve in training, find the word in their word dict
        if client in train_clients:
            # Get the word dict
            word_dict_path = Path(model_path) / Path(f"{client}_word_dict.json")
            with open(word_dict_path, "r", encoding="utf-8") as json_file:
                word_dict = json.load(json_file)
        else:
            # Read the global vocab dictionary
            with open("dataset/global_vocab.json", "r", encoding="utf-8") as json_file:
                global_vocab = json.load(json_file)
            

        

        # Initialize variables to count the accuracy time
        accuracy_count = 0
        for original_path, original_log in original_logs:
            # Calculate vector representation of original log
            original_vec = self.word_embedding_model(model_path, W1, original_log, client_name)

            generated_logs_vec = []
            for generated_path, generated_log in generated_logs:
                # Calculate vector representation of the logs
                generated_vec = self.word_embedding_model(model_path, W1, generated_log, client_name)
                generated_logs_vec.append((generated_path, generated_vec))

            similar_logs = self.find_k_similar_logs(original_vec, generated_logs_vec, k=NUM_LOGS_SELECTED)

            actual_similar_log_path = self.find_actual_similar_log_path(original_log_path=original_path)

            print("--------------------------------------------------")
            print(f"Finding similar logs for {original_path}:")
            for i, (file_path, similarity) in enumerate(similar_logs):
                if Path(file_path).resolve() == actual_similar_log_path:
                    accuracy_count += 1
                    print(f"TRUE: included at rank {i + 1} with similarity {similarity:.4f}")
                print(f"Rank {i + 1}: {Path(file_path).name} with similarity {similarity:.4f}")
            # if similar_logs[0][0] == actual_similar_log_path:
            #     accuracy_count += 1
            #     print(f"TRUE: with similarity {similar_logs[0][1]:.4f}")
            print("--------------------------------------------------")
        accuracy_rate = accuracy_count / len(test_paths)
        print(f"Accuracy rate for client {client_name}:\n{accuracy_rate:.4f}")
        return accuracy_rate
    
    def test_with_pretrained_model(self, client_name: str) -> float:
        """Run the finding similar log test for a client test data.
        
        Args:
            client_name (str): the name of the client which test data is being used.
        """
        # Read the list of all test log files and generated test log files
        test_paths = self.collect_all_files_from_folder(f"dataset/train_test_internal/{client_name}/test")
        generated_log_paths = self.collect_all_files_from_folder(
            f"dataset/train_test_internal/{client_name}/generate_test_log")
        
        # Collect all original logs
        original_logs = []
        for test_path in test_paths:
            # Read the training log
            with open(test_path, "r", encoding="utf-8") as file:
                original_log = file.read()
            original_logs.append((test_path, original_log))

        # Collect all testing logs
        generated_logs = []
        for generated_path in generated_log_paths:
            with open(generated_path, "r", encoding="utf-8") as file:
                generated_log = file.read()
            generated_logs.append((generated_path, generated_log))

        # Initialize variables to count the accuracy time
        accuracy_count = 0
        for original_path, original_log in original_logs:
            # Calculate vector representation of original log
            original_vec = self.pretrained_embedding_model(text=original_log)

            generated_logs_vec = []
            for generated_path, generated_log in generated_logs:
                # Calculate vector representation of the logs
                generated_vec = self.pretrained_embedding_model(text=generated_log)
                generated_logs_vec.append((generated_path, generated_vec))

            similar_logs = self.find_k_similar_logs(original_vec, generated_logs_vec, k=NUM_LOGS_SELECTED)

            actual_similar_log_path = self.find_actual_similar_log_path(original_log_path=original_path)

            print("--------------------------------------------------")
            print(f"Finding similar logs for {original_path}:")
            for i, (file_path, similarity) in enumerate(similar_logs):
                if Path(file_path).resolve() == actual_similar_log_path:
                    accuracy_count += 1
                    print(f"TRUE: included at rank {i + 1} with similarity {similarity:.4f}")
                print(f"Rank {i + 1}: {Path(file_path).name} with similarity {similarity:.4f}")
            # if similar_logs[0][0] == actual_similar_log_path:
            #     accuracy_count += 1
            #     print(f"TRUE: with similarity {similar_logs[0][1]:.4f}")
            print("--------------------------------------------------")
        accuracy_rate = accuracy_count / len(test_paths)
        print(f"Accuracy rate for client {client_name}:\n{accuracy_rate:.4f}")
        return accuracy_rate


if __name__ == "__main__":
    # Please change this path to the path to the model folder which you want to test
    model_path = "models/2_clients_2_context_10_5_epochs"

    # Please list the clients which test dataset will be used here
    client_list = ["d2klab", "maryangel101", "logsage"]  # "d2klab", "maryangel101"

    # Test self-trained word2vec model

    # Get the number of client trained
    # num_clients = int(model_path.split("/")[-1][0])

    # tester = FindSimilarLogTester(num_train_clients=num_clients)

    # # Get the path to the model weights.
    # w1_path = Path(model_path) / Path("W1_word2vec.npy")
    # w2_path = Path(model_path) / Path("W2_word2vec.npy")
    # # Load the model
    # W1 = np.load(w1_path)
    # W2 = np.load(w2_path)

    # for client in client_list:
    #     tester.run_test_for_client(
    #         model_path=model_path, W1=W1, client_name=client
    #     )

    # Test pretrained model
    tester = FindSimilarLogTester(which_model="sentence_transformer")
    for client in client_list:
        tester.test_with_pretrained_model(client_name=client)
