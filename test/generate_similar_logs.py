"""For each log file in the test dataset, extract its template, and generate similar log with different variables."""
from pathlib import Path
import re
import random
import string
import os
from datetime import datetime, timedelta, timezone
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
from drain3.masking import MaskingInstruction

class SimilarLogGenerator:
    """Generate similar log for test log."""
    
    def __init__(self):
        """Initialize SimilarLogGenerator."""
        self.client_list = ["maryangel101", "d2klab", "logsage"]
    
    def collect_all_client_test_files(self, client_name: str) -> list[str]:
        """Collect all file paths in client test folder.
        
        Args:
            client_name (str): the name of the client whose we want to extract the file path.
        """
        # The path to client's test folder
        test_path = Path("dataset/train_test_internal") / client_name / "test"
        if not test_path.exists():
            print(f"WARNING: client test folder path: {test_path} does not exist.")
            return []
        # Recursively collect all files
        file_paths = [str(path) for path in test_path.rglob("*") if path.is_file()]
        return file_paths
    
    def extract_log_template(self, original_log: str) -> list[str]:
        """Extract template from a log file, mask as many variables as possible.
        
        Args:
            original_log (str): the log which we want to extract the template.
        
        Returns:
            list[str]: the list of lines of the template. 
        """
        # Split log into list of lines
        log_lines = original_log.splitlines()
        # Define timestampt format for deleting it from log_lines
        timestamp_pattern = re.compile(
            r'\d{4}-\d{2}-\d{2}'                   # YYYY-MM-DD
            r'[T\s]'                               # T or space
            r'\d{2}:\d{2}:\d{2}'                   # HH:MM:SS
            r'(?:\.\d+)?'                          # optional .fractional seconds
            r'(?:Z|[+-]\d{2}:\d{2})?'              # optional timezone (Z or +hh:mm)
            r'\s*'                                 # trailing spaces
        )
        # Define variables format to be masked
        config = TemplateMinerConfig()
        masking_instances = [
            MaskingInstruction(r'((?<=[^A-Za-z0-9])|^)(([0-9a-f]{2,}:){3,}([0-9a-f]{2,}))((?=[^A-Za-z0-9])|$)', "ID"),
            MaskingInstruction(r'((?<=[^A-Za-z0-9])|^)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})((?=[^A-Za-z0-9])|$)', "IP"),
            MaskingInstruction(r'((?<=[^A-Za-z0-9])|^)([0-9a-f]{6,} ?){3,}((?=[^A-Za-z0-9])|$)', "SEQ"),
            MaskingInstruction(r'((?<=[^A-Za-z0-9])|^)([0-9A-F]{4} ?){4,}((?=[^A-Za-z0-9])|$)', "SEQ"),

            MaskingInstruction(r'((?<=[^A-Za-z0-9])|^)(0x[a-f0-9A-F]+)((?=[^A-Za-z0-9])|$)', "HEX"),
            MaskingInstruction(r'((?<=[^A-Za-z0-9])|^)([\-\+]?\d+)((?=[^A-Za-z0-9])|$)', "NUM"),
            MaskingInstruction(r'(?<=executed cmd )(".+?")', "CMD"),
            MaskingInstruction(r'((?<=[^A-Za-z0-9])|^)(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z?)((?=[^A-Za-z0-9])|$)', "TIME"),
        ]
        config.masking_instructions = masking_instances
        # Mask variables
        template_miner = TemplateMiner(config=config)
        for line in log_lines:
            # Delete timestampt
            line = timestamp_pattern.sub('', line).strip('\n')
            template_miner.add_log_message(line.strip())
        # Add only masked content (without cluster ID and size)
        new_log_lines = []
        for cluster in template_miner.drain.clusters:
            new_log_lines.append(cluster.get_template())
        return new_log_lines

    def generate_variables(self, label: str) -> str:
        """Generate a random variable for each type of variable being masked.
        
        Args:
            label (str): The label of the variable to generate.

        Returns:
            str: The generated variable.
        """
        if label == "ID":
            # ([0-9a-f]{2,}:){3,}([0-9a-f]{2,})
            groups = random.randint(4, 6)  # at least 4 groups
            return ":".join(
                "".join(random.choice("0123456789abcdef") for _ in range(random.randint(2, 4)))
                for _ in range(groups)
            )

        if label == "IP":
            # \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
            return ".".join(str(random.randint(0, 255)) for _ in range(4))

        if label == "SEQ":
            # ([0-9a-f]{6,} ?){3,}  OR  ([0-9A-F]{4} ?){4,}
            use_upper = random.choice([True, False])
            if use_upper:
                groups = random.randint(4, 6)
                return " ".join(
                    "".join(random.choice("0123456789ABCDEF") for _ in range(4))
                    for _ in range(groups)
                )
            else:
                groups = random.randint(3, 5)
                return " ".join(
                    "".join(random.choice("0123456789abcdef") for _ in range(random.randint(6, 12)))
                    for _ in range(groups)
                )

        if label == "HEX":
            # 0x[a-f0-9A-F]+
            return "0x" + "".join(
                random.choice("0123456789abcdefABCDEF")
                for _ in range(random.randint(1, 16))
            )

        if label == "NUM":
            # [\-\+]?\d+
            sign = random.choice(["", "-", "+"])
            return sign + str(random.randint(0, 99999))

        if label == "CMD":
            # (?<=executed cmd )(".+?")
            cmds = [
                "ls -la",
                "cat /etc/passwd",
                "ps aux | grep python",
                "curl -I http://example.com",
                "df -h"
            ]
            return f"\"{random.choice(cmds)}\""

        if label == "TIME":
            # generate a timezone-aware UTC datetime
            base = datetime.now(timezone.utc) - timedelta(days=random.randint(0, 365))
            ts = base.strftime("%Y-%m-%dT%H:%M:%S")
            # optional 'Z' to match ISO 8601 UTC notation
            return ts + ("Z" if random.choice([True, False]) else "")

        return label
    
    def get_generated_log_path(self, log_path: str) -> str:
        """Calculate the path for the generated log given the path for the original log.
        
        Args:
            log_path (str): the path to the test log file whose template we are going to find path to save.
        """
        path = Path(log_path)
        # Find the index of "test" in the path, which we want to replace
        parts = path.parts
        test_idx = parts.index("test")
        # Build new path: replace "test" with "generate_test_log"
        new_parts = (
            parts[:test_idx]
            + ("generate_test_log",)
            + parts[test_idx + 1:]
        )
        return Path(*new_parts)
    
    def create_log_template_for_client(self, client_name: str) -> None:
        """Create log template for each client's logs.

        Args:
            client_name (str): The name of the client for whom to create the dataset.
        """
        # Get the list of file paths of the training dataset.
        log_file_paths = self.collect_all_client_test_files(client_name=client_name)

        # Create a testing dataset for each file.
        for file_path in log_file_paths:
            with open(file_path, "r", encoding="utf-8") as log_file:
                log_text = log_file.read()

            log_template = self.extract_log_template(log_text)

            log_template_text = "\n".join(log_template)

            angle_pattern = re.compile(r'<(ID|IP|SEQ|HEX|NUM|CMD|URL|PATH|TIME)>')

            def _angle_repl(m):
                return self.generate_variables(m.group(1))

            test_log = angle_pattern.sub(_angle_repl, log_template_text)
            test_log = re.sub(
                r'<\*>',
                lambda _: ''.join(random.choices(string.ascii_letters + string.digits, k=5)),
                test_log
            )
            # Get the path where we can save the generated log file
            generated_file_path = self.get_generated_log_path(file_path)
            # Make sure all the associated directory already exist
            generated_file_path.parent.mkdir(parents=True, exist_ok=True)
            # Save the generated log to the targeted path
            with open(generated_file_path, "w", encoding="utf-8") as generated_file:
                generated_file.write(test_log)
            print(f"Saved the generated log to file: {generated_file_path}")
    
    def run(self) -> None:
        """Generate the similar logs for all clients test dataset."""
        for client in self.client_list:
            self.create_log_template_for_client(client_name=client)


if __name__ == "__main__":
    log_generator = SimilarLogGenerator()
    log_generator.run()
