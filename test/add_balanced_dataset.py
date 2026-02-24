import os
import shutil
import random
from pathlib import Path


def balance_dataset(origin_root, balanced_root, k, seed=42):
    """
    origin_root: path to dataset/origin
    balanced_root: path to dataset/balanced_data
    k: number of new clients
    seed: random seed for reproducibility
    """

    random.seed(seed)

    origin_root = Path(origin_root)
    balanced_root = Path(balanced_root)

    # Step 1: Collect all txt files
    all_files = list(origin_root.glob("*/*/*.txt"))

    print(f"Total .txt files found: {len(all_files)}")

    if len(all_files) == 0:
        raise ValueError("No .txt files found in the origin dataset.")

    # Step 2: Shuffle files
    random.shuffle(all_files)

    # Step 3: Split files equally
    splits = [[] for _ in range(k)]
    for idx, file_path in enumerate(all_files):
        splits[idx % k].append(file_path)

    # Step 4: Create balanced structure
    for i, client_files in enumerate(splits):
        new_client_root = balanced_root / f"client_{i+1}"
        print(f"Client {i+1}: {len(client_files)} files")

        for file_path in client_files:
            # Extract original client_directory and log_file
            # origin/[client_name]/[client_directory]/[log_file].txt
            relative_parts = file_path.relative_to(origin_root).parts
            client_directory = relative_parts[1]  # [client_directory]
            log_file = relative_parts[2]          # [log_file].txt

            target_dir = new_client_root / client_directory
            target_dir.mkdir(parents=True, exist_ok=True)

            shutil.copy(file_path, target_dir / log_file)

    print(f"Balanced dataset created with {k} clients at {balanced_root}")


def count_files_per_client(origin_root):
    """
    Count and print how many files each client has in the original dataset.

    origin_root: path to dataset/origin
    """

    origin_root = Path(origin_root)

    # Step 1: Find all client directories
    client_dirs = [d for d in origin_root.iterdir() if d.is_dir()]
    if not client_dirs:
        print("No client directories found in the origin dataset.")
        return

    # Step 2: Count .txt files for each client
    total_files = 0
    for client_dir in client_dirs:
        # Count recursively all .txt files under this client
        client_files = list(client_dir.rglob("*.txt"))
        print(f"Client {client_dir.name}: {len(client_files)} files")
        total_files += len(client_files)

    print(f"Total .txt files in dataset: {total_files}")


if __name__ == "__main__":
    # balance_dataset(
    #     origin_root="dataset/origin",
    #     balanced_root="dataset/balanced_data",
    #     k=3
    # )

    count_files_per_client("dataset/balanced_data")
