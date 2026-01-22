"""Manage central server actions."""
import json
import os
import numpy as np
from helper.global_vocab_processor import GlobalVocabProcessor
from client_program import ClientProgram


NUM_CONTEXT_WORDS = 2


class CentralServerProgram:
    """Central server program to manage global vocabulary."""
    def __init__(self):
        """Initialize the CentralServerProgram."""
        self.global_vocab_processor = GlobalVocabProcessor()
        # Read the vocab if not read yet
        self.vocab_global_index = self.global_vocab_processor.get_global_vocab()
        # Define client list
        self.client_list = ["maryangel101", "d2klab"]
        # Get clients' unknown words
        client_unknown_sets = []
        for client in self.client_list:
            client_program = ClientProgram(client_name=client)
            unknown_words = client_program.get_client_unknown_words()
            client_unknown_sets.append(set(unknown_words))
        # Add client common unknown words to the global vocab
        common_unknown_words = set.intersection(*client_unknown_sets)
        self.global_vocab_processor.add_common_words_to_global_vocab(common_unknown_words)
        # Initialize full vocab
        self.full_vocab = {}
        # Initialize onehot embedding
        self.onehot_embedding = {}
        # Initialize the dictionary to store client vocab
        self.client_vocab = {}


    def get_all_client_vocabs(self, num_context_words: int=NUM_CONTEXT_WORDS):
        """Get the vocabulary for each client."""
        full_vocab = {}
        reserved_index = 0
        for client in self.client_list:
            # Call the client program to get its vocab's global indices
            client_program = ClientProgram(client_name=client, num_context_words=num_context_words)
            _, word_indices = client_program.get_client_global_vocab()
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
        new_word_dict = client_program.change_to_internal_common_indices(indices_dict)
        return new_word_dict
    
    def execute_decentralize_word2vec(self, embedding_dim: int=500, num_neg_samples: int=5, num_epochs: int=50,
                                      learning_rate: float=0.01, num_context_words: int=NUM_CONTEXT_WORDS):
        """Perform a decentralize word2vec embedding model training."""
        # Prepare a common vocab which contains indices for all clients' words.
        _ = self.get_all_client_vocabs(num_context_words=num_context_words)
        # Initialize W1, W2
        vocab_size = len(self.full_vocab)
        # W₁: Input embeddings (V × N) - Xavier initialization
        W1 = np.random.normal(0, 0.1, (vocab_size, embedding_dim))
        # W₂: Output embeddings (N × V) - Xavier initialization  
        W2 = np.random.normal(0, 0.1, (embedding_dim, vocab_size))
        client_W1_list = []
        client_W2_list = []
        for epoch in range(num_epochs):
            # Update clients' word dict with common vocab
            for client in self.client_list:
                client_program = ClientProgram(client_name=client, num_context_words=num_context_words)
                word_dict = self.send_common_indices_to_client(client_name=client, client_program=client_program)
                client_avg_loss, client_W1, client_W2 = client_program.perform_word2vec_embedding(
                    word_dict=word_dict, W1=W1.copy(), W2=W2.copy(), num_neg_samples=num_neg_samples, num_epochs=5,
                    learning_rate=learning_rate)
                client_W1_list.append(client_W1)
                client_W2_list.append(client_W2)
                print("----------------------------------------------------------------")
                print(f"Epoch: {epoch} Client {client} average loss: {client_avg_loss}.")
                print("----------------------------------------------------------------")
            W1 = np.mean(client_W1_list, axis=0)
            W2 = np.mean(client_W2_list, axis=0)
        # Delete new_word_dict.json file
        for client in self.client_list:
            file_path = f"dataset/{client}_new_word_dict.json"
            if os.path.exists(file_path):
                os.remove(file_path)
        return W1, W2


if __name__ == "__main__":
    central_server_program = CentralServerProgram()

    W1, W2 = central_server_program.execute_decentralize_word2vec()
    # Save W1, W2 for testing
    os.makedirs("models", exist_ok=True)

    np.save("models/W1_word2vec.npy", W1)
    np.save("models/W2_word2vec.npy", W2)