"""Create testing dataset by replacing variables in training dataset."""
import re
import random
import string
import os
from datetime import datetime, timedelta, timezone
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
from drain3.masking import MaskingInstruction
from helper.create_training_dataset import TrainingDatasetCreator

CLIENT_LIST = ["d2klab", "maryangel101"]



class TestingDatasetCreator:
    """A class to create a testing dataset."""
    def __init__(self, client_name: list[str]) -> None:
        """Initialize the TestingDatasetCreator."""
        self.client_name = client_name
    
    def extract_log_template(self, log_lines: list[str]) -> list[str]:
        """Mask all variables in the logs.
        
        Args:
            log_lines (list[str]): The log lines to extract the template from.

        Returns:
            list[str]: The extracted log template.
        """
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

    def create_log_template_for_client(self, client_name: str) -> None:
        """Create log template for each client's logs.

        Args:
            client_name (str): The name of the client for whom to create the dataset.
        """
        # Create template folder in dataset folder if not already exist
        template_folder = os.path.join("dataset", "template")
        os.makedirs(template_folder, exist_ok=True)

        # Get the list of file paths of the training dataset.
        training_file_paths = TrainingDatasetCreator().get_file_list_from_folder(f"dataset/training/{client_name}")

        # Create a testing dataset for each file.
        for file_path in training_file_paths:
            # Read the original log content
            with open(file_path, "r", encoding="utf-8") as train_file:
                log_lines = train_file.readlines()

            # Extract log template
            log_template = self.extract_log_template(log_lines)
            # Save log template to template folder in dataset
            template_path = file_path.replace("dataset/training", "dataset/template")
            # Check if the directory exist
            os.makedirs(os.path.dirname(template_path), exist_ok=True)
            # Save log template
            with open(template_path, "w", encoding="utf-8") as out_file:
                out_file.writelines("\n".join(log_template))
            print("Saved template to:", template_path)
    
    def random_string(self, length=5):
        """Randomly generate a string to replace unidentifiable variable types.
        
        Args:
            length (int): the length that the string should have.
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def create_testing_data_for_client(self, client_name: str) -> None:
        # Create testing folder in dataset folder if not already exist
        testing_folder = os.path.join("dataset", "testing")
        os.makedirs(testing_folder, exist_ok=True)

        # Get the list of file paths of the template dataset.
        template_file_paths = TrainingDatasetCreator().get_file_list_from_folder(f"dataset/template/{client_name}")

        for template_path in template_file_paths:
            # Read the original log content
            with open(template_path, "r", encoding="utf-8") as template_file:
                template = template_file.read()
            # If the template is empty, skip
            if template == "":
                print(f"WARNING: {template_path} is empty.")
                continue

            # First, replace identifiable variables types with their corresponding formats
            angle_pattern = re.compile(r'<(ID|IP|SEQ|HEX|NUM|CMD|URL|PATH|TIME)>')
            def _angle_repl(m):
                label = m.group(1)
                return self.generate_variables(label)
            # Then, handle unidentifiable variables types with a random string of length 5
            test_log = angle_pattern.sub(_angle_repl, template)
            test_log = re.sub(r'<\*>', lambda _: self.random_string(5), test_log)

            # Save the test log to the testing folder
            testing_path = template_path.replace("dataset/template", "dataset/testing")
            os.makedirs(os.path.dirname(testing_path), exist_ok=True)
            with open(testing_path, "w", encoding="utf-8") as out_file:
                out_file.write(test_log)
            print("Saved testing log to:", testing_path)

if __name__ == "__main__":
    # Create a log template for each client's logs
    test_creator = TestingDatasetCreator(CLIENT_LIST)
    for client in CLIENT_LIST:
        test_creator.create_log_template_for_client(client)
    for client in CLIENT_LIST:
        test_creator.create_testing_data_for_client(client)
