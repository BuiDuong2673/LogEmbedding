import json
import numpy as np

class Tester:
    def __init__(self):
        """Initialize the class."""
        self.W1 = np.load("models/W1.npy")
        self.W2 = np.load("models/W2.npy")
        with open("dataset/internal_central_vocab.json", "r", encoding="utf-8") as file:
            self.full_vocab = json.load(file)
        with open("dataset/global_vocab_index.json", "r", encoding="utf-8") as file:
            self.global_vocab = json.load(file)
    
    def test_analogy(
        self, center_word: str, pos_sample_word: str, neg_sample_word: str, top_k=3):
        """Test analogy: a is to b as c is to ?"""
        # Get indices representation of the words
        for word, global_idx in self.global_vocab.items():
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
        center_embedding = self.W1[center_idx, :]
        pos_sample_embedding = self.W1[pos_sample_idx, :]  
        neg_sample_embedding = self.W1[neg_sample_idx, :]

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
    
    def find_similar_words(self, word: str, top_k: int=10) -> None:
        """Find k similar words."""
        for global_word, global_idx in self.global_vocab.items():
            if global_word == word:
                word_idx = self.full_vocab.get(f"{global_idx}")
        similarities = []
        word_embedding = self.W1[word_idx, :]
        # Cosine similarity: cos(θ) = (a·b)/(|a||b|)
        norm_word = np.linalg.norm(word_embedding)
        for _, internal_idx in self.full_vocab.items():
            if internal_idx == word_idx:
                continue
            other_word_embedding = self.W1[internal_idx, :]
            norm_other_word = np.linalg.norm(other_word_embedding)
            if norm_word > 0 and norm_other_word > 0:
                cosine_sim = np.dot(word_embedding, other_word_embedding) / (norm_word * norm_other_word)
            else:
                cosine_sim = 0
            similarities.append((cosine_sim, internal_idx))
        # Sort by similarity (descending)
        similarities.sort(reverse=True)
        print(f"\nWords most similar to '{word}':")
        for i, (sim, similar_word_idx) in enumerate(similarities[:top_k]):
            similar_word = None
            for global_idx_str, internal_idx in self.full_vocab.items():
                if similar_word_idx == internal_idx:
                    for global_word, global_word_idx in self.global_vocab.items():
                        if global_idx_str == f"{global_word_idx}":
                            similar_word = global_word
                            break
                    if similar_word != None:
                        break
            print(f"{i+1}. '{similar_word}' (similarity: {sim:.3f})")


if __name__ == "__main__":
    tester = Tester()
    # Test anology
    tester.test_analogy("error", "value", "success")
    print()
    tester.test_analogy("error", "runtime", "success")
    # Find similar words
    tester.find_similar_words("failed", 5)
    