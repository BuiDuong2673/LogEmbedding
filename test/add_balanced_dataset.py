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


if __name__ == "__main__":
    balance_dataset(
        origin_root="dataset/origin",
        balanced_root="dataset/balanced_data",
        k=3
    )
