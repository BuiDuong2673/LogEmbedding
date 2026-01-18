"""Manage client actions."""
import json
import re
import numpy as np
from helper.vocab_extractor import VocabExtractor
from embedding_techniques.word2vec import Word2Vec
from embedding_techniques.sent2vec import Sent2Vec


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
    
    def load_sentences_as_word_indices(self) -> list[list[int]]:
        """Load sentences from dataset and convert them to word index lists.
        
        This method should be called after change_to_internal_common_indices() 
        to ensure word_dict uses common indices.
        
        Returns:
            list[list[int]]: List of sentences, each sentence is a list of word indices.
        """
        # Load raw log lines
        log_lines = self.vocab_extractor.load_client_dataset()
        # Delete timestamps
        log_lines = self.vocab_extractor.delete_time_stamp(log_lines)
        
        sentences = []
        for line in log_lines:
            # Split on spaces, underscores, hyphens
            parts = re.split(r'[\s_-]+', line)
            # Split camelCase
            words = []
            for part in parts:
                split_camel = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', part)
                words.extend(split_camel)
            
            # Convert words to indices
            word_indices = []
            for word in words:
                if word in self.word_dict:
                    word_idx = self.word_dict[word]["index"]
                    # Handle both int and string indices
                    if isinstance(word_idx, (int, np.integer)):
                        word_indices.append(int(word_idx))
                    elif isinstance(word_idx, str):
                        # Try to convert string to int
                        try:
                            word_indices.append(int(word_idx))
                        except (ValueError, TypeError):
                            # Skip if cannot convert (e.g., "unk_123" format)
                            continue
            
            # Only add non-empty sentences
            if len(word_indices) > 0:
                sentences.append(word_indices)
        
        return sentences
    
    def generate_sentence_pairs(self, sentences: list[list[int]], window_size: int = 1) -> list[tuple[list[int], list[int]]]:
        """Generate sentence pairs for training Sent2Vec.
        
        Args:
            sentences (list[list[int]]): List of sentences as word index lists.
            window_size (int): Number of surrounding sentences to consider as context.
        
        Returns:
            list[tuple[list[int], list[int]]]: List of (sentence, context_sentence) pairs.
        """
        training_pairs = []
        
        for i, sentence in enumerate(sentences):
            # Get context sentences within window
            start_idx = max(0, i - window_size)
            end_idx = min(len(sentences), i + window_size + 1)
            
            for j in range(start_idx, end_idx):
                if j != i:
                    context_sentence = sentences[j]
                    training_pairs.append((sentence, context_sentence))
        
        return training_pairs
    
    def perform_sent2vec_embedding(self, W1: np.array, W2: np.array, num_neg_samples: int=5, 
                                   num_epochs: int=10, learning_rate: float=0.01,
                                   word_ngrams: int=2, dropout_k: int=2, bucket_size: int=2000000,
                                   window_size: int=1):
        """Perform one round Sent2Vec embedding.
        
        Args:
            W1 (np.array): embedding matrix to embed words and n-grams into vectors.
            W2 (np.array): context matrix (weight of the sentence being in a context).
            num_neg_samples (int): number of negative samples should we consider.
            num_epochs (int): number of training epochs should we perform.
            learning_rate (float): Learning rate for the optimizer.
            word_ngrams (int): max length of word n-gram [default: 2].
            dropout_k (int): number of n-grams dropped when training [default: 2].
            bucket_size (int): number of hash buckets for n-gram vocabulary [default: 2000000].
            window_size (int): number of surrounding sentences to consider as context [default: 2].
        """
        # Initialize Sent2Vec model
        model = Sent2Vec(W1, W2, word_ngrams=word_ngrams, dropout_k=dropout_k, bucket_size=bucket_size)
        
        # Load sentences as word index lists
        sentences = self.load_sentences_as_word_indices()
        if len(sentences) == 0:
            print(f"Warning: No sentences found for client {self.client_name}")
            return 0.0, W1, W2
        
        # Generate sentence pairs
        training_pairs = self.generate_sentence_pairs(sentences, window_size=window_size)
        
        if len(training_pairs) == 0:
            print(f"Warning: No training pairs generated for client {self.client_name}")
            return 0.0, W1, W2
        
        # Adjust negative samples
        actual_negative_samples = min(num_neg_samples, max(1, len(sentences) - 2))
        
        # Training loop
        for epoch in range(num_epochs):
            total_loss = 0
            num_pairs = 0
            
            for sentence_indices, context_sentence_indices in training_pairs:
                # Generate negative samples (random sentences)
                negative_samples = []
                if actual_negative_samples > 0:
                    # Select random sentences as negative samples
                    possible_negative_sentences = [
                        s for s in sentences 
                        if s != sentence_indices and s != context_sentence_indices
                    ]
                    if len(possible_negative_sentences) >= actual_negative_samples:
                        negative_indices = np.random.choice(
                            len(possible_negative_sentences),
                            size=actual_negative_samples,
                            replace=False
                        )
                        negative_samples = [possible_negative_sentences[i] for i in negative_indices]
                    else:
                        negative_samples = possible_negative_sentences
                
                # Train on this pair
                if len(negative_samples) > 0:
                    loss, W1, W2 = model.train_with_negative_sampling(
                        sentence_indices,
                        context_sentence_indices,
                        negative_samples,
                        learning_rate
                    )
                    total_loss += loss
                    num_pairs += 1
            
            avg_loss = total_loss / num_pairs if num_pairs > 0 else 0.0
            print(f"Epoch {epoch + 1}/{num_epochs}, Average Loss: {avg_loss:.4f}, Pairs: {num_pairs}")
        
        return avg_loss, W1, W2


