"""Involve test program for self-trained model and pretrained model."""

import json
import os
import re
from pathlib import Path

import gensim.downloader as gensim_api
import numpy as np
import torch
import torch.nn.functional as F
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from transformers import AutoModel, AutoTokenizer

hf_token = os.getenv("HUGGINGFACE_TOKEN")


class SelfTrainTester:
    """Test self-trained model ability in finding similar log."""

    def __init__(self, train_clients: list[str], test_clients: list[str], model_path: str, k: int = 5) -> None:
        """Initialize SelfTrainTester.

        Args:
            train_clients (list[str]): the list of clients involving in training.
            test_clients (list[str]): the list of clients whose datasets are used to test.
            model_path (str): the path to the folder of the model being tested.
            k (int): top k similar logs should be selected.
        """
        self.train_clients = train_clients
        self.test_clients = test_clients
        self.model_path = model_path
        self.k_value = k

        # Check if test_clients contains any clients that are not in train clients set
        invalid_clients = set(self.test_clients) - set(self.train_clients)
        if invalid_clients:
            # Read global vocab and indice map for finding unknown client words
            # Read the global vocab dictionary
            with open("dataset/global_vocab.json", "r", encoding="utf-8") as json_file:
                self.global_vocab = json.load(json_file)
            # Read the dictionary mapping global index with internal index
            all_indice_map_path = Path(model_path) / Path("all_indice_map.json")
            with open(all_indice_map_path, "r", encoding="utf-8") as json_file_1:
                self.indice_map = json.load(json_file_1)

        # Read trained client word dicts
        all_word_dict = {}
        for client in train_clients:
            word_dict_path = Path(model_path) / Path(f"{client}_word_dict.json")
            with open(word_dict_path, "r", encoding="utf-8") as json_file:
                word_dict = json.load(json_file)
            all_word_dict[client] = word_dict
        self.all_word_dict = all_word_dict

        # Get the embedding model
        w1_path = Path(model_path) / Path("W1_word2vec.npy")
        self.W1 = np.load(w1_path)

    def split_text_to_word(self, text: str) -> list[str]:
        """Split the given text to word so that it is searchable in the dictionary.

        Args:
            text (str): the text which need extracting words.
        """
        # If the text is already splitted, retrieve it directly
        if not hasattr(self, "_word_cache"):
            self._word_cache = {}
        if text in self._word_cache:
            return self._word_cache[text]
        # Initialize the collection
        words = set()
        # Split text into list of lines
        lines = text.splitlines()
        # Define timestampt pattern to be deleted
        timestamp_pattern = re.compile(
            r"\d{4}-\d{2}-\d{2}"  # YYYY-MM-DD
            r"[T\s]"  # T or space
            r"\d{2}:\d{2}:\d{2}"  # HH:MM:SS
            r"(?:\.\d+)?"  # optional .fractional seconds
            r"(?:Z|[+-]\d{2}:\d{2})?"  # optional timezone (Z or +hh:mm)
            r"\s*"  # trailing spaces
        )
        for line in lines:
            # Delete timestampt
            line = timestamp_pattern.sub("", line).strip("\n")
            # Split on spaces, underscores, hyphens
            parts = re.split(r"[\s_-]+", line)
            # Split camelCase
            for part in parts:
                split_camel = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])", part)
                words.update(split_camel)
        # Change the words from set to list
        words = [word.lower() for word in words if word]
        # Save the splitted text for later use
        self._word_cache[text] = words
        return words

    def find_index_for_word_train(self, word: str, client_name: str) -> int:
        """Find the internal index corresponding to the word in case the word is from a trained client dataset.

        Args:
            word (str): the word which need finding the index.
            client_name (str): the name of the trained client which has the word.
        """
        # Get client word dict
        word_dict = self.all_word_dict.get(client_name)
        # Get the word index
        word_info = word_dict.get(word)
        if not word_info:
            print(f"WARNING: word: {word} is not found.")
            return -1
        word_index = word_info.get("index", -1)
        return word_index

    def find_index_for_word_untrain(self, word: str) -> int:
        """Find the index for a word come from client who did not involve in training the model.

        Args:
            word (str): the word to search for.
        """
        # Search for the word in the global vocab if exist
        global_index = self.global_vocab.get(word, -1)
        if global_index == -1:
            print(f"WARNING: word: {word} is not found in global vocab.")
            return -1
        # Search for the global index in indices map if exist
        global_index = str(global_index)
        internal_index = self.indice_map.get(global_index, -1)
        if internal_index == -1:
            print(f"WARNING: word: {word} is not found in internal index.")
        return internal_index

    def word_embedding_train(self, text: str, client_name: str) -> np.ndarray:
        """Embed the text which come from client involving in training process.

        Args:
            text (str): The input text to embed.
            client_name (str): the name of the client who has that word.

        Returns:
            np.ndarray: The embedded vector of the text.
        """
        # Get all the words from the text
        word_list = self.split_text_to_word(text=text)
        if not word_list:
            print("WARNING: the text contain no word.")
            return np.zeros(self.W1.shape[1], dtype=np.float32)
        # Initialize the overall vector for the text
        embedding_dim = self.W1.shape[1]  # number of dimensions in your word embeddings
        text_vector = np.zeros(embedding_dim)
        # Find the embedding of each word
        for word in word_list:
            # Get the internal index representing the word
            word_index = self.find_index_for_word_train(word=word, client_name=client_name)
            if word_index == -1:
                continue  # if the word embedding not found, skip
            # Get the embedding vector of the word
            word_embedding = self.W1[word_index, :]
            # Aggregate the embedding vector of the word to the vector of the whole text
            text_vector += word_embedding
        # Average the vectors to get the final text vector
        if word_list:
            text_vector /= len(word_list)
        return text_vector

    def word_embedding_untrain(self, text: str) -> np.ndarray:
        """Embed the text which come from client did not involve in training process.

        Args:
            text (str): The input text to embed.

        Returns:
            np.ndarray: The embedded vector of the text.
        """
        # Get all the words from the text
        word_list = self.split_text_to_word(text=text)
        if not word_list:
            print("WARNING: the text contain no word.")
            return np.zeros(self.W1.shape[1], dtype=np.float32)
        # Initialize the overall vector for the text
        embedding_dim = self.W1.shape[1]  # number of dimensions in your word embeddings
        text_vector = np.zeros(embedding_dim)
        # Find the embedding of each word
        for word in word_list:
            # Get the internal index representing the word
            word_index = self.find_index_for_word_untrain(word=word)
            if word_index == -1:
                continue  # if the word embedding not found, skip
            # Get the embedding vector of the word
            word_embedding = self.W1[word_index, :]
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

    def find_k_similar_logs(self, original_vec: np.ndarray, generated_vecs: list[tuple[str, np.ndarray]]) -> str:
        """Find the most similar log in the generated logs.

        Args:
            original_vec (np.ndarray): The vector representation of the original log.
            generated_vecs (list[tuple[str, np.ndarray]]): The list of (file_path, generated log vector) to compare against.
        """
        similarity_list = []
        for file_path, generated_vec in generated_vecs:
            # Calculate the cosine similarity between 2 logs
            similarity = self.cosine_similarity(original_vec, generated_vec)
            similarity_list.append((file_path, similarity))
        # Sort the similarity list so that the most similar log is first
        similarity_list.sort(key=lambda x: x[1], reverse=True)
        return similarity_list[: self.k_value]

    def collect_all_files_from_folder(self, folder_path: str) -> list[str]:
        """Get paths to all files in a folder.

        Args:
            folder_path (str): the path to the folder which we want to get all of its file paths.
        """
        folder_path = Path(folder_path)
        if not folder_path.exists():
            return []
        # Recursively collect all files
        file_paths = [str(path) for path in folder_path.rglob("*") if path.is_file()]
        return file_paths

    def find_actual_similar_log_path(self, original_log_path: str) -> Path:
        """From the original log path, find the path to the generated log file which is actual similar.

        Args:
            original_log_path (str): the path to the original log file.
        """
        original_path = Path(original_log_path)
        parts = original_path.parts
        test_idx = parts.index("test")
        actual_similar_log_path = Path(*parts[:test_idx], "generate_test_log", *parts[test_idx + 1 :]).resolve()
        return actual_similar_log_path

    def run_test_for_client(self, client_name: str) -> float:
        """Run the finding similar log test for a client test data.

        Args:
            client_name (str): the name of the client which test data is being used.
        """
        # Read the list of all test log files and generated test log files
        test_paths = self.collect_all_files_from_folder(f"dataset/train_test_balanced/{client_name}/test")
        generated_log_paths = self.collect_all_files_from_folder(
            f"dataset/train_test_balanced/{client_name}/generate_test_log"
        )

        # Check if client involve in training
        if client_name in self.train_clients:
            is_train_client = True
        else:
            is_train_client = False

        # Collect all original logs and get their embedding.
        original_logs = []
        for test_path in test_paths:
            # Read the training log
            with open(test_path, "r", encoding="utf-8") as file:
                original_log = file.read()
            # Get log embedding
            if is_train_client:
                original_vec = self.word_embedding_train(text=original_log, client_name=client_name)
            else:
                original_vec = self.word_embedding_untrain(text=original_log)
            original_logs.append((test_path, original_vec))

        # Collect all testing logs
        generated_logs = []
        for generated_path in generated_log_paths:
            with open(generated_path, "r", encoding="utf-8") as file:
                generated_log = file.read()
            if is_train_client:
                generated_vec = self.word_embedding_train(text=generated_log, client_name=client_name)
            else:
                generated_vec = self.word_embedding_untrain(text=generated_log)
            generated_logs.append((generated_path, generated_vec))

        # Initialize variables to count the accuracy time
        accuracy_count = 0
        accuracy_1_count = 0  # only in rank 1 is considered correct
        for original_path, original_vec in original_logs:
            # Find k similar logs
            similar_logs = self.find_k_similar_logs(original_vec, generated_logs)
            # Get the real similar generated log
            actual_similar_log_path = self.find_actual_similar_log_path(original_log_path=original_path)
            print("--------------------------------------------------")
            print(f"Finding similar logs for {original_path}:")
            for i, (file_path, similarity) in enumerate(similar_logs):
                if Path(file_path).resolve() == actual_similar_log_path:
                    accuracy_count += 1
                    if i == 1:
                        accuracy_1_count += 1
                    print(f"TRUE: included at rank {i + 1} with similarity {similarity:.4f}")
                print(f"Rank {i + 1}: {Path(file_path).name} with similarity {similarity:.4f}")
            print("--------------------------------------------------")
        print("=" * 50)
        print(f"Accuracy rate for client {client_name}:")
        # Calculate the accuracy of having most similar log in top 5
        accuracy_rate = accuracy_count / len(test_paths)
        print(f"Having similar generated log in top 5: {accuracy_rate:.4f}")
        # Calculate the accuracy of having most similar log in top 1
        accuracy_1_rate = accuracy_1_count / len(test_paths)
        print(f"Having similar generated log in top 1: {accuracy_1_rate:.4f}")
        print("=" * 50)

    def run(self):
        for client in self.test_clients:
            self.run_test_for_client(client_name=client)


