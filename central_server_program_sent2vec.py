"""Example script to run Sent2Vec FL training."""
import sys
import os
import numpy as np
from central_server_program import CentralServerProgram

if __name__ == "__main__":
    # sys.stdout = open('output_sent2vec.txt', 'w', encoding='utf-8')
    central_server_program = CentralServerProgram()

    # Execute Sent2Vec FL training
    W1, W2 = central_server_program.execute_decentralize_sent2vec(
        embedding_dim=500,
        num_neg_samples=5,
        num_epochs=5,
        learning_rate=0.01,
        word_ngrams=2,
        dropout_k=2,
        bucket_size=2000000,
        window_size=1
    )
    
    # Save W1, W2 for testing
    os.makedirs("models", exist_ok=True)
    np.save("models/W1_sent2vec.npy", W1)
    np.save("models/W2_sent2vec.npy", W2)
    
    print("\nSent2Vec FL training completed!")
    print(f"W1 shape: {W1.shape}")
    print(f"W2 shape: {W2.shape}")
    
    # sys.stdout.close()
