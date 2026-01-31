"""Experiment with different number of context words to decide which gives best accuracy."""
import os
from pathlib import Path

import numpy as np

from central_server_program import CentralServerProgram
from test.find_similar_log_test import FindSimilarLogTester


class Word2VecExperiment:
    """Experiment with different coefficients of Word2Vec to find out which one work best."""
    def __init__(self):
        """Initialize the Word2VecExperiment."""
        self.client_list = ["maryangel101", "d2klab"]

    def run_context_words_experiment(self, num_possible_context_words: list[int]):
        """Experiment with different number of context words."""
        # Initialize collections of W1 and W2
        W1_list = []
        W2_list = []
        # Create the directory if not exist
        os.makedirs(f"models/context_word_experiment", exist_ok=True)
        # Train the model with each number of context word.
        for num_context in num_possible_context_words:
            # Check if the weight files exist (we trained already)
            W1_path = f"models/context_word_experiment/W1_{num_context}.npy"
            W2_path = f"models/context_word_experiment/W2_{num_context}.npy"
            if Path(W1_path).exists() and Path(W2_path).exists():
                print(f"The model with number of context words {num_context} is already trained. Skipping ...")
                # Read the exist W1, W2
                W1 = np.load(W1_path)
                W2 = np.load(W2_path)
                W1_list.append(W1)
                W2_list.append(W2)
                continue
            central_server = CentralServerProgram()
            W1, W2 = central_server.execute_decentralize_word2vec(num_context_words=num_context)
            # Save the weights
            np.save(W1_path, W1)
            np.save(W2_path, W2)
            W1_list.append(W1)
            W2_list.append(W2)
        # Test the models
        # Initialize collection of accuracy
        accuracy_dict = {}
        for i, num_context in enumerate(num_context_words):
            W1 = W1_list[i]
            W2 = W2_list[i]
            tester = FindSimilarLogTester()
            # Perform your testing here
            accuracy_dict[f"{num_context}"] = []
            for i, client in enumerate(self.client_list):
                accuracy = tester.run_test_for_client(W1, W2, client, model_name="Word2Vec")
                if accuracy == -1.0:
                    print(f"WARNING: The model is not supported.")
                else:
                    accuracy_dict[f"{num_context}"].append((client, accuracy))
        # Visualize the accuracy result
        for num_context, accuracy_list in accuracy_dict.items():
            print("-----------------------------------------------------------")
            print(f"Accuracy result for number of context words: {num_context}")
            for client, accuracy in accuracy_list:
                print(f"Client {client}, Accuracy: {accuracy:.4f}")

    def run_num_epochs_experiment(self, num_possible_epochs: list[int]) -> None:
        """Experiment with different number of epochs."""
        # Initialize collections of W1 and W2
        W1_list = []
        W2_list = []
        # Train the model with each number of epochs.
        for num_epochs in num_possible_epochs:
            central_server = CentralServerProgram()
            W1, W2 = central_server.execute_decentralize_word2vec(num_epochs=num_epochs)
            # Create the directory if not exist
            os.makedirs(f"models/epochs_experiment", exist_ok=True)
            # Save the weights
            np.save(f"models/epochs_experiment/W1_{num_epochs}.npy", W1)
            np.save(f"models/epochs_experiment/W2_{num_epochs}.npy", W2)
            W1_list.append(W1)
            W2_list.append(W2)
        # Test the models
        for i, num_epochs in enumerate(num_possible_epochs):
            W1 = W1_list[i]
            W2 = W2_list[i]
            tester = FindSimilarLogTester()
            # Perform your testing here
            for i, client in enumerate(self.client_list):
                accuracy = tester.run_test_for_client(client, model_name="Word2Vec")
                if accuracy == -1.0:
                    print(f"The model is not supported.")
                else:
                    print(f"Number of Epochs: {num_epochs}, Client {client}, Accuracy: {accuracy:.4f}")

    def run_learning_rate_experiment(self, learning_rates: list[float]) -> None:
        """Experiment with different learning rates."""
        # Initialize collections of W1 and W2
        W1_list = []
        W2_list = []
        # Train the model with each learning rate.
        for lr in learning_rates:
            central_server = CentralServerProgram()
            W1, W2 = central_server.execute_decentralize_word2vec(learning_rate=lr)
            # Create the directory if not exist
            os.makedirs(f"models/learning_rate_experiment", exist_ok=True)
            # Save the weights
            np.save(f"models/learning_rate_experiment/W1_{lr}.npy", W1)
            np.save(f"models/learning_rate_experiment/W2_{lr}.npy", W2)
            W1_list.append(W1)
            W2_list.append(W2)
        # Test the models
        for i, lr in enumerate(learning_rates):
            W1 = W1_list[i]
            W2 = W2_list[i]
            tester = FindSimilarLogTester()
            # Perform your testing here
            for i, client in enumerate(self.client_list):
                accuracy = tester.run_test_for_client(client, model_name="Word2Vec")
                if accuracy == -1.0:
                    print(f"The model is not supported.")
                else:
                    print(f"Learning Rate: {lr}, Client {client}, Accuracy: {accuracy:.4f}")


if __name__ == "__main__":
    # Find best number of context words
    num_context_words = [1, 2]  #[1, 2, 3, 4, 5]
    experiment = Word2VecExperiment()
    experiment.run_context_words_experiment(num_context_words)

    # # Find best number of epochs
    # num_epochs = [30, 50, 70, 90, 100]
    # experiment = Word2VecExperiment()
    # experiment.run_num_epochs_experiment(num_epochs)

    # # Find best learning rate
    # learning_rates = [0.01, 0.05, 0.1, 0.5, 1.0]
    # experiment = Word2VecExperiment()
    # experiment.run_learning_rate_experiment(learning_rates)