class PreTrainTester:
    """Test the pretrained models."""

    def __init__(self, test_clients: list[str], which_model: str, k: int = 5) -> None:
        """Initialize PreTrainTester class.

        Args:
            test_clients (list[str]): the list of clients whose test dataset will be used.
            which_model (str): the name of the pretrained model being tested.
            k (int): value of k for top k similar log selection.
        """
        self.test_clients = test_clients
        self.which_model = which_model
        self.k_value = k
        # login(hf_token)

        if which_model == "glove":
            self._pretrained_model = SentenceTransformer("sentence-transformers/average_word_embeddings_glove.6B.300d")
        elif which_model == "all-MiniLM-L6-v2":
            self._pretrained_model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
            self._tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        elif which_model == "fasttext":
            self._pretrained_model = gensim_api.load("fasttext-wiki-news-subwords-300")
        elif which_model in ["e5-base-v2", "intfloat/e5-base-v2"]:
            self._pretrained_model = SentenceTransformer("intfloat/e5-base-v2")
        elif which_model == "embeddinggemma-300m":
            self._embedder = HuggingFaceEmbeddings(
                model_name="google/embeddinggemma-300m",
                query_encode_kwargs={"prompt_name": "query"},
                encode_kwargs={"prompt_name": "document"},
            )
        else:
            raise ValueError(f"We do not have this model '{which_model}'.")

    def split_text_to_word(self, text: str) -> list[str]:
        """Split the given text to word so that it is searchable in the dictionary.

        Args:
            text (str): the text which need extracting words.
        """
        # If the text is already splitted, retrieve it directly
        if not hasattr(self, "_word_cache"):
            self._word_cache = {}
        if text in self._word_cache:
            return self._word_cache[text]
        # Initialize the collection
        words = set()
        # Split text into list of lines
        lines = text.splitlines()
        # Define timestampt pattern to be deleted
        timestamp_pattern = re.compile(
            r"\d{4}-\d{2}-\d{2}"  # YYYY-MM-DD
            r"[T\s]"  # T or space
            r"\d{2}:\d{2}:\d{2}"  # HH:MM:SS
            r"(?:\.\d+)?"  # optional .fractional seconds
            r"(?:Z|[+-]\d{2}:\d{2})?"  # optional timezone (Z or +hh:mm)
            r"\s*"  # trailing spaces
        )
        for line in lines:
            # Delete timestampt
            line = timestamp_pattern.sub("", line).strip("\n")
            # Split on spaces, underscores, hyphens
            parts = re.split(r"[\s_-]+", line)
            # Split camelCase
            for part in parts:
                split_camel = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])", part)
                words.update(split_camel)
        # Change the words from set to list
        words = [word.lower() for word in words if word]
        # Save the splitted text for later use
        self._word_cache[text] = words
        return words

    def split_text_to_sentences(self, text: str) -> list[str]:
        """Split log into sentences with timestampt deleted.

        Args:
            text (str): the text which need extracting words.
        """
        # If the text is already splitted, retrieve it directly
        if not hasattr(self, "_sentence_cache"):
            self._sentence_cache = {}
        if text in self._sentence_cache:
            return self._sentence_cache[text]
        # Split text into list of lines
        lines = text.splitlines()
        # Define timestampt pattern to be deleted
        timestamp_pattern = re.compile(
            r"\d{4}-\d{2}-\d{2}"  # YYYY-MM-DD
            r"[T\s]"  # T or space
            r"\d{2}:\d{2}:\d{2}"  # HH:MM:SS
            r"(?:\.\d+)?"  # optional .fractional seconds
            r"(?:Z|[+-]\d{2}:\d{2})?"  # optional timezone (Z or +hh:mm)
            r"\s*"  # trailing spaces
        )
        # filtered timestampt lines
        new_lines = set()
        for line in lines:
            # Delete timestampt
            line = timestamp_pattern.sub("", line).strip("\n")
            new_lines.update(line)
        # Save the splitted text for later use
        self._sentence_cache[text] = list(new_lines)
        return list(new_lines)

    def glove_embedding(self, text: str) -> np.ndarray:
        """Embed the log using glove model.
        Source: https://huggingface.co/sentence-transformers/average_word_embeddings_glove.6B.300d

        Args:
            text (str): the log to be embedded into vector.
        """
        sentences = self.split_text_to_sentences(text)
        if not sentences:
            return np.zeros(300, dtype=np.float32)
        embeddings = self._pretrained_model.encode(sentences)
        return embeddings.mean(axis=0)

    def all_MiniLM_L6_v2_embedding(self, text: str) -> np.ndarray:
        """Embed the log using all-MiniLM-L6-v2 model.
        Source: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

        Args:
            text (str): the text to be embedded.
        """

        sentences = self.split_text_to_sentences(text=text)
        if not sentences:
            return np.zeros(384, dtype=np.float32)

        encoded_input = self._tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

        with torch.no_grad():
            model_output = self._pretrained_model(**encoded_input)

        token_embeddings = model_output.last_hidden_state
        attention_mask = encoded_input["attention_mask"]

        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sentence_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
            input_mask_expanded.sum(1), min=1e-9
        )

        sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

        # Aggregate sentence embeddings into ONE log embedding
        return sentence_embeddings.mean(dim=0).cpu().numpy()

    def fasttext_embedding(self, text: str) -> np.ndarray:
        """Embed the log using fastText model.
        Source: https://github.com/facebookresearch/fastText/blob/main/docs/crawl-vectors.md

        Args:
            text (str): the text to be embedded.
        """
        words = self.split_text_to_word(text=text)
        if not words:
            return np.zeros(300, dtype=np.float32)

        word_embeddings = []
        for word in words:
            try:
                word_embeddings.append(self._pretrained_model.get_vector(word))
            except KeyError:
                continue

        if not word_embeddings:
            return np.zeros(300, dtype=np.float32)

        return np.mean(np.array(word_embeddings), axis=0)

    def e5_base_v2_embedding(self, text: str) -> np.ndarray:
        """Embed the log using E5-base-v2 model.
        Source: https://huggingface.co/intfloat/e5-base-v2

        Args:
            text (str): the text to be embedded.
        """
        lines = text.splitlines()
        timestamp_pattern = re.compile(
            r"\d{4}-\d{2}-\d{2}"
            r"[T\s]"
            r"\d{2}:\d{2}:\d{2}"
            r"(?:\.\d+)?"
            r"(?:Z|[+-]\d{2}:\d{2})?"
            r"\s*"
        )
        cleaned_lines = []
        for line in lines:
            line = timestamp_pattern.sub("", line).strip()
            if line:
                cleaned_lines.append(line)

        cleaned_text = " ".join(cleaned_lines).strip()
        if not cleaned_text:
            return np.zeros(768, dtype=np.float32)

        embedding = self._pretrained_model.encode(
            [f"passage: {cleaned_text}"], normalize_embeddings=True, convert_to_numpy=True
        )
        return embedding[0]

    def embedding_model(self, text: str, which_model: str) -> np.ndarray:
        """Using the selected model for embedding the text.

        Args:
            text (str): the log to be embedded into vector.
            which_model (str): the name of the pretrained embedding model.
        """
        if which_model == "glove":
            return self.glove_embedding(text=text)
        elif which_model == "all-MiniLM-L6-v2":
            return self.all_MiniLM_L6_v2_embedding(text=text)
        elif which_model == "fasttext":
            return self.fasttext_embedding(text=text)
        elif which_model in ["e5-base-v2", "intfloat/e5-base-v2"]:
            return self.e5_base_v2_embedding(text=text)
        raise ValueError(f"We do not have this model '{which_model}'.")

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

    def find_k_similar_logs(self, original_vec: np.ndarray, generated_vecs: list[tuple[str, np.ndarray]]):
        """Find the most similar log in the generated logs.

        Args:
            original_vec (np.ndarray): The vector representation of the original log.
            generated_vecs (list[tuple[str, np.ndarray]]): The list of (file_path, generated log vector) to compare against.
        """
        similarity_list = []
        for file_path, generated_vec in generated_vecs:
            # Calculate the cosine similarity between 2 logs
            similarity = self.cosine_similarity(original_vec, generated_vec)
            similarity_list.append((file_path, similarity))
        # Sort the similarity list so that the most similar log is first
        similarity_list.sort(key=lambda x: x[1], reverse=True)
        return similarity_list[: self.k_value]

    def collect_all_files_from_folder(self, folder_path: str) -> list[str]:
        """Get paths to all files in a folder.

        Args:
            folder_path (str): the path to the folder which we want to get all of its file paths.
        """
        folder_path = Path(folder_path)
        if not folder_path.exists():
            return []
        # Recursively collect all files
        file_paths = [str(path) for path in folder_path.rglob("*") if path.is_file()]
        return file_paths

    def find_actual_similar_log_path(self, original_log_path: str) -> Path:
        """From the original log path, find the path to the generated log file which is actual similar.

        Args:
            original_log_path (str): the path to the original log file.
        """
        original_path = Path(original_log_path)
        parts = original_path.parts
        test_idx = parts.index("test")
        actual_similar_log_path = Path(*parts[:test_idx], "generate_test_log", *parts[test_idx + 1 :]).resolve()
        return actual_similar_log_path

    def run_test_for_client(self, client_name: str) -> float:
        """Run the finding similar log test for a client test data.

        Args:
            client_name (str): the name of the client which test data is being used.
        """
        # Read the list of all test log files and generated test log files
        test_paths = self.collect_all_files_from_folder(f"dataset/train_test_balanced/{client_name}/test")
        generated_log_paths = self.collect_all_files_from_folder(
            f"dataset/train_test_balanced/{client_name}/generate_test_log"
        )

        # Collect all original logs and get their embedding.
        original_logs = []
        for test_path in test_paths:
            # Read the training log
            with open(test_path, "r", encoding="utf-8") as file:
                original_log = file.read()
            # Get log embedding
            original_vec = self.embedding_model(text=original_log, which_model=self.which_model)
            original_logs.append((test_path, original_vec))

        # Collect all testing logs
        generated_logs = []
        for generated_path in generated_log_paths:
            with open(generated_path, "r", encoding="utf-8") as file:
                generated_log = file.read()
            generated_vec = self.embedding_model(text=generated_log, which_model=self.which_model)
            generated_logs.append((generated_path, generated_vec))

        # Initialize variables to count the accuracy time
        accuracy_count = 0
        accuracy_1_count = 0  # only in rank 1 is considered correct
        for original_path, original_vec in original_logs:
            # Find k similar logs
            similar_logs = self.find_k_similar_logs(original_vec, generated_logs)
            # Get the real similar generated log
            actual_similar_log_path = self.find_actual_similar_log_path(original_log_path=original_path)
            print("--------------------------------------------------")
            print(f"Finding similar logs for {original_path}:")
            for i, (file_path, similarity) in enumerate(similar_logs):
                if Path(file_path).resolve() == actual_similar_log_path:
                    accuracy_count += 1
                    if i == 1:
                        accuracy_1_count += 1
                    print(f"TRUE: included at rank {i + 1} with similarity {similarity:.4f}")
                print(f"Rank {i + 1}: {Path(file_path).name} with similarity {similarity:.4f}")
            print("--------------------------------------------------")
        print("=" * 50)
        print(f"Accuracy rate for client {client_name}:")
        # Calculate the accuracy of having most similar log in top 5
        accuracy_rate = accuracy_count / len(test_paths)
        print(f"Having similar generated log in top 5: {accuracy_rate:.4f}")
        # Calculate the accuracy of having most similar log in top 1
        accuracy_1_rate = accuracy_1_count / len(test_paths)
        print(f"Having similar generated log in top 1: {accuracy_1_rate:.4f}")
        print("=" * 50)

    def google_similarity(self, original_log: str, generated_logs: list[tuple[str, str]]):
        """Find the most similar log in the generated logs.
        Source: https://huggingface.co/blog/embeddinggemma

        Args:
            original_log (str): The original log.
            generated_logs (list[tuple[str, str]]): The list of (file_path, generated log) to compare against.
        """
        # Extract document texts
        documents_0 = [log_text for _, log_text in generated_logs]
        documents = [Document(page_content=text, metadata={"id": i}) for i, text in enumerate(documents_0)]
        # Cosine similarity (dot product because embeddings are normalized)
        vector_store = FAISS.from_documents(documents, self._embedder, distance_strategy="MAX_INNER_PRODUCT")
        results = vector_store.similarity_search_with_score(original_log, k=self.k_value)
        # Sort by similarity descending and take top-k
        similarities = []
        for doc, score in results:
            similarities.append((doc.page_content, score))
        return similarities

    def run_test_for_client_google(self, client_name: str) -> None:
        """Run the test specifically for google model, since it has indepdent functions.

        Args:
            client_name (str): the name of the client whose dataset being tested.
        """
        # Read the list of all test log files and generated test log files
        test_paths = self.collect_all_files_from_folder(f"dataset/train_test_balanced/{client_name}/test")
        generated_log_paths = self.collect_all_files_from_folder(
            f"dataset/train_test_balanced/{client_name}/generate_test_log"
        )
        # Collect all original logs and get their embedding.
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
        accuracy_1_count = 0  # only in rank 1 is considered correct
        for original_path, original_log in original_logs:
            # Find k similar logs
            similar_logs = self.google_similarity(original_log, generated_logs)
            # Get the real similar generated log
            actual_similar_log_path = self.find_actual_similar_log_path(original_log_path=original_path)
            print("--------------------------------------------------")
            print(f"Finding similar logs for {original_path}:")
            for i, (file_path, similarity) in enumerate(similar_logs):
                if Path(file_path).resolve() == actual_similar_log_path:
                    accuracy_count += 1
                    if i == 1:
                        accuracy_1_count += 1
                    print(f"TRUE: included at rank {i + 1} with similarity {similarity:.4f}")
                print(f"Rank {i + 1}: {Path(file_path).name} with similarity {similarity:.4f}")
            print("--------------------------------------------------")
        print("=" * 50)
        print(f"Accuracy rate for client {client_name}:")
        # Calculate the accuracy of having most similar log in top 5
        accuracy_rate = accuracy_count / len(test_paths)
        print(f"Having similar generated log in top 5: {accuracy_rate:.4f}")
        # Calculate the accuracy of having most similar log in top 1
        accuracy_1_rate = accuracy_1_count / len(test_paths)
        print(f"Having similar generated log in top 1: {accuracy_1_rate:.4f}")
        print("=" * 50)

    def run(self):
        if self.which_model == "embeddinggemma-300m":
            for client in self.test_clients:
                self.run_test_for_client_google(client_name=client)
        else:
            for client in self.test_clients:
                self.run_test_for_client(client_name=client)


if __name__ == "__main__":
    test_clients = ["client_1", "client_2", "client_3"]

    # Test self-trained model
    model_path = "models_balanced/10_3_epochs_300_dimensions_5_context_4_negative_0001_learning_rate"
    train_clients = ["client_1", "client_2", "client_3"]
    # self_train_tester = SelfTrainTester(train_clients=train_clients, test_clients=test_clients, model_path=model_path)
    # self_train_tester.run()

    # Test pretrained model ("glove"/ "all-MiniLM-L6-v2" / "fasttext" / "e5-base-v2" / "embeddinggemma-300m")
    pretrained_tester = PreTrainTester(test_clients=test_clients, which_model="fasttext", k=5)
    pretrained_tester.run()
