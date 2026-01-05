"""Perform embedding in word-level. Generally known as Word2Vec technique.

Reference:
https://ahammadnafiz.github.io/posts/Word2Vec-From-Scratch-A-Complete-Mathematical-and-Implementation-Guide/
"""
import numpy as np

class Word2Vec:
    """A class performs one-round word-level embedding following negative sampling Word2Vec method."""
    
    def __init__(self, W1: np.array, W2: np.array):
        """Initialize the class.
        
        Args:
            W1 (np.array): embedding matrix to embed words into vectors.
            W2 (np.array): context matrix (weight of the word being in a context).
        """
        # W₁: Input embeddings (V × N) - Xavier initialization
        self.W1 = W1
        # W₂: Output embeddings (N × V) - Xavier initialization  
        self.W2 = W2
    
    def sigmoid(self, x):
        """Numerically stable sigmoid function"""
        x = np.clip(x, -500, 500)  # Prevent overflow
        return 1 / (1 + np.exp(-x))
    
    def train_with_negative_sampling(self, center_idx, context_idx,
                                     negative_samples, learning_rate=0.01):
        """Train using negative sampling (much faster)"""
        
        center_embedding = self.W1[center_idx, :]
        
        # Initialize gradients
        grad_center = np.zeros_like(center_embedding)
        total_loss = 0
        
        # Positive sample: actual context word
        context_vec = self.W2[:, context_idx]
        score = np.dot(center_embedding, context_vec)
        # Clip score to prevent overflow
        score = np.clip(score, -10, 10)
        sigmoid_score = self.sigmoid(score)
        
        # Loss and gradients for positive sample
        loss = -np.log(sigmoid_score + 1e-10)
        grad = (sigmoid_score - 1)  # ∂L/∂score for positive sample
        
        grad_center += grad * context_vec
        self.W2[:, context_idx] -= learning_rate * grad * center_embedding
        total_loss += loss
        
        # Negative samples: random words
        for neg_idx in negative_samples:
            if neg_idx == center_idx or neg_idx == context_idx:
                continue
                
            neg_vec = self.W2[:, neg_idx]
            score = np.dot(center_embedding, neg_vec)
            # Clip score to prevent overflow
            score = np.clip(score, -10, 10)
            sigmoid_score = self.sigmoid(score)
            
            # Loss and gradients for negative sample
            loss = -np.log(1 - sigmoid_score + 1e-10)
            grad = sigmoid_score  # ∂L/∂score for negative sample
            
            grad_center += grad * neg_vec
            self.W2[:, neg_idx] -= learning_rate * grad * center_embedding
            total_loss += loss
        
        # Update center word embedding with gradient clipping
        grad_center = np.clip(grad_center, -1, 1)
        self.W1[center_idx, :] -= learning_rate * grad_center
        
        return total_loss, self.W1, self.W2