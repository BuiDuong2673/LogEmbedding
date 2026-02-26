import os
import re
import collections
from collections import defaultdict
from matplotlib import lines
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


class TestResultAnalyzer:
    """Analyze the test results."""
    def __init__(self, result_folder: str) -> None:
        """Initialize TestResultAnalyzer."""
        self.result_folder = result_folder
    
    def get_all_files_in_folder(self) -> list[str]:
        """Get all files in the result folder."""
        # Get all file paths in a folder
        file_paths = [os.path.join(self.result_folder, f) for f in os.listdir(self.result_folder) if os.path.isfile(os.path.join(self.result_folder, f))]
        return file_paths

    def get_ranking_scores(self, file_path: str) -> dict[str, list[float]]:
        score_dict = {"1": 1, "2": 0.8, "3": 0.6, "4": 0.4, "5": 0.2}
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        client_scores = {}
        temp_scores = []
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # Detect each ranking mission
            if line.startswith("Finding similar logs for"):
                j = i + 1
                rank_found = False
                while j < len(lines):
                    l = lines[j].strip()
                    # Detect the end of each ranking mission
                    if l.startswith("----"):
                        break
                    # Read the rank
                    m = re.search(r"TRUE: included at rank\s+(\d+)", l, re.IGNORECASE)
                    if m:
                        rank_num = int(m.group(1))
                        temp_scores.append(score_dict.get(str(rank_num), 0))
                        rank_found = True
                        break
                    j += 1
                if not rank_found:
                    temp_scores.append(0.0)
                i = j  # jump to end of block

            # Detect the end of each client accuracy test
            elif line.startswith("Accuracy rate for client"):
                m = re.search(r"Accuracy rate for client (\S+):", line)
                if m:
                    client = m.group(1)
                    client_scores[client] = temp_scores
                    temp_scores = []
            i += 1
        return client_scores

    def get_each_client_accuracy(self, file_path: str) -> dict[str, tuple[float, float]]:
        """Get the mean accuracy and standard deviation for each client plus the total average."""
        client_accuracies = self.get_ranking_scores(file_path)
        print(f"Client accuracies for {file_path}: {client_accuracies}")
        
        all_scores = []
        processed_results = {}

        # Calculate for each client and collect all scores for the global average
        for client, scores in client_accuracies.items():
            processed_results[client] = (
                float(round(np.mean(scores), 2)), 
                float(round(np.std(scores), 2))
            )
            all_scores.extend(scores)

        # Calculate the global mean and std if there is data
        if all_scores:
            processed_results["All"] = (
                float(round(np.mean(all_scores), 2)), 
                float(round(np.std(all_scores), 2))
            )
        return processed_results
    
    def get_parameters_from_file_name(self, file_name: str) -> tuple[int, int, int, int, int, float]:
        """Read the parameters from the file name in this format.
        [int]_[int]_epochs_[int]_dimensions_[int]_context_[int]_negative_[float]_learning_rate.txt

        Args:
            file_name (str): The name of the file to extract parameters from.

        Returns:
            tuple[int, int, int, int, int, float]: A tuple containing the extracted parameters.
        """

        pattern = r"(\d+)_(\d+)_epochs_(\d+)_dimensions_(\d+)_context_(\d+)_negative_([\d.]+)_learning_rate"
        match = re.match(pattern, file_name)
        if match:
            central_server_epochs = int(match.group(1))
            client_epochs = int(match.group(2))
            embedding_dimension = int(match.group(3))
            context_window_size = int(match.group(4))
            negative_samples = int(match.group(5))
            learning_rate = float(f"0.{match.group(6)}") * 10
            return (
                central_server_epochs,
                client_epochs,
                embedding_dimension,
                context_window_size,
                negative_samples,
                learning_rate
            )
        raise ValueError(f"Invalid file name format: {file_name}")

    def get_ranking_score_for_all_files(self, file_paths: list[str]) -> dict[str, list[float]]:
        """Get the ranking scores for all files."""
        all_scores = {}
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            all_scores[file_name] = self.get_ranking_scores(file_path)
        return all_scores
    
    def get_accuracy_score_for_all_files(self, file_paths: list[str]) -> dict[str, dict[str, tuple[float, float]]]:
        """Get the accuracy scores for all files."""
        all_scores = {}
        pretrained_files = [
            "test_result_balanced/glove.txt",
            "test_result_balanced/all_MiniLM_L6_v2.txt",
            "test_result_balanced/e5-base-v2.txt"
        ]
        for file_path in file_paths:
            file_name = os.path.basename(file_path).replace(".txt", "")
            # If file_name is pretrained model use it as parameter directly
            if file_path in pretrained_files:
                # Get file name except .txt
                all_scores[file_name] = self.get_each_client_accuracy(file_path)
            else:
                # Get the parameters
                parameters = self.get_parameters_from_file_name(file_name)
                all_scores[f"{parameters}"] = self.get_each_client_accuracy(file_path)
        return all_scores
    
    def draw_dimension_experiment(
            self, accuracy_scores: dict[str, dict[str, tuple[float, float]]],
            fixed_central_server_epochs: int=10,
            fixed_client_epochs: int=3,
            fixed_learning_rate: float=0.01,
            fixed_context_window: int=2,
            fixed_negative_samples: int=5,
            possible_dimensions: list[int]=[100, 200, 300]
            ) -> None:
        """Draw the embedding dimension experiment results."""
        # Use a dictionary of lists to store results per client
        client_means = collections.defaultdict(list)
        client_stds = collections.defaultdict(list)

        for dim in possible_dimensions:
            key = (fixed_central_server_epochs, fixed_client_epochs,
                dim, fixed_context_window, fixed_negative_samples, fixed_learning_rate)

            # Ensure you handle the string vs tuple key correctly based on your data
            model_result = accuracy_scores.get(str(key), {})

            for client, (mean, std) in model_result.items():
                client_means[client].append(mean)
                client_stds[client].append(std)

        plt.figure(figsize=(8, 5))

        # Now iterate through each client to plot their specific line
        for client in client_means.keys():
            if client == "All":
                continue
            means = client_means[client]
            stds = client_stds[client]

            # Plot the line
            plt.plot(possible_dimensions, means, marker="o", label=client)

            # Add text labels for each point
            for i, dim in enumerate(possible_dimensions):
                plt.text(dim, means[i], f"{means[i]}±{stds[i]}", 
                        ha="left", va="bottom", fontsize=8)
        
        # Plot the Average accuracy of all clients
        if "All" in client_means:
            all_means = np.array(client_means["All"])
            all_stds = np.array(client_stds["All"])
            
            # Draw the red dashed line
            plt.plot(possible_dimensions, all_means, color='red', linestyle='--', 
                     linewidth=2.5, marker='s', label="Average Accuracy per Client")

            # Add text labels for each point
            for i, dim in enumerate(possible_dimensions):
                plt.text(dim, all_means[i], f"{all_means[i]:.2f}±{all_stds[i]:.2f}", 
                        ha="right", va="bottom", color="red", fontweight='bold', fontsize=9)

        plt.xticks(possible_dimensions)
        plt.legend()

        plt.title("Embedding Dimension Experiment")
        plt.xlabel("Embedding Dimension")
        plt.ylabel("Mean Accuracy")
        # Set y to start at 0 and end at 1
        # plt.ylim(bottom=0, top=1)

        os.makedirs("test_analysis_result", exist_ok=True)
        plt.savefig("test_analysis_result/embedding_dimension_experiment.pdf")
        plt.close()

    def draw_learning_rate_experiment(
            self, accuracy_scores: dict[str, dict[str, tuple[float, float]]],
            fixed_central_server_epochs: int=10,
            fixed_client_epochs: int=3,
            fixed_dimension: int=300,
            fixed_context_window: int=2,
            fixed_negative_samples: int=5,
            possible_learning_rates: list[float]=[0.001, 0.01, 0.1]
            ) -> None:
        """Draw the learning rate experiment results."""
        # Use a dictionary of lists to store results per client
        client_means = collections.defaultdict(list)
        client_stds = collections.defaultdict(list)

        for lr in possible_learning_rates:
            key = (fixed_central_server_epochs, fixed_client_epochs,
                fixed_dimension, fixed_context_window, fixed_negative_samples, lr)
            
            # Ensure you handle the string vs tuple key correctly based on your data
            model_result = accuracy_scores.get(str(key), {}) 
            
            for client, (mean, std) in model_result.items():
                client_means[client].append(mean)
                client_stds[client].append(std)

        plt.figure(figsize=(8, 5))
        
        # Now iterate through each client to plot their specific line
        for client in client_means.keys():
            if client == "All":
                continue
            means = client_means[client]
            stds = client_stds[client]
            
            # Plot the line
            plt.plot(possible_learning_rates, means, marker="o", label=client)
            
            # Add text labels for each point
            for i, lr in enumerate(possible_learning_rates):
                plt.text(lr, means[i], f"{means[i]}±{stds[i]}", 
                        ha="left", va="bottom", fontsize=8)
        
        # Plot the Average accuracy of all clients
        if "All" in client_means:
            all_means = np.array(client_means["All"])
            all_stds = np.array(client_stds["All"])
            
            # Draw the red dashed line
            plt.plot(possible_learning_rates, all_means, color='red', linestyle='--', 
                     linewidth=2.5, marker='s', label="Average Accuracy per Client")

            # Add text labels for each point
            for i, lr in enumerate(possible_learning_rates):
                plt.text(lr, all_means[i], f"{all_means[i]:.2f}±{all_stds[i]:.2f}", 
                        ha="left", va="top", color="red", fontweight='bold', fontsize=8)

        plt.xticks(possible_learning_rates)
        plt.legend()

        plt.title("Learning Rate Experiment")
        plt.xlabel("Learning Rate")
        plt.ylabel("Mean Accuracy")
        # Set y to start at 0 and end at 1
        # plt.ylim(bottom=0, top=1)

        os.makedirs("test_analysis_result", exist_ok=True)
        plt.savefig("test_analysis_result/learning_rate_experiment.pdf")
        plt.close()

    def draw_matrix_experiment(
            self, client: str, accuracy_scores: dict[str, dict[str, tuple[float, float]]],
            fixed_central_server_epochs: int=10,
            fixed_client_epochs: int=3,
            fixed_dimension: int=300,
            possible_context_window: list[int]=[1, 2, 3, 4, 5],
            possible_negative_samples: list[int]=[1, 2, 3, 4, 5],
            fixed_learning_rates: float=0.001
            ) -> None:
        """Draw the matrix experiment results for a specific client or 'All'."""
        
        # 1. Prepare the grid (Contexts on Y-axis, Negatives on X-axis)
        # Reverse contexts so larger values are at the top, or keep as is for 1 at the bottom
        contexts = sorted(possible_context_window, reverse=True)
        negatives = sorted(possible_negative_samples)
        
        grid = np.zeros((len(contexts), len(negatives)))
        # To store std for annotation later
        std_grid = np.zeros((len(contexts), len(negatives)))

        # 2. Fill the grid
        for i, context in enumerate(contexts):
            for j, negative in enumerate(negatives):
                key = (fixed_central_server_epochs, fixed_client_epochs,
                    fixed_dimension, context, negative, fixed_learning_rates)
                
                model_result = accuracy_scores.get(str(key), {})
                mean, std = model_result.get(client, (0.0, 0.0))
                
                grid[i, j] = mean
                std_grid[i, j] = std

        # 3. Plotting
        fig, ax = plt.subplots(figsize=(len(negatives) + 2, len(contexts) + 2))
        cax = ax.matshow(grid, cmap="viridis")

        # Annotate each cell with mean ± std
        for i, context in enumerate(contexts):
            for j, negative in enumerate(negatives):
                mean = grid[i, j]
                std = std_grid[i, j]
                
                if mean > 0:
                    text = f"{mean:.2f}±{std:.2f}"
                    # Dynamic text color for readability
                    if client == "client_1":
                        text_color = "white" if mean <= 0.85 else "black"
                    elif client == "client_2":
                        text_color = "white" if mean <= 0.93 else "black"
                    elif client == "client_3":
                        text_color = "white" if mean <= 0.82 else "black"
                    ax.text(j, i, text, ha="center", va="center", color=text_color, fontweight="bold")
                else:
                    ax.text(j, i, "-", ha="center", va="center", color="white")

        # Add bold black gridlines
        for i in range(len(contexts)):
            for j in range(len(negatives)):
                rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, edgecolor='white', linewidth=2)
                ax.add_patch(rect)

        # Labels and Formatting
        ax.set_xticks(range(len(negatives)))
        ax.set_xticklabels(negatives)
        ax.xaxis.set_label_position('bottom')
        ax.xaxis.tick_bottom()
        
        ax.set_yticks(range(len(contexts)))
        ax.set_yticklabels(contexts)
        
        ax.set_xlabel("Number of Negative Samples (NNS)")
        ax.set_ylabel("Context Window Size (CWS)")

        # Read client index from client_1, _2, _3
        client_index = client.split("_")[-1]
        ax.set_title(f"Client {client_index}'s Accuracy w.r.t CWS and NNS")

        plt.colorbar(cax, label="Mean Accuracy")
        
        # Save
        save_dir = "test_analysis_result"
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(f"{save_dir}/matrix_experiment_{client}.pdf")
        plt.close()
        

def main_balance() -> None:
    """Do statistical analysis of the tests with balanced dataset."""
    analyzer = TestResultAnalyzer("test_result_balanced")
    all_files = analyzer.get_all_files_in_folder()
    # all_scores = analyzer.get_ranking_score_for_all_files(all_files)
    accuracy_scores = analyzer.get_accuracy_score_for_all_files(all_files)
    # analyzer.draw_learning_rate_experiment(accuracy_scores)
    # analyzer.draw_dimension_experiment(accuracy_scores)
    analyzer.draw_matrix_experiment("client_1", accuracy_scores)
    analyzer.draw_matrix_experiment("client_2", accuracy_scores)
    analyzer.draw_matrix_experiment("client_3", accuracy_scores)

if __name__ == "__main__":
    main_balance()

