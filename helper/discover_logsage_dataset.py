"""LogSage is a very large dataset. This file is explore the dataset to decide which file to use."""
import re
import os
from pathlib import Path
import shutil


LOGSAGE_PATH = "dataset/logsage"


def delete_timestampt(origin_log_lines: list[str]) -> list[str]:
    """Delete timestampt in each line of the log and return a list of log lines.
    
    Args:
        origin_log_lines (list[str]): the list of log lines in the original file which we want to remove timestampts.
    """
    # Delete timestampt
    cleaned_log_lines = []
    for line in origin_log_lines:
        cleaned_line = re.sub(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z\s*", "", line)
        if cleaned_line != "":
            # Remote escape characters.
            ANSI_ESCAPE_RE = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
            cleaned_line = ANSI_ESCAPE_RE.sub('', cleaned_line)
            cleaned_log_lines.append(cleaned_line.strip())
    return cleaned_log_lines


def is_big_file_contain_small_files(status_dir: str) -> bool:
    """Check whether fail.txt contains the contents of all files in fail/fail/.

    Args:
        status_dir (str): the path to the folder ...pair_{1/2}/fail/ or ...pair_{1/2}/success/
    """
    pair_path = Path(status_dir)
    folder_name = pair_path.name
    txt_path = pair_path / f"{folder_name}.txt"
    steps_dir = pair_path / folder_name

    # Read fail.txt
    if not txt_path.exists():
        raise FileNotFoundError(f"Missing {txt_path}")

    with open(txt_path, "r", encoding="utf-8") as f:
        txt_content = f.readlines()
    # Remove timestampt
    txt_content = delete_timestampt(txt_content)

    missing_files = []

    # Iterate through all step files
    for step_file in sorted(steps_dir.glob("*.txt")):
        with open(step_file, "r", encoding="utf-8") as f:
            step_content = f.readlines()
        # Remove timestampt
        step_content = delete_timestampt(step_content)

        for step_line in step_content:
            if step_line == "":
                continue
            similar_line_found = False
            for txt_line in txt_content:
                if step_line.strip() == txt_line.strip():
                    similar_line_found = True
                    break
            if similar_line_found == False:
                missing_files.append(step_file)
                break

    if missing_files:
        print(f"❌ {txt_path} is missing content from:")
        for name in missing_files:
            print(f"  - {name}")
        return False

    print(f"✅ {txt_path} contains all step file contents.")
    return True


def get_status_dir() -> list[str]:
    """Get all status dir where the folder that we need to analyze locate in, e.g. ...pair_{1/2}/fail/."""
    base_dir = Path("dataset/logsage")

    result_paths = []

    for topic_dir in base_dir.iterdir():
        if not topic_dir.is_dir():
            continue

        for pair_dir in topic_dir.iterdir():
            if not pair_dir.is_dir():
                continue

            for status in ["fail", "success"]:
                status_dir = pair_dir / status
                if status_dir.exists() and status_dir.is_dir():
                    result_paths.append(status_dir)
    print(f"len(result_paths) = {len(result_paths)}")
    return result_paths

def reformat_dataset() -> None:
    """Remove unnecessary files and rearrange the dataset."""
    base_dir = Path("dataset/logsage")
    # Create a new dataset
    new_base_dir = Path("dataset/logsage_preprocessed")
    os.makedirs(new_base_dir, exist_ok=True)

    num_copied = 0

    for topic_dir in base_dir.iterdir():
        if not topic_dir.is_dir():
            continue
        # Create topic directory
        new_topic_dir = new_base_dir / topic_dir.name
        os.makedirs(new_base_dir, exist_ok=True)

        for pair_dir in topic_dir.iterdir():
            if not pair_dir.is_dir():
                continue

            for status in ["fail", "success"]:
                status_dir = pair_dir / status
                if not status_dir.is_dir():
                    continue

                # Source file: fail.txt or success.txt
                src_file = status_dir / f"{status}.txt"

                if not src_file.is_file():
                    print(f"Missing file: {src_file}")
                    continue

                # Target file name: pair_1_fail.txt, pair_1_success.txt
                new_file_path = new_topic_dir / f"{pair_dir.name}_{status}.txt"

                # Ensure the parent directory exists
                new_file_path.parent.mkdir(parents=True, exist_ok=True)

                # Copy file content
                shutil.copyfile(src_file, new_file_path)
                num_copied += 1

    print(f"Copied {num_copied} files to new dataset.")


def main():
    """Run all the analyzing."""
    get_status_dir()
    reformat_dataset()


if __name__ == "__main__":
    main()
