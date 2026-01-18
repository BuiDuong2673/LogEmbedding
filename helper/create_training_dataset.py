"""Create a training dataset that filtering out unrelated log lines."""
import os
import re


CLIENT_LIST = ["d2klab", "maryangel101"]
NUM_CONTEXT_LINE = 5


class TrainingDatasetCreator:
    """A class to create a training dataset."""
    def __init__(self, client_list: list[str]=CLIENT_LIST) -> None:
        """Initialize the TrainingDatasetCreator."""
        self.client_list = client_list

    def get_file_list_from_folder(self, folder_path: str) -> list[str]:
        """Load the file list from a folder given the path.

        Args:
            folder_path (str): The path to the folder to load files from.

        Returns:
            list[str]: A list of file paths.
        """
        dataset_paths = []
        for subdir in os.listdir(folder_path):
            full_path = os.path.join(folder_path, subdir)

            if os.path.isdir(full_path):
                dataset_paths.append(full_path)

        file_path_list = []
        for dataset_path in dataset_paths:
            for filename in os.listdir(dataset_path):
                file_path = os.path.join(dataset_path, filename)
                file_path_list.append(file_path)
        return file_path_list
    
    def delete_time_stamp(self, log_lines: list, deduplicate: bool = True) -> list:
        """Delete the time stamp from each log line.
        Args:
            log_lines (list): The list of log lines.
            deduplicate (bool): Whether to deduplicate lines. Word2Vec used
                deduplication; Doc2Vec needs order and duplicates.
        Returns:
            list: The list of log lines without the time stamp.
        """
        # Initialize new list
        new_log_lines = []
        # Initialize timestamp patterns
        # Matches almost all ISO-8601 timestamps
        timestamp_pattern = re.compile(
            r'\d{4}-\d{2}-\d{2}'                   # YYYY-MM-DD
            r'[T\s]'                               # T or space
            r'\d{2}:\d{2}:\d{2}'                   # HH:MM:SS
            r'(?:\.\d+)?'                          # optional .fractional seconds
            r'(?:Z|[+-]\d{2}:\d{2})?'              # optional timezone (Z or +hh:mm)
            r'\s*'                                 # trailing spaces
        )
        seen = set()
        for line in log_lines:
            new_line = timestamp_pattern.sub('', line).strip('\n')
            if not new_line:
                continue
            if deduplicate:
                if new_line in seen:
                    continue
                seen.add(new_line)
            new_log_lines.append(new_line)
        return new_log_lines
    
    def shorten_log_file_with_keywords(self, log_lines: list[str], num_context_line: int=5) -> list[str]:
        """Shorten a log file to contain only lines surrounding failure keywords.
        
        Args:
            log_lines (list[str]): the lines of the log file to be shortened.
            num_context_line (int): the number of lines surrounding the failure keywords will be included.
        """
        # Define the failure keywords
        failure_keywords = [
            "error", "fail", "exception", "critical", "unable", "denied", "not found", "timeout", "segfault", "panic",
            "unsuccessful", "fatal"
        ]
        selected_lines_index = []
        for i, line in enumerate(log_lines):
            # Split on spaces, underscores, hyphens
            word_list = re.split(r'[\s_-]+', line)
            # Split camelCase
            words = []
            for part in word_list:
                split_camel = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', part)
                words.extend(split_camel)
            word_list = [word.lower() for word in words]
            for keyword in failure_keywords:
                if keyword in word_list:
                    start = max(0, i - num_context_line)
                    end = min(len(log_lines), i + num_context_line + 1)
                    selected_lines_index.extend(range(start, end))
                    break
        # Remove duplicates and sort the indices
        selected_lines_index = sorted(set(selected_lines_index))
        # Select the lines from the original log
        return [log_lines[i] for i in selected_lines_index]
    
    def run(self, num_context_line: int=5) -> None:
        """Run the training dataset creation process."""
        # Create training folder in dataset folder if not already exist
        training_folder = os.path.join("dataset", "training")
        os.makedirs(training_folder, exist_ok=True)
        for client in self.client_list:
            # Get the client file list
            client_file_list = self.get_file_list_from_folder(os.path.join("dataset", client))
            for origin_file in client_file_list:
                # Read log file
                with open(origin_file, "r", encoding="utf-8") as file:
                    log_lines = file.readlines()
                    log_lines = [line.strip() for line in log_lines if line.strip()]
                    log_lines = self.delete_time_stamp(log_lines)
                    log_lines = self.shorten_log_file_with_keywords(log_lines, num_context_line)
                # Check if the log lines are empty
                if len(log_lines) == 0:
                    print("No relevant log lines found for:", origin_file)
                    continue
                # Write processed log lines into a file in training dataset
                out_path = origin_file.replace("dataset", "dataset/training")
                # Check if the directory exist
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, "w", encoding="utf-8") as out_file:
                    # Write each line in a line
                    out_file.writelines("\n".join(log_lines))
                print("Saved:", out_path)


if __name__ == "__main__":
    TrainingDatasetCreator(CLIENT_LIST).run(NUM_CONTEXT_LINE)
