"""Analyze collected test results."""
import re
from collections import Counter, defaultdict
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


class TestResultAnalysis:
    """Analyze collected test results."""
    
    def __init__(self):
        """Initialize TestResultAnalysis class."""
        pass

    def get_rank_distribution(self, file_path: str, max_rank: int = 5) -> dict:
        """
        Reads one test result file and returns the distribution of TRUE ranks (1..max_rank).

        Args:
            file_path (str): the path to the test result file.
        """

        true_rank_pattern = re.compile(r"TRUE:.*rank\s+(\d+)", re.IGNORECASE)
        distribution = Counter({rank: 0 for rank in range(1, max_rank + 1)})

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                match = true_rank_pattern.search(line)
                if match:
                    rank = int(match.group(1))
                    if 1 <= rank <= max_rank:
                        distribution[rank] += 1

        return dict(distribution)

    def compute_client_accuracy(self, file_path: str):
        """
        Parse a test result file and compute weighted accuracy per client.
        
        Args:
            file_path (str): the path to the test result file.
        """
        rank_score = {1: 1.0, 2: 0.8, 3: 0.6, 4: 0.4, 5: 0.2,}
        client_scores = defaultdict(list)

        current_client = None

        # Regex patterns
        client_pattern = re.compile(
            r"dataset/train_test_internal/([^/]+)/test/"
        )
        true_pattern = re.compile(
            r"TRUE: included at rank (\d+)"
        )

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                # Detect client
                client_match = client_pattern.search(line)
                if client_match:
                    current_client = client_match.group(1)
                    continue

                # Detect TRUE rank
                true_match = true_pattern.search(line)
                if true_match and current_client is not None:
                    rank = int(true_match.group(1))
                    score = rank_score.get(rank, 0.0)
                    client_scores[current_client].append(score)

        # Compute average accuracy per client
        client_accuracy = {
            client: sum(scores) / len(scores)
            for client, scores in client_scores.items()
            if scores
        }

        return client_accuracy
    
    def compare_learning_rate(self) -> None:
        """Compare the performance of the system across different learning rate."""
        # Define the path to the test result of different learning rate
        learning_rate_dict = {
            "0.001": "test_result_2/2_clients_2_context_50_5_epochs_0001_learning_rate.txt",
            "0.01": "test_result_2/2_clients_2_context_50_5_epochs.txt",
            "0.1": "test_result_2/2_clients_2_context_50_5_epochs_01_learning_rate.txt"
        }
        # Prepare list of accuracies across learning rates for each client to plot
        client_results = {}
        # Get the score of these file
        for learning_rate, result_path in learning_rate_dict.items():
            client_accuracies = self.compute_client_accuracy(file_path=result_path)
            for client, acc in client_accuracies.items():
                if client not in client_results:
                    client_results[client] = []
                client_results[client].append(acc)
        
        learning_rates = [float(lr) for lr in learning_rate_dict.keys()]
        # Plot the result
        plt.figure(figsize=(8, 5))

        for client, accuracies in client_results.items():
            plt.plot(
                learning_rates,
                accuracies,
                marker="o",
                label=client
            )

        plt.xlabel("Learning Rate")
        plt.ylabel("Accuracy Score")
        plt.title("Learning Rate Comparision")
        plt.legend()
        plt.xscale("log")
        plt.xticks(learning_rates, labels=[str(lr) for lr in learning_rates])
        plt.tight_layout()

        output_file = Path("test_analysis_result") / "learning_rate_comparision"
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Plot saved to: {output_file}")
    
    def compare_num_context(self) -> None:
        """Compare the accuracy score across different number of context words."""
        num_context_dict = {
            "1": "test_result_2/2_clients_1_context_50_5_epochs_001_learning_rate_5_neg.txt",
            "2": "test_result_2/2_clients_2_context_50_5_epochs.txt",
            "3": "test_result_2/2_clients_3_context_50_5_epochs.txt",
            "4": "test_result_2/2_clients_4_context_50_5_epochs.txt",
            "5": "test_result_2/2_clients_5_context_50_5_epochs.txt"
        }
        # Prepare list of accuracies across learning rates for each client to plot
        client_results = {}
        # Get the score of these file
        for num_words, result_path in num_context_dict.items():
            client_accuracies = self.compute_client_accuracy(file_path=result_path)
            for client, acc in client_accuracies.items():
                if client not in client_results:
                    client_results[client] = []
                client_results[client].append(acc)
        
        num_contexts = [float(nc) for nc in num_context_dict.keys()]
        # Plot the result
        plt.figure(figsize=(8, 5))

        for client, accuracies in client_results.items():
            plt.plot(
                num_contexts,
                accuracies,
                marker="o",
                label=client
            )

        plt.xlabel("Number of Context Words")
        plt.ylabel("Accuracy Score")
        plt.title("Number of Context Words Comparision")
        plt.legend()
        plt.xscale("log")
        plt.xticks(num_contexts, labels=[str(nc) for nc in num_contexts])
        plt.tight_layout()

        output_file = Path("test_analysis_result") / "num_context_comparision"
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Plot saved to: {output_file}")

    def compare_num_neg_sample(self) -> None:
        """Compare the accuracy scores across different number of negative samples."""
        num_neg_dict = {
            "1": "test_result_2/2_clients_2_context_50_5_epochs_1_neg.txt",
            "2": "test_result_2/2_clients_2_context_50_5_epochs_2_neg.txt",
            "3": "test_result_2/2_clients_2_context_50_5_epochs_3_neg.txt",
            "4": "test_result_2/2_clients_2_context_50_5_epochs_4_neg.txt",
            "5": "test_result_2/2_clients_2_context_50_5_epochs.txt"
        }
        # Prepare list of accuracies across learning rates for each client to plot
        client_results = {}
        # Get the score of these file
        for num_words, result_path in num_neg_dict.items():
            client_accuracies = self.compute_client_accuracy(file_path=result_path)
            for client, acc in client_accuracies.items():
                if client not in client_results:
                    client_results[client] = []
                client_results[client].append(acc)
        
        num_neg = [float(nn) for nn in num_neg_dict.keys()]
        # Plot the result
        plt.figure(figsize=(8, 5))

        for client, accuracies in client_results.items():
            plt.plot(
                num_neg,
                accuracies,
                marker="o",
                label=client
            )

        plt.xlabel("Number of Negative Samples")
        plt.ylabel("Accuracy Score")
        plt.title("Number of Negative Samples Comparision")
        plt.legend()
        plt.xscale("log")
        plt.xticks(num_neg, labels=[str(nc) for nc in num_neg])
        plt.tight_layout()

        output_file = Path("test_analysis_result") / "num_neg_comparision"
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Plot saved to: {output_file}")
    
    def compare_num_epochs(self) -> None:
        """Compare accuracy scores across different number of epochs."""
        num_epoch_dict = {
            "10": "test_result_2/2_clients_2_context_10_5_epochs_001_learning_rate_5_neg.txt",
            "30": "test_result_2/2_clients_2_context_30_5_epochs_001_learning_rate_5_neg.txt",
            "50": "test_result_2/2_clients_2_context_50_5_epochs.txt",
            "70": "test_result_2/2_clients_2_context_70_5_epochs_001_learning_rate_5_neg.txt",
            "100": "test_result_2/2_clients_2_context_100_5_epochs.txt"
        }
        # Prepare list of accuracies across learning rates for each client to plot
        client_results = {}
        # Get the score of these file
        for num_epoch, result_path in num_epoch_dict.items():
            client_accuracies = self.compute_client_accuracy(file_path=result_path)
            for client, acc in client_accuracies.items():
                if client not in client_results:
                    client_results[client] = []
                client_results[client].append(acc)
        
        num_epochs= [float(ne) for ne in num_epoch_dict.keys()]
        # Plot the result
        plt.figure(figsize=(8, 5))

        for client, accuracies in client_results.items():
            plt.plot(
                num_epochs,
                accuracies,
                marker="o",
                label=client
            )

        plt.xlabel("Number of Epochs in Central Server")
        plt.ylabel("Accuracy Score")
        plt.title("Number of Epochs Comparision")
        plt.legend()
        plt.xscale("log")
        plt.xticks(num_epochs, labels=[str(ne) for ne in num_epochs])
        plt.tight_layout()

        output_file = Path("test_analysis_result") / "num_epoch_comparision"
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Plot saved to: {output_file}")
    
    def compare_num_clients(self) -> None:
        """Compare the accuracy score when have logsage and when dont have logsage."""
        client_dict = {
            "2": "test_result_2/2_clients_2_context_10_5_epochs_001_learning_rate_5_neg.txt",
            "3": "test_result_2/3_clients_2_context_10_5_epochs.txt"
        }
        # Collect results
        client_results = {}
        num_clients_list = sorted([int(k) for k in client_dict.keys()])

        for num_client, result_path in client_dict.items():
            client_accuracies = self.compute_client_accuracy(file_path=result_path)
            for client, acc in client_accuracies.items():
                if client not in client_results:
                    client_results[client] = []
                client_results[client].append(acc)

        # Prepare x positions
        clients = list(client_results.keys())
        x = np.arange(len(clients))  # one position per client
        num_bars = len(num_clients_list)
        bar_width = 0.3 / num_bars  # thinner bars

        plt.figure(figsize=(8, 5))

        for i, num_client in enumerate(num_clients_list):
            # extract i-th accuracy for each client
            accuracies = [client_results[client][i] for client in clients]
            plt.bar(
                x + i * bar_width,
                accuracies,
                width=bar_width,
                label=f"{num_client} clients"
            )

        plt.xlabel("Client's Test Data")
        plt.ylabel("Accuracy Score")
        plt.title("Number of Clients Comparision")
        plt.xticks(x + bar_width * (num_bars - 1) / 2, clients)
        plt.legend()
        plt.tight_layout()

        output_file = Path("test_analysis_result") / "num_client_comparision"
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Plot saved to: {output_file}")
    
    def compare_models(self) -> None:
        """Compare the self-trained model with pretrained models accuracy scores."""
        model_dict = {
            "Self-trained": "test_result_2/2_clients_2_context_50_5_epochs.txt",
            "all-MiniLM-L6-v2": "test_result_2/all_MiniLM_L6_v2.txt",
            "Glove": "test_result_2/glove.txt"
        }
        # Collect results
        client_results = {}
        model_list = [k for k in model_dict.keys()]

        for model_name, result_path in model_dict.items():
            model_accuracies = self.compute_client_accuracy(file_path=result_path)
            for client, acc in model_accuracies.items():
                if client not in client_results:
                    client_results[client] = []
                client_results[client].append(acc)

        # Prepare x positions
        clients = list(client_results.keys())
        x = np.arange(len(clients))  # one position per client
        num_bars = len(model_list)
        bar_width = 0.3 / num_bars  # thinner bars

        plt.figure(figsize=(8, 5))

        for i, model in enumerate(model_list):
            # extract i-th accuracy for each client
            accuracies = [client_results[client][i] for client in clients]
            plt.bar(
                x + i * bar_width,
                accuracies,
                width=bar_width,
                label=f"{model}"
            )

        plt.xlabel("Client's Test Data")
        plt.ylabel("Accuracy Score")
        plt.title("Self-trained vs Pre-trained Models Comparision")
        plt.xticks(x + bar_width * (num_bars - 1) / 2, clients)
        plt.legend()
        plt.tight_layout()

        output_file = Path("test_analysis_result") / "model_comparision"
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Plot saved to: {output_file}")




def get_all_file_paths(folder_path: str) -> list[str]:
    return [
        str(path)
        for path in Path(folder_path).rglob("*")
        if path.is_file()
    ]


if __name__ == "__main__":
    file_list = get_all_file_paths("test_result_2")

    analysis = TestResultAnalysis()

    # for file in file_list:
    #     dist = analysis.get_rank_distribution(file_path=file)
    #     print(f"{file}: {dist}")
    
    # for file in file_list:
    #     print("-" * 50)
    #     print(f"File: {file}")
    #     client_scores = analysis.compute_client_accuracy(file_path=file)
    #     for client, score in client_scores.items():
    #         print(f"Client: {client}. Score: {score:.4f}")
    #     print("-" * 50)
    
    # analysis.compare_learning_rate()
    # analysis.compare_num_context()
    # analysis.compare_num_neg_sample()
    # analysis.compare_num_epochs()
    analysis.compare_num_clients()
    analysis.compare_models()