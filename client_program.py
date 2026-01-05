"""Manage client actions."""
import json
import numpy as np
from helper.vocab_extractor import VocabExtractor
from embedding_techniques.word2vec import Word2Vec


class ClientProgram:
    """Client program to manage local vocabulary."""
    def __init__(self, client_name: str):
        """Initialize the ClientProgram."""
        self.client_name = client_name
        # Extract the vocab.
        self.vocab_extractor = VocabExtractor(client_name=self.client_name)
        self.word_dict, self.words_indices = self.vocab_extractor.get_vocab()

    def get_client_global_vocab(self):
        """Provide client's globally known words to the central server."""
        # Save the word_dict to a json file
        file_path = f"dataset/{self.client_name}_word_dict.json"
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(self.word_dict, file, ensure_ascii=False, indent=4)
        print(f"Saved {self.client_name} vocab into {file_path}.")
        # Visualize the data information
        print(f"Client {self.client_name}:")
        known_word_indices = []
        unknown_word_indices = []
        for index in self.words_indices:
            if index.startswith("unk_"):
                unknown_word_indices.append(index)
            else:
                known_word_indices.append(index)
        print(f"Num known words: {len(known_word_indices)}")
        print(f"Num unknown words: {len(unknown_word_indices)}")
        return self.words_indices

    def change_to_internal_common_indices(self, indices_dict: dict) -> dict:
        """Change the initial global indices to internal indices.
        
        Args:
            indices_dict (dict): the dictionary map global indices to internal common indices.
        """
        new_word_dict = {}
        for word, word_info in self.word_dict.items():
            # First: replace the word's index
            global_word_index = word_info.get("index")
            common_word_index = indices_dict.get(global_word_index)
            if common_word_index == None:
                print(f"Cannot read common index for word: '{word}', global_index: {global_word_index}")
            # Initialize the item in the new_word_dict
            new_word_dict[word] = {"index": common_word_index, "freq": word_info.get("freq")}
            # Second: replace the context words' indices
            global_context_word_indices = word_info.get("context_words")
            # Initialize the value in new_word_dict
            new_word_dict[word]["context_words"] = []
            for global_context_index in global_context_word_indices:
                common_context_index = indices_dict.get(global_context_index)
                new_word_dict[word]["context_words"].append(common_context_index)
        # Save the new_word_dict to a json file
        with open(f"dataset/{self.client_name}_new_word_dict.json", "w", encoding="utf-8") as json_file:
            json.dump(new_word_dict, json_file, ensure_ascii=False, indent=4)
        print(f"Save the vocab to path: dataset/{self.client_name}_new_word_dict.json")
        # Update the class values
        self.word_dict = new_word_dict
        self.words_indices = list(indices_dict.values())
        return new_word_dict
    
    def generate_training_pairs(self) -> list[tuple[int, int]]:
        """Add all pairs of center words, context words into a list."""
        training_pairs = []
        for center_word, center_word_info in self.word_dict.items():
            context_words = center_word_info.get("context_words")
            for context_word in context_words:
                training_pairs.append((center_word, context_word))
        return training_pairs
    
    def perform_word2vec_embedding(self, W1: np.array, W2: np.array, num_neg_samples: int=5, num_epochs: int=10,
                                   learning_rate: float=0.01):
        """Perform one round Word2Vec embedding.
        
        Args:
            W1 (np.array): embedding matrix to embed words into vectors.
            W2 (np.array): context matrix (weight of the word being in a context).
            num_neg_samples (int): number of negative samples should we consider.
            num_epochs (int): number of training epochs should we perform.
            learning_rate (float): Learning rate for the optimizer.
        """
        # Initialize word2vec model
        model = Word2Vec(W1, W2)
        # Adjust negative samples if vocabulary is small
        actual_negative_samples = min(num_neg_samples, max(1, len(self.word_dict) - 2))
        # Training loop
        for epoch in range(num_epochs):
            # Initialize number of pairs
            num_pairs = 0
            total_loss = 0
            for center_word, info in self.word_dict.items():
                center_idx = info["index"]
                context_idxs = info["context_words"]
                num_pairs += len(context_idxs)
                if actual_negative_samples >= 0:
                    possible_negative_indices = [i for i in range(len(self.word_dict)) if i != center_idx and i not in context_idxs]
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


