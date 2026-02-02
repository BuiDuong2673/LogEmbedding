"""Analyze collected test results."""
import re
from collections import Counter


class TestResultAnalysis:
    """Analyze collected test results."""
    
    def __init__(self):
        """Initialize TestResultAnalysis class."""
        pass

    def true_rank_distribution_single_file(self, file_path: str, max_rank: int = 5) -> dict:
        """
        Reads one log file and returns the distribution of TRUE ranks (1..max_rank).

        Returns:
            dict {rank: count}
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


if __name__ == "__main__":
    file_list = [
        "test_result/2_clients_1_context_50_5_epochs.txt",
        "test_result/2_clients_2_context_10_5_epochs.txt",
        "test_result/2_clients_2_context_50_5_epochs_01_learning_rate.txt",
        "test_result/2_clients_2_context_50_5_epochs_0001_learning_rate.txt",
        "test_result/2_clients_2_context_50_5_epochs.txt",
        "test_result/2_clients_2_context_100_5_epochs.txt",
        "test_result/2_clients_3_context_50_5_epochs.txt",
        "test_result/2_clients_4_context_50_5_epochs.txt",
        "test_result/2_clients_5_context_50_5_epochs.txt",
        "test_result/sentence_transformer.txt"
    ]

    analysis = TestResultAnalysis()

    for file in file_list:
        dist = analysis.true_rank_distribution_single_file(file_path=file)
        print(f"{file}: {dist}")