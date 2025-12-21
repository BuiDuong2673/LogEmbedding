"""Log embedding using Doc2Vec."""
import os
import json
import pickle
from typing import List, Dict, Tuple, Optional
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import simple_preprocess


class LogEmbedder:
    """Train and use Doc2Vec embeddings for log templates."""
    
    def __init__(self, vector_size: int = 128, window: int = 5, 
                 min_count: int = 1, epochs: int = 20, dm: int = 1):
        """Initialize the LogEmbedder.
        
        Args:
            vector_size (int): Dimensionality of the feature vectors. Default 128.
            window (int): Maximum distance between current and predicted word. Default 5.
            min_count (int): Ignores all words with frequency lower than this. Default 1.
            epochs (int): Number of iterations (epochs) over the corpus. Default 20.
            dm (int): Training algorithm: 1 for PV-DM, 0 for PV-DBOW. Default 1 (DM).
        """
        self.vector_size = vector_size
        self.window = window
        self.min_count = min_count
        self.epochs = epochs
        self.dm = dm
        
        self.model = None
        self.templates = {}
        self.cluster_to_label = {}
        
    def preprocess_text(self, text: str) -> List[str]:
        """Preprocess text by tokenizing and cleaning.
        
        Args:
            text (str): Input text (log template).
            
        Returns:
            List[str]: List of tokens.
        """
        # Use gensim's simple_preprocess for tokenization
        # It lowercases, removes punctuation, and splits
        tokens = simple_preprocess(text, deacc=True)
        return tokens
    
    def load_templates_from_json(self, template_file: str, label: Optional[str] = None) -> List[TaggedDocument]:
        """Load templates from JSON file and prepare for Doc2Vec training.
        
        Args:
            template_file (str): Path to the template JSON file.
            label (Optional[str]): Label for this set of templates (e.g., 'pass' or 'fail').
            
        Returns:
            List[TaggedDocument]: List of tagged documents for Doc2Vec.
        """
        with open(template_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        templates = data.get('templates', {})
        tagged_docs = []
        
        for cluster_id, template_data in templates.items():
            template_text = template_data['template']
            count = template_data['count']
            
            # Preprocess the template
            tokens = self.preprocess_text(template_text)
            
            # Create tag: client_clusterID or client_label_clusterID
            if label:
                tag = f"{label}_{cluster_id}"
                self.cluster_to_label[int(cluster_id)] = label
            else:
                tag = str(cluster_id)
            
            # Create TaggedDocument
            # Replicate based on frequency (optional: can weight differently)
            tagged_doc = TaggedDocument(words=tokens, tags=[tag])
            tagged_docs.append(tagged_doc)
            
            # Store template info
            self.templates[tag] = {
                'template': template_text,
                'count': count,
                'tokens': tokens
            }
        
        print(f"Loaded {len(tagged_docs)} templates from {template_file}")
        return tagged_docs
    
    def load_templates_with_labels(self, base_dir: str, client_name: str) -> Tuple[List[TaggedDocument], Dict]:
        """Load templates from pass/fail directories with labels.
        
        Args:
            base_dir (str): Base directory containing template files.
            client_name (str): Name of the client.
            
        Returns:
            Tuple[List[TaggedDocument], Dict]: Tagged documents and statistics.
        """
        all_docs = []
        stats = {'pass': 0, 'fail': 0}
        
        # Check if we have pass/fail subdirectories
        pass_file = os.path.join(base_dir, f"{client_name}_pass_templates.json")
        fail_file = os.path.join(base_dir, f"{client_name}_fail_templates.json")
        
        if os.path.exists(pass_file):
            docs = self.load_templates_from_json(pass_file, label='pass')
            all_docs.extend(docs)
            stats['pass'] = len(docs)
        
        if os.path.exists(fail_file):
            docs = self.load_templates_from_json(fail_file, label='fail')
            all_docs.extend(docs)
            stats['fail'] = len(docs)
        
        # If no labeled data, load from single file
        if not all_docs:
            single_file = os.path.join(base_dir, f"{client_name}_templates.json")
            if os.path.exists(single_file):
                docs = self.load_templates_from_json(single_file, label=None)
                all_docs.extend(docs)
                stats['unlabeled'] = len(docs)
        
        return all_docs, stats
    
    def train(self, tagged_documents: List[TaggedDocument], workers: int = 4):
        """Train the Doc2Vec model.
        
        Args:
            tagged_documents (List[TaggedDocument]): Training documents.
            workers (int): Number of worker threads. Default 4.
        """
        print(f"\nTraining Doc2Vec model...")
        print(f"  Vector size: {self.vector_size}")
        print(f"  Window: {self.window}")
        print(f"  Min count: {self.min_count}")
        print(f"  Epochs: {self.epochs}")
        print(f"  Algorithm: {'PV-DM' if self.dm else 'PV-DBOW'}")
        print(f"  Documents: {len(tagged_documents)}")
        
        # Initialize model
        self.model = Doc2Vec(
            vector_size=self.vector_size,
            window=self.window,
            min_count=self.min_count,
            workers=workers,
            epochs=self.epochs,
            dm=self.dm
        )
        
        # Build vocabulary
        print("Building vocabulary...")
        self.model.build_vocab(tagged_documents)
        print(f"Vocabulary size: {len(self.model.wv)}")
        
        # Train model
        print(f"Training for {self.epochs} epochs...")
        self.model.train(
            tagged_documents,
            total_examples=self.model.corpus_count,
            epochs=self.model.epochs
        )
        
        print("✓ Training completed!")
    
    def infer_vector(self, text: str, epochs: int = 20) -> np.ndarray:
        """Infer vector for a new log message.
        
        Args:
            text (str): Log message or template.
            epochs (int): Number of inference epochs. Default 20.
            
        Returns:
            np.ndarray: Embedding vector.
        """
        if self.model is None:
            raise ValueError("Model not trained yet. Call train() first.")
        
        tokens = self.preprocess_text(text)
        vector = self.model.infer_vector(tokens, epochs=epochs)
        return vector
    
    def get_similar_templates(self, text: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """Find similar templates to a given log message.
        
        Args:
            text (str): Input log message.
            top_k (int): Number of similar templates to return. Default 5.
            
        Returns:
            List[Tuple[str, float]]: List of (template, similarity_score) tuples.
        """
        if self.model is None:
            raise ValueError("Model not trained yet. Call train() first.")
        
        # Infer vector for input
        vector = self.infer_vector(text)
        
        # Find most similar document vectors
        similar_docs = self.model.dv.most_similar([vector], topn=top_k)
        
        results = []
        for doc_tag, similarity in similar_docs:
            if doc_tag in self.templates:
                template_text = self.templates[doc_tag]['template']
                results.append((template_text, similarity, doc_tag))
            else:
                results.append((doc_tag, similarity, doc_tag))
        
        return results
    
    def get_all_embeddings(self) -> Dict[str, np.ndarray]:
        """Get embeddings for all trained templates.
        
        Returns:
            Dict[str, np.ndarray]: Dictionary mapping template tags to vectors.
        """
        if self.model is None:
            raise ValueError("Model not trained yet. Call train() first.")
        
        embeddings = {}
        for tag in self.templates.keys():
            embeddings[tag] = self.model.dv[tag]
        
        return embeddings
    
    def save(self, model_dir: str):
        """Save the model and metadata.
        
        Args:
            model_dir (str): Directory to save the model.
        """
        os.makedirs(model_dir, exist_ok=True)
        
        # Save Doc2Vec model
        model_path = os.path.join(model_dir, "doc2vec.model")
        self.model.save(model_path)
        print(f"✓ Saved Doc2Vec model to {model_path}")
        
        # Save metadata
        metadata = {
            'vector_size': self.vector_size,
            'window': self.window,
            'min_count': self.min_count,
            'epochs': self.epochs,
            'dm': self.dm,
            'templates': self.templates,
            'cluster_to_label': self.cluster_to_label
        }
        
        metadata_path = os.path.join(model_dir, "metadata.pkl")
        with open(metadata_path, 'wb') as f:
            pickle.dump(metadata, f)
        print(f"✓ Saved metadata to {metadata_path}")
        
        # Save config as JSON for easy inspection
        config = {
            'vector_size': self.vector_size,
            'window': self.window,
            'min_count': self.min_count,
            'epochs': self.epochs,
            'dm': self.dm,
            'num_templates': len(self.templates),
            'vocabulary_size': len(self.model.wv) if self.model else 0
        }
        
        config_path = os.path.join(model_dir, "config.json")
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        print(f"✓ Saved config to {config_path}")
    
    def load(self, model_dir: str):
        """Load a trained model.
        
        Args:
            model_dir (str): Directory containing the saved model.
        """
        # Load Doc2Vec model
        model_path = os.path.join(model_dir, "doc2vec.model")
        self.model = Doc2Vec.load(model_path)
        print(f"✓ Loaded Doc2Vec model from {model_path}")
        
        # Load metadata
        metadata_path = os.path.join(model_dir, "metadata.pkl")
        with open(metadata_path, 'rb') as f:
            metadata = pickle.load(f)
        
        self.vector_size = metadata['vector_size']
        self.window = metadata['window']
        self.min_count = metadata['min_count']
        self.epochs = metadata['epochs']
        self.dm = metadata['dm']
        self.templates = metadata['templates']
        self.cluster_to_label = metadata.get('cluster_to_label', {})
        
        print(f"✓ Loaded metadata from {metadata_path}")
        print(f"  Templates: {len(self.templates)}")
        print(f"  Vector size: {self.vector_size}")


def train_client_embedder(client_name: str, template_dir: str = "dataset/templates",
                          output_dir: str = "models/checkpoints", 
                          vector_size: int = 128, epochs: int = 20) -> LogEmbedder:
    """Train Doc2Vec embedder for a specific client.
    
    Args:
        client_name (str): Name of the client.
        template_dir (str): Directory containing template files.
        output_dir (str): Directory to save the trained model.
        vector_size (int): Embedding dimension.
        epochs (int): Number of training epochs.
        
    Returns:
        LogEmbedder: Trained embedder.
    """
    print(f"\n{'='*60}")
    print(f"Training Doc2Vec for client: {client_name}")
    print(f"{'='*60}\n")
    
    # Initialize embedder
    embedder = LogEmbedder(vector_size=vector_size, epochs=epochs)
    
    # Load templates
    tagged_docs, stats = embedder.load_templates_with_labels(template_dir, client_name)
    
    print(f"\nDataset statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value} templates")
    
    # Train
    embedder.train(tagged_docs)
    
    # Save model
    model_path = os.path.join(output_dir, client_name)
    embedder.save(model_path)
    
    return embedder


if __name__ == "__main__":
    # Train embedder for maryangel101
    embedder = train_client_embedder(
        client_name="maryangel101",
        vector_size=128,
        epochs=20
    )
    
    # Test inference
    print(f"\n{'='*60}")
    print("Testing inference on sample logs:")
    print(f"{'='*60}\n")
    
    test_logs = [
        "/usr/bin/tar: Cannot mkdir: No such file or directory",
        "Done in 0.79s.",
        "Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec"
    ]
    
    for log in test_logs:
        print(f"\nLog: {log}")
        similar = embedder.get_similar_templates(log, top_k=3)
        print("Top 3 similar templates:")
        for i, (template, score, tag) in enumerate(similar, 1):
            print(f"  {i}. [Score: {score:.3f}] {template[:80]}...")
