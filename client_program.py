"""Handle client tasks."""
import sys
import socket
import numpy as np
from helper.vocab_extractor import VocabExtractor
from helper.network_communication import send_message, receive_message
from embedding_techniques.word2vec import Word2Vec


HOST = "127.0.0.1"
PORT = 5000
NUM_CONTEXT_WORDS = 2


class ClientProgram:
    """Handle client tasks."""
    
    def __init__(self, client_name: str, num_context_words: int):
        """Initialize ClientProgram class.
        
        Args:
            client_name (str): the name of the client.
            num_context_words (int): [EXPERIMENT] the number of words around central word that is considered similar.
        """
        self.client_name = client_name
        self.word_dict = {}
        self.word_indices = []
        self.num_context_words = num_context_words
    
    def get_initial_vocab(self) -> tuple[dict, list]:
        """Get the initial word_dict and word_indices represented by global indices."""
        vocab_extractor = VocabExtractor(client_name=self.client_name)
        word_dict, word_indices = vocab_extractor.get_vocab(num_context_words=self.num_context_words)
        return word_dict, word_indices

    def change_global_indices_to_internal(self, old_word_dict: dict, indice_map: dict) -> dict:
        """Change indices in word_dict to internal common indices.
        
        Args:
            old_word_dict (dict): the old word_dict that established before sending to central server for aggregation.
            indice_map (dict): map between global indices and internal common indices sent from central server.
        """
        new_word_dict = {}  # Store updated word dict
        for word, word_info in old_word_dict.items():
            # First: replace the word's index
            global_word_index = word_info.get("index")
            internal_word_index = indice_map.get(global_word_index)
            if internal_word_index == None:
                print(f"Cannot read common index for word: '{word}', global_index: {global_word_index}")
            # Initialize the item in the new_word_dict
            new_word_dict[word] = {"index": internal_word_index, "freq": word_info.get("freq")}
            # Second: replace the context words' indices
            global_context_word_indices = word_info.get("context_words")
            # Initialize the value in new_word_dict
            new_word_dict[word]["context_words"] = []
            for global_context_index in global_context_word_indices:
                internal_context_index = indice_map.get(global_context_index)
                new_word_dict[word]["context_words"].append(internal_context_index)
        # Get the list of indices of all words
        new_word_indices = list(indice_map.values())
        return new_word_dict, new_word_indices
    
    def train_word2vec(
            self, word_dict, W1: np.array, W2: np.array, num_neg_samples: int=5,
            num_epochs: int=10, learning_rate: float=0.01) -> None:
        """Locally train a Word2Vec embedding model.
        
        Args:
            word_dict (dict): client's word dictionary.
            W1 (np.array): embedding matrix to embed words into vectors.
            W2 (np.array): context matrix (weight of the word being in a context).
            num_neg_samples (int): number of negative samples should we consider.
            num_epochs (int): number of training epochs should we perform.
            learning_rate (float): Learning rate for the optimizer.
        """
        # Initialize word2vec model
        model = Word2Vec(W1, W2)
        # Adjust negative samples if vocabulary is small
        actual_negative_samples = min(num_neg_samples, max(1, len(word_dict) - 2))
        # Training loop
        for epoch in range(num_epochs):
            # Initialize number of pairs
            num_pairs = 0
            total_loss = 0
            for center_word, info in word_dict.items():
                center_idx = info["index"]
                context_idxs = info["context_words"]
                num_pairs += len(context_idxs)
                if actual_negative_samples >= 0:
                    possible_negative_indices = [i for i in range(len(word_dict)) if i != center_idx and i not in context_idxs]
                    if len(possible_negative_indices) >= actual_negative_samples:
                        negative_idx = np.random.choice(
                            possible_negative_indices, 
                            size=actual_negative_samples, 
                            replace=False
                        )
                    else:
                        negative_idx = possible_negative_indices
                else:
                    negative_idx = []
                # Train on this pair
                if len(negative_idx) > 0:
                    for context_idx in context_idxs:
                        loss, W1, W2 = model.train_with_negative_sampling(
                            center_idx, context_idx, negative_idx, learning_rate
                        )
                        total_loss += loss
            avg_loss = total_loss / num_pairs
            print(f"Epoch {epoch + 1}/{num_epochs}, Average Loss: {avg_loss:.4f}")
        return avg_loss, W1, W2
    
    def training(self, num_neg_samples: int=5, num_epochs: int=10, learning_rate: float=0.01) -> None:
        """Run the entire training process from Client side."""
        # Get initial vocab
        initial_word_dict, initial_word_indices = self.get_initial_vocab()
        # Start connecting to central server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            # Send initial vocab to central server for vocab aggregation
            send_message(sock, {
                "type": "VOCAB",
                "client": self.client_name,
                "word indices": initial_word_indices
            })
            # Receive message from central server with map between global indices and internal indices
            msg = receive_message(sock)
            if msg.get("type") != "INITIAL":
                raise ValueError(f"Unexpected message type: {msg.get('type')}, expected INITIAL")
            # Read the initial pretrained variables
            indice_map = msg.get("indice map")
            initial_W1 = np.array(msg.get("W1"))
            initial_W2 = np.array(msg.get("W2"))
            # Update local word dict from using global indices to internal indices
            word_dict, word_indices = self.change_global_indices_to_internal(
                old_word_dict=initial_word_dict, indice_map=indice_map
            )
            # Save the new vocab for later use
            self.word_dict = word_dict
            self.word_indices = word_indices
            # Train word2vec model
            while True:
                _, W1, W2 = self.train_word2vec(
                    word_dict=word_dict,
                    W1=initial_W1,
                    W2=initial_W2,
                    num_neg_samples=num_neg_samples,
                    num_epochs=num_epochs,
                    learning_rate=learning_rate
                )

                # Send weight update to central server
                send_message(sock, {
                    "type": "WEIGHTS",
                    "client": self.client_name,
                    "W1": W1.tolist(),
                    "W2": W2.tolist()
                })

                # Receive aggregated updates from central server
                msg = receive_message(sock)
                if msg["type"] == "FINISH":  # Check if the central server training finish or not
                    print("Training finished.")
                    break
                # Training hasn't finished, update weights with aggregated weights from central server and train again.
                if msg.get("type") == "AGGREGATED_WEIGHTS":
                    W1 = np.array(msg["W1"])
                    W2 = np.array(msg["W2"])
                else:
                    raise ValueError(f"Unexpected message type: {msg.get('type')}, expected AGGREGATED_WEIGHTS")
    
    def internal_index_to_word(self, internal_index: int) -> str:
        """Find the word that is represented by the internal index.
        
        Args:
            internal_index (int): the internal index representation of the word.
        """
        target_word = ""
        for word, word_info in self.word_dict.items():
            if word_info.get("index") == internal_index:
                target_word = word
        return target_word

    def word_to_internal_index(self, word: str) -> int:
        """Find the internal index represention of a word.
        
        Args:
            word (str): the word that we want to find its index.
        """
        # Get all the information of the word
        word_info = self.word_dict.get(word)
        return word_info.get("index")


if __name__ == "__main__":
    # Read the client name from system argument variables.
    if len(sys.argv) < 2:
        raise ValueError("Missing client name. Usage: python client_program.py <client_name>")
    client_name = sys.argv[1]
    # Call ClientProgram class to handle the traning process
    client_program = ClientProgram(client_name=client_name, num_context_words=NUM_CONTEXT_WORDS)
    client_program.training()
