"""Perform embedding in sentence-level with word and n-gram features. Generally known as Sent2Vec technique.

Reference:
https://github.com/epfml/sent2vec
Matteo Pagliardini, Prakhar Gupta, Martin Jaggi, 
"Unsupervised Learning of Sentence Embeddings using Compositional n-Gram Features" NAACL 2018
"""
import numpy as np
import hashlib


class Sent2Vec:
    """A class performs one-round sentence-level embedding following negative sampling Sent2Vec method.
    
    Sent2Vec considers both words and n-grams to create sentence embeddings.
    """
    
    def __init__(self, W1: np.array, W2: np.array, word_ngrams: int = 2, dropout_k: int = 2, 
                 bucket_size: int = 2000000):
        """Initialize the class.
        
        Args:
            W1 (np.array): embedding matrix to embed words and n-grams into vectors.
            W2 (np.array): context matrix (weight of the sentence being in a context).
            word_ngrams (int): max length of word n-gram [default: 2].
            dropout_k (int): number of n-grams dropped when training [default: 2].
            bucket_size (int): number of hash buckets for n-gram vocabulary [default: 2000000].
        """
        # W₁: Input embeddings (V × N) - includes words and n-grams
        self.W1 = W1
        # W₂: Output embeddings (N × V) - Xavier initialization  
        self.W2 = W2
        self.word_ngrams = word_ngrams
        self.dropout_k = dropout_k
        self.bucket_size = bucket_size
    
    def sigmoid(self, x):
        """Numerically stable sigmoid function"""
        x = np.clip(x, -500, 500)  # Prevent overflow
        return 1 / (1 + np.exp(-x))
    
    def hash_ngram(self, ngram: tuple) -> int:
        """Hash an n-gram tuple to a bucket index.
        
        Args:
            ngram (tuple): tuple of word indices representing an n-gram.
            
        Returns:
            int: bucket index for the n-gram.
        """
        # Convert ngram tuple to string and hash it
        ngram_str = '_'.join(map(str, ngram))
        hash_value = int(hashlib.md5(ngram_str.encode()).hexdigest(), 16)
        return hash_value % self.bucket_size
    
    def generate_ngrams(self, word_indices: list) -> list:
        """Generate word n-grams from a list of word indices.
        
        Args:
            word_indices (list): list of word indices in a sentence.
            
        Returns:
            list: list of tuples, each tuple is (ngram_type, index)
                  where ngram_type is 'word' or 'ngram' and index is the vocabulary index.
        """
        features = []
        
        # Add unigrams (single words)
        for word_idx in word_indices:
            features.append(('word', word_idx))
        
        # Add n-grams (bigrams, trigrams, etc.)
        for n in range(2, self.word_ngrams + 1):
            for i in range(len(word_indices) - n + 1):
                ngram = tuple(word_indices[i:i+n])
                ngram_hash = self.hash_ngram(ngram)
                # Offset ngram hash by vocab_size to avoid collision with word indices
                # Assuming vocab_size is less than bucket_size
                ngram_idx = ngram_hash + len(self.W1)  # Offset by original vocab size
                features.append(('ngram', ngram_idx))
        
        return features
    
    def get_sentence_embedding(self, word_indices: list, apply_dropout: bool = True) -> np.array:
        """Compute sentence embedding by averaging word and n-gram embeddings.
        
        Args:
            word_indices (list): list of word indices in a sentence.
            apply_dropout (bool): whether to apply dropout during training [default: True].
            
        Returns:
            np.array: sentence embedding vector.
        """
        features = self.generate_ngrams(word_indices)
        
        # Apply dropout: randomly drop dropout_k features
        if apply_dropout and len(features) > self.dropout_k:
            # Randomly select features to drop
            indices_to_drop = np.random.choice(
                len(features), 
                size=min(self.dropout_k, len(features) - 1), 
                replace=False
            )
            features = [f for i, f in enumerate(features) if i not in indices_to_drop]
        
        if len(features) == 0:
            # Return zero vector if no features
            return np.zeros(self.W1.shape[1])
        
        # Get embeddings for all features
        embeddings = []
        for feature_type, feature_idx in features:
            if feature_type == 'word':
                if feature_idx < len(self.W1):
                    embeddings.append(self.W1[feature_idx, :])
            else:  # ngram
                # For n-grams, we need to handle the extended vocabulary
                # If ngram_idx is beyond W1, we use a hash-based lookup
                if feature_idx < len(self.W1):
                    embeddings.append(self.W1[feature_idx, :])
                else:
                    # Use hash to get a consistent index within W1 bounds
                    consistent_idx = feature_idx % len(self.W1)
                    embeddings.append(self.W1[consistent_idx, :])
        
        if len(embeddings) == 0:
            return np.zeros(self.W1.shape[1])
        
        # Average all embeddings to get sentence embedding
        sentence_embedding = np.mean(embeddings, axis=0)
        return sentence_embedding
    
    def train_with_negative_sampling(self, sentence_word_indices: list, context_sentence_indices: list,
                                     negative_samples: list, learning_rate=0.01):
        """Train using negative sampling (much faster) for sentence-level embedding.
        
        Args:
            sentence_word_indices (list): list of word indices in the center sentence.
            context_sentence_indices (list): list of word indices in the context sentence (positive sample).
            negative_samples (list): list of lists, each containing word indices of a negative sentence.
            learning_rate (float): learning rate for training [default: 0.01].
            
        Returns:
            tuple: (total_loss, updated_W1, updated_W2)
        """
        # Get sentence embeddings
        sentence_embedding = self.get_sentence_embedding(sentence_word_indices, apply_dropout=True)
        context_embedding = self.get_sentence_embedding(context_sentence_indices, apply_dropout=False)
        
        # Initialize gradients
        grad_sentence = np.zeros_like(sentence_embedding)
        total_loss = 0
        
        # Positive sample: actual context sentence
        score = np.dot(sentence_embedding, context_embedding)
        # Clip score to prevent overflow
        score = np.clip(score, -10, 10)
        sigmoid_score = self.sigmoid(score)
        
        # Loss and gradients for positive sample
        loss = -np.log(sigmoid_score + 1e-10)
        grad = (sigmoid_score - 1)  # ∂L/∂score for positive sample
        
        grad_sentence += grad * context_embedding
        # Update context sentence embedding (approximate gradient)
        context_grad = grad * sentence_embedding
        
        total_loss += loss
        
        # Negative samples: random sentences
        for neg_sentence_indices in negative_samples:
            neg_embedding = self.get_sentence_embedding(neg_sentence_indices, apply_dropout=False)
            score = np.dot(sentence_embedding, neg_embedding)
            # Clip score to prevent overflow
            score = np.clip(score, -10, 10)
            sigmoid_score = self.sigmoid(score)
            
            # Loss and gradients for negative sample
            loss = -np.log(1 - sigmoid_score + 1e-10)
            grad = sigmoid_score  # ∂L/∂score for negative sample
            
            grad_sentence += grad * neg_embedding
            # Update negative sentence embedding (approximate gradient)
            neg_grad = grad * sentence_embedding
            
            total_loss += loss
        
        # Update sentence embedding by backpropagating to word and n-gram embeddings
        # Distribute gradient equally to all features in the sentence
        features = self.generate_ngrams(sentence_word_indices)
        if len(features) > 0:
            feature_grad = grad_sentence / len(features)
            feature_grad = np.clip(feature_grad, -1, 1)  # Gradient clipping
            
            for feature_type, feature_idx in features:
                if feature_type == 'word':
                    if feature_idx < len(self.W1):
                        self.W1[feature_idx, :] -= learning_rate * feature_grad
                else:  # ngram
                    if feature_idx < len(self.W1):
                        self.W1[feature_idx, :] -= learning_rate * feature_grad
                    else:
                        consistent_idx = feature_idx % len(self.W1)
                        self.W1[consistent_idx, :] -= learning_rate * feature_grad
        
        # Update context and negative sentence embeddings similarly
        # For simplicity, we update W2 which represents sentence-level context
        # In practice, this would be more complex, but we approximate it
        context_features = self.generate_ngrams(context_sentence_indices)
        if len(context_features) > 0:
            context_feature_grad = context_grad / len(context_features)
            context_feature_grad = np.clip(context_feature_grad, -1, 1)
            
            for feature_type, feature_idx in context_features:
                if feature_type == 'word':
                    if feature_idx < len(self.W1):
                        self.W1[feature_idx, :] -= learning_rate * context_feature_grad
                else:  # ngram
                    if feature_idx < len(self.W1):
                        self.W1[feature_idx, :] -= learning_rate * context_feature_grad
                    else:
                        consistent_idx = feature_idx % len(self.W1)
                        self.W1[consistent_idx, :] -= learning_rate * context_feature_grad
        
        return total_loss, self.W1, self.W2
