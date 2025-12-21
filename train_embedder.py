"""Training and evaluation script for log embeddings."""
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.log_embedder import LogEmbedder, train_client_embedder


def train_and_save():
    """Train Doc2Vec model and save it."""
    print("\n" + "="*70)
    print("PHASE 2: Training Doc2Vec Embedding Model")
    print("="*70)
    
    
    # Train for maryangel101
    embedder = train_client_embedder(
        client_name="maryangel101",
        template_dir="dataset/templates",
        output_dir="models/checkpoints",
        vector_size=128,
        epochs=20
    )
    
    return embedder


def test_inference(embedder: LogEmbedder):
    """Test the trained model on sample logs."""
    print(f"\n{'='*70}")
    print("Testing Inference & Template Matching")
    print(f"{'='*70}\n")
    
    # Sample test logs (new variations)
    test_logs = [
        "/usr/bin/tar: node_modules: Cannot mkdir: No such file or directory",
        "Done in 1.5s.",
        "Received 8388608 of 1274821257 (0.7%), 8.0 MBs/sec",
        "warning Resolution field is incompatible",
        "Wrote a Flow config to /home/runner/work/test/.flowconfig",
        "Complete job name: Build React",
        "[command]/usr/bin/tar -xf cache.tzst"
    ]
    
    for i, log in enumerate(test_logs, 1):
        print(f"\n{i}. Input Log:")
        print(f"   {log}")
        
        # Get similar templates
        similar = embedder.get_similar_templates(log, top_k=3)
        
        print(f"   Top 3 Similar Templates:")
        for j, (template, score, tag) in enumerate(similar, 1):
            # Truncate long templates
            display_template = template[:70] + "..." if len(template) > 70 else template
            print(f"      {j}. [Similarity: {score:.3f}] {display_template}")


def analyze_embeddings(embedder: LogEmbedder):
    """Analyze the learned embeddings."""
    print(f"\n{'='*70}")
    print("Embedding Analysis")
    print(f"{'='*70}\n")
    
    # Get all embeddings
    embeddings = embedder.get_all_embeddings()
    
    print(f"Total templates: {len(embeddings)}")
    print(f"Embedding dimension: {embedder.vector_size}")
    
    # Convert to matrix
    tags = list(embeddings.keys())
    vectors = np.array([embeddings[tag] for tag in tags])
    
    # Compute statistics
    print(f"\nEmbedding Statistics:")
    print(f"  Mean norm: {np.mean(np.linalg.norm(vectors, axis=1)):.3f}")
    print(f"  Std norm: {np.std(np.linalg.norm(vectors, axis=1)):.3f}")
    
    # Compute pairwise similarities
    similarities = cosine_similarity(vectors)
    
    # Exclude diagonal (self-similarity)
    np.fill_diagonal(similarities, -1)
    
    print(f"\nPairwise Similarity Statistics:")
    print(f"  Mean similarity: {np.mean(similarities[similarities > -1]):.3f}")
    print(f"  Max similarity: {np.max(similarities):.3f}")
    print(f"  Min similarity: {np.min(similarities[similarities > -1]):.3f}")
    
    # Find most similar pairs
    print(f"\nMost Similar Template Pairs:")
    flat_idx = np.argsort(similarities.flatten())[-5:][::-1]
    
    for idx in flat_idx:
        i, j = np.unravel_index(idx, similarities.shape)
        sim = similarities[i, j]
        
        tag1, tag2 = tags[i], tags[j]
        template1 = embedder.templates[tag1]['template']
        template2 = embedder.templates[tag2]['template']
        
        print(f"\n  Similarity: {sim:.3f}")
        print(f"    1. {template1[:60]}...")
        print(f"    2. {template2[:60]}...")
    
    return vectors, tags


def visualize_embeddings(embedder: LogEmbedder, output_path: str = "models/tsne_visualization.png"):
    """Visualize embeddings using t-SNE."""
    print(f"\n{'='*70}")
    print("Visualizing Embeddings with t-SNE")
    print(f"{'='*70}\n")
    
    # Get all embeddings
    embeddings = embedder.get_all_embeddings()
    tags = list(embeddings.keys())
    vectors = np.array([embeddings[tag] for tag in tags])
    
    print(f"Running t-SNE on {len(vectors)} templates...")
    
    # Run t-SNE
    tsne = TSNE(n_components=2, random_state=42, perplexity=min(30, len(vectors)-1))
    vectors_2d = tsne.fit_transform(vectors)
    
    # Prepare colors based on labels (if available)
    colors = []
    for tag in tags:
        if 'pass' in tag:
            colors.append('green')
        elif 'fail' in tag:
            colors.append('red')
        else:
            colors.append('blue')
    
    # Plot
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1], 
                         c=colors, alpha=0.6, s=50)
    
    # Add legend if we have labels
    if 'pass' in ''.join(tags) or 'fail' in ''.join(tags):
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='green', alpha=0.6, label='Pass'),
            Patch(facecolor='red', alpha=0.6, label='Fail')
        ]
        plt.legend(handles=legend_elements, loc='best')
    
    plt.title('t-SNE Visualization of Log Template Embeddings', fontsize=14)
    plt.xlabel('t-SNE Dimension 1')
    plt.ylabel('t-SNE Dimension 2')
    plt.grid(True, alpha=0.3)
    
    # Save
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"✓ Saved visualization to {output_path}")
    
    # Also show top templates in different regions
    print(f"\nSample templates in different regions:")
    
    # Find templates at extremes
    indices = {
        'top-right': np.argmax(vectors_2d[:, 0] + vectors_2d[:, 1]),
        'top-left': np.argmax(-vectors_2d[:, 0] + vectors_2d[:, 1]),
        'bottom-right': np.argmax(vectors_2d[:, 0] - vectors_2d[:, 1]),
        'bottom-left': np.argmax(-vectors_2d[:, 0] - vectors_2d[:, 1])
    }
    
    for region, idx in indices.items():
        tag = tags[idx]
        template = embedder.templates[tag]['template']
        print(f"\n  {region.upper()}:")
        print(f"    {template[:70]}...")


def evaluate_model():
    """Full evaluation pipeline."""
    # Train
    embedder = train_and_save()
    
    # Test inference
    test_inference(embedder)
    
    # Analyze embeddings
    analyze_embeddings(embedder)
    
    # Visualize
    try:
        visualize_embeddings(embedder)
    except Exception as e:
        print(f"\nWarning: Could not create visualization: {e}")
        print("This is optional and doesn't affect the model.")
    
    print(f"\n{'='*70}")
    print("✓ Phase 2 Completed Successfully!")
    print("✓ Model saved to: models/checkpoints/maryangel101/")
    print("="*70 + "\n")


if __name__ == "__main__":
    evaluate_model()
