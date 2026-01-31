"""Different designs to separate between training set and test set for each client dataset."""
import os
import random
import shutil
from pathlib import Path


class InternalTrainTestSeparator:
    """Separate clients datasets into training dataset and test dataset."""
    def __init__(self):
        """Initialize InternalTrainTestSeparator."""
        self.client_list = ["d2klab", "logsage", "maryangel101"]
        self.test_ratio = 0.2  # the test dataset is 20% the size of the client dataset

    def collect_all_client_files(self, client_name: str) -> list[str]:
        """Get all log file paths in client dataset.
        
        Args:
            client_name (str): name of client whose dataset we are analyzing.
        """
        client_dataset = f"dataset/origin/{client_name}"
        # Read all log file in the client_dataset folder
        dataset_paths = []  # Collect all folders inside client's overall dataset folder
        for subdir in os.listdir(client_dataset):
            full_path = os.path.join(client_dataset, subdir)
            if os.path.isdir(full_path):
                dataset_paths.append(full_path)
        file_path_list = []  # Collect all file paths in client_dataset folder
        for dataset_path in dataset_paths:
            for filename in os.listdir(dataset_path):
                file_path = os.path.join(dataset_path, filename)
                file_path_list.append(file_path)
        return file_path_list
    
    def select_train_test_files(self, client_name: str) -> tuple[list[str], list[str]]:
        """Classify client log files into training and test file.
        
        Args:
            client_name (str): the name of clients whose we are preparing training and test set.
        """
        # Get the list of log files in client dataset
        file_path_list = self.collect_all_client_files(client_name=client_name)
        num_log_files = len(file_path_list)
        # Check if client has only file, in which case we can split
        if num_log_files <= 1:
            print(f"WARNING: only {num_log_files} file in client dataset. No test file available.")
        # Get the number of test files we should have
        num_test_files = int(num_log_files * self.test_ratio)
        # Ensure at least one test file if possible
        if num_test_files == 0:
            print(f"WARNING: with ratio {self.test_ratio}, there is no test file for client {client_name}.")
            print("Randomly select 1 file as test file.")
            num_test_files = 1
        # Randomly shuffling the list of files in the dataset.
        shuffled_files = file_path_list.copy()
        random.shuffle(shuffled_files)
        
        # Extract the test files and training files
        test_files = shuffled_files[:num_test_files]
        train_files = shuffled_files[num_test_files:]
        print(f"Client: {client_name}, num train files: {len(train_files)}, num_test_files: {len(test_files)}")
        return train_files, test_files

    def create_train_test_directory(self) -> None:
        """Create a folder directory storing the train and test files in separate folders."""
        
        base_path = Path("dataset/train_test_internal")
        base_path.mkdir(exist_ok=True, parents=True)

        for client in self.client_list:
            client_path = base_path / client
            train_path = client_path / "train"
            test_path = client_path / "test"

            train_path.mkdir(parents=True, exist_ok=True)
            test_path.mkdir(parents=True, exist_ok=True)

            # Get client files
            train_files, test_files = self.select_train_test_files(client_name=client)

            for train_file in train_files:
                file_path = Path(train_file)
                # Extract file path after dataset/origin/<client>
                rel_path = file_path.relative_to(Path("dataset") / Path("origin") / client)
                # Full target path preserving folder structure
                target_path = train_path / rel_path
                # Create any missing directories in the target
                target_path.parent.mkdir(parents=True, exist_ok=True)
                # Copy file
                shutil.copy(file_path, target_path)
            
            for test_file in test_files:
                file_path = Path(test_file)
                # Extract file path after dataset/origin/<client>
                rel_path = file_path.relative_to(Path("dataset") / Path("origin") / client)
                # Full target path preserving folder structure
                target_path = test_path / rel_path
                # Create any missing directories in the target
                target_path.parent.mkdir(parents=True, exist_ok=True)
                # Copy file
                shutil.copy(file_path, target_path)

        # Checking the number of files in train and test folder of each client
        
        for client in self.client_list:
            client_path = base_path / client
            train_path = client_path / "train"
            test_path = client_path / "test"

            # Count all files recursively
            num_train_files = len([f for f in train_path.rglob("*") if f.is_file()])
            num_test_files = len([f for f in test_path.rglob("*") if f.is_file()])

            print(f"Client: {client}")
            print(f"  Train files: {num_train_files}")
            print(f"  Test files:  {num_test_files}")
            print("-" * 40)


# if __name__ == "__main__":
    # internal_train_test_separator = InternalTrainTestSeparator()
    # internal_train_test_separator.create_train_test_directory()

