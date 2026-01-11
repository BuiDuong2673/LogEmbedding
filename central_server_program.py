"""Manage central server actions."""
import json
import os
import numpy as np
from helper.global_vocab_processor import GlobalVocabProcessor
from client_program import ClientProgram

class CentralServerProgram:
    """Central server program to manage global vocabulary."""
    def __init__(self):
        """Initialize the CentralServerProgram."""
        self.global_vocab_processor = GlobalVocabProcessor()
        # Read the vocab if not read yet
        self.vocab_global_index = self.global_vocab_processor.get_global_vocab()
        # Define client list
        self.client_list = ["maryangel101", "d2klab"]
        # Initialize full vocab
        self.full_vocab = {}
        # Initialize onehot embedding
        self.onehot_embedding = {}
        # Initialize the dictionary to store client vocab
        self.client_vocab = {}

    def get_all_client_vocabs(self):
        """Get the vocabulary for each client."""
        full_vocab = {}
        reserved_index = 0
        for client in self.client_list:
            # Call the client program to get its vocab's global indices
            client_program = ClientProgram(client_name=client)
            word_indices = client_program.get_client_global_vocab()
            # Store client vocab in class variable
            self.client_vocab[client] = word_indices
            # Store all words with their internal common index
            for index in word_indices:
                if index.startswith("unk_"):
                    # If the word is not globally known, we have to add the client's name to it
                    full_vocab[f"{client}_{index}"] = reserved_index
                    reserved_index += 1
                else:
                    if index not in full_vocab:
                        full_vocab[index] = reserved_index
                        reserved_index += 1
        self.full_vocab = full_vocab
        # Save full internal vocab to JSON
        with open("dataset/internal_central_vocab.json", "w", encoding="utf-8") as json_file:
            json.dump(self.full_vocab, json_file, ensure_ascii=False, indent=4)
        print(f"Save the vocab to path: dataset/internal_central_vocab.json")
        return self.full_vocab
    
    def send_common_indices_to_client(self, client_name: str, client_program: ClientProgram):
        """Send each client the common indices for their words."""
        indices_dict = {}
        client_old_word_indices = self.client_vocab[client_name]
        for old_index in client_old_word_indices:
            # Retrieve the new index in full_vocab
            if old_index.startswith("unk_"):
                # If it is unknown words, then add client name in front
                new_index = self.full_vocab.get(f"{client_name}_{old_index}")
            else:
                new_index = self.full_vocab.get(old_index)
            indices_dict[old_index] = new_index
        # Update client word dict with new indices
        client_program.change_to_internal_common_indices(indices_dict)
    
    def execute_decentralize_word2vec(
        self,
        embedding_dim: int = 500,
        num_neg_samples: int = 5,
        num_epochs: int = 50,
        learning_rate: float = 0.01,
    ):
        """Perform a decentralize word2vec embedding model training."""
        # Prepare a common vocab which contains indices for all clients' words.
        _ = self.get_all_client_vocabs()
        # Initialize W1, W2
        vocab_size = len(self.full_vocab)
        # W₁: Input embeddings (V × N) - Xavier initialization
        W1 = np.random.normal(0, 0.1, (vocab_size, embedding_dim))
        # W₂: Output embeddings (N × V) - Xavier initialization  
        W2 = np.random.normal(0, 0.1, (embedding_dim, vocab_size))
        for epoch in range(num_epochs):
            client_W1_list = []
            client_W2_list = []
            # Update clients' word dict with common vocab
            for client in self.client_list:
                client_program = ClientProgram(client_name=client)
                _ = self.send_common_indices_to_client(client_name=client, client_program=client_program)
                client_avg_loss, client_W1, client_W2 = client_program.perform_word2vec_embedding(
                    W1=W1.copy(), W2=W2.copy(), num_neg_samples=num_neg_samples, num_epochs=5,
                    learning_rate=learning_rate)
                client_W1_list.append(client_W1)
                client_W2_list.append(client_W2)
                print("----------------------------------------------------------------")
                print(f"Epoch: {epoch} Client {client} average loss: {client_avg_loss}.")
                print("----------------------------------------------------------------")
            W1 = np.mean(client_W1_list, axis=0)
            W2 = np.mean(client_W2_list, axis=0)
        return W1, W2

    def execute_decentralize_doc2vec(
        self,
        embedding_dim: int = 500,
        sentence_window: int = 5,
        failure_keywords: list[str] | None = None,
        num_neg_samples: int = 5,
        num_epochs: int = 1,
        learning_rate: float = 0.01,
        max_docs_per_client: int | None = None,
    ):
        """Decentralized Doc2Vec (PV-DBOW) training.

        Aggregates only the shared word output matrix W (dim × vocab_size).
        Keeps per-client document vectors D locally (document IDs are client-local).
        """
        _ = self.get_all_client_vocabs()
        vocab_size = len(self.full_vocab)
        W = np.random.normal(0, 0.1, (embedding_dim, vocab_size))

        # Reuse client instances so D can be carried between rounds
        client_programs: dict[str, ClientProgram] = {
            client: ClientProgram(client_name=client) for client in self.client_list
        }
        client_doc_vectors: dict[str, np.ndarray | None] = {client: None for client in self.client_list}
        client_doc_centers: dict[str, list[int] | None] = {client: None for client in self.client_list}

        # Send common indices once per client (avoid repeated JSON writes each epoch)
        for client in self.client_list:
            _ = self.send_common_indices_to_client(client_name=client, client_program=client_programs[client])

        if failure_keywords is None:
            failure_keywords = [
                "fail",
                "failed",
                "failure",
                "error",
                "exception",
                "fatal",
                "panic",
                "traceback",
            ]

        for epoch in range(num_epochs):
            client_W_list: list[np.ndarray] = []
            for client in self.client_list:
                client_program = client_programs[client]
                client_avg_loss, client_D, client_W = client_program.perform_doc2vec_embedding(
                    W=W.copy(),
                    embedding_dim=embedding_dim,
                    sentence_window=sentence_window,
                    failure_keywords=failure_keywords,
                    only_failure_windows=True,
                    num_neg_samples=num_neg_samples,
                    num_epochs=5,
                    learning_rate=learning_rate,
                    max_docs=max_docs_per_client,
                    D=client_doc_vectors[client],
                )
                client_doc_vectors[client] = client_D
                client_doc_centers[client] = client_program.last_doc_centers
                client_W_list.append(client_W)

                print("----------------------------------------------------------------")
                print(f"Epoch: {epoch} Client {client} Doc2Vec average loss: {client_avg_loss}.")
                print("----------------------------------------------------------------")

            W = np.mean(client_W_list, axis=0)

        return W, client_doc_vectors, client_doc_centers
    
    def test_analogy(
            self, W1: np.array, W2: np.array, center_word: str, pos_sample_word: str, neg_sample_word: str, top_k=3):
        """Test analogy: a is to b as c is to ?"""
        # Get indices representation of the words
        # Read global vocab
        with open("dataset/global_vocab_index.json", "r", encoding="utf-8") as file:
            global_vocab = json.load(file)
        for word, global_idx in global_vocab.items():
            if word == center_word:
                center_idx = self.full_vocab.get(f"{global_idx}")
            elif word == pos_sample_word:
                pos_sample_idx = self.full_vocab.get(f"{global_idx}")
            elif word == neg_sample_word:
                neg_sample_idx = self.full_vocab.get(f"{global_idx}")
            else:
                continue
        if center_idx == None or pos_sample_idx == None or neg_sample_idx == None:
            print(f"Error: cannot perform test because some words not found. center_idx = {center_idx},"
                  f"pos_sample_idx = {pos_sample_idx} and neg_sample_idx = {neg_sample_idx}")
            return
        
        # Get embeddings
        center_embedding = W1[center_idx, :]
        pos_sample_embedding = W1[pos_sample_idx, :]  
        neg_sample_embedding = W1[neg_sample_idx, :]

        norm_center = np.linalg.norm(center_embedding)
        norm_pos = np.linalg.norm(pos_sample_embedding)
        norm_neg = np.linalg.norm(neg_sample_embedding)

        if norm_center > 0 and norm_pos > 0 and norm_neg > 0:
            cosine_sim_pos = np.dot(center_embedding, pos_sample_embedding) / (norm_center * norm_pos)
            cosine_sim_neg = np.dot(center_embedding, neg_sample_embedding) / (norm_center * norm_neg)
        else:
            cosine_sim_pos, cosine_sim_neg = 0, 0
        
        print(f"Cosine_sim between {center_word} and {pos_sample_word} is: {cosine_sim_pos}")
        print(f"Cosine_sim between {center_word} and {neg_sample_word} is: {cosine_sim_neg}")





if __name__ == "__main__":
    central_server_program = CentralServerProgram()

    mode = os.getenv("EMBEDDING_MODE", "doc2vec").strip().lower()
    os.makedirs("models", exist_ok=True)

    if mode == "doc2vec":
        W, client_doc_vectors, client_doc_centers = central_server_program.execute_decentralize_doc2vec(
            sentence_window=5,
        )
        np.save("models/doc2vec_W.npy", W)
        for client, D in client_doc_vectors.items():
            if D is None:
                continue
            np.save(f"models/doc2vec_{client}_D.npy", D)
        with open("models/doc2vec_failure_centers.json", "w", encoding="utf-8") as f:
            json.dump(client_doc_centers, f, ensure_ascii=False, indent=2)
        print("Saved Doc2Vec models to models/doc2vec_W.npy and models/doc2vec_<client>_D.npy")
    else:
        W1, W2 = central_server_program.execute_decentralize_word2vec()
        np.save("models/W1.npy", W1)
        np.save("models/W2.npy", W2)

        center_word = "error"
        pos_word = "runtime"
        neg_word = "success"
        central_server_program.test_analogy(
            W1, W2, center_word=center_word, pos_sample_word=pos_word, neg_sample_word=neg_word
        )