"""Log template extraction using Drain algorithm."""
import sys
import os
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig


# Allow running this file directly via `python helper/log_parser.py`
# by ensuring the project root is on sys.path.
_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))


class LogParser:
    """Parse logs and extract templates using Drain algorithm."""
    
    def __init__(self, depth: int = 4, sim_th: float = 0.4, max_children: int = 100):
        """Initialize the LogParser with Drain configuration.
        
        Args:
            depth (int): Depth of the parse tree. Default is 4.
            sim_th (float): Similarity threshold for clustering. Default is 0.4.
            max_children (int): Max number of children for a node in the tree. Default is 100.
        """
        self.depth = depth
        self.sim_th = sim_th
        self.max_children = max_children
        
        # Configure Drain
        config = TemplateMinerConfig()
        config.load({
            "drain": {
                "depth": depth,
                "sim_th": sim_th,
                "max_children": max_children,
                "max_clusters": None
            },
            "masking": [
                {
                    "regex_pattern": r"\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?",
                    "mask_with": "<TIMESTAMP>"
                },
                {
                    "regex_pattern": r"\b\d+\.\d+\.\d+\.\d+\b",
                    "mask_with": "<IP>"
                },
                {
                    "regex_pattern": r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b",
                    "mask_with": "<UUID>"
                },
                {
                    "regex_pattern": r"\b[0-9a-fA-F]{32,64}\b",
                    "mask_with": "<HASH>"
                },
                {
                    "regex_pattern": r"\b\d+\b",
                    "mask_with": "<NUM>"
                },
                {
                    "regex_pattern": r"\/[\w\-\.\/]+",
                    "mask_with": "<PATH>"
                }
            ]
        })
        
        self.template_miner = TemplateMiner(config=config)
        self.templates = {}
        self.log_to_template = {}
    
    def parse_log_line(self, log_line: str) -> Tuple[str, int]:
        """Parse a single log line and return its template.
        
        Args:
            log_line (str): A single log line.
            
        Returns:
            Tuple[str, int]: Template string and cluster ID.
        """
        result = self.template_miner.add_log_message(log_line)
        cluster_id = result["cluster_id"]
        template = result["template_mined"]
        
        return template, cluster_id
    
    def parse_logs(self, log_lines: List[str]) -> Dict:
        """Parse multiple log lines and extract templates.
        
        Args:
            log_lines (List[str]): List of log lines.
            
        Returns:
            Dict: Dictionary containing templates and statistics.
        """
        template_counts = {}
        
        for log_line in log_lines:
            if not log_line or not log_line.strip():
                continue
                
            template, cluster_id = self.parse_log_line(log_line.strip())
            
            # Store template information
            if cluster_id not in self.templates:
                self.templates[cluster_id] = {
                    "template": template,
                    "count": 0,
                    "examples": []
                }
            
            self.templates[cluster_id]["count"] += 1
            
            # Store a few examples (max 5)
            if len(self.templates[cluster_id]["examples"]) < 5:
                self.templates[cluster_id]["examples"].append(log_line.strip())
            
            # Map log to template
            self.log_to_template[log_line.strip()] = cluster_id
        
        return self.templates

    def get_cluster_examples(self, *, sort_examples: bool = False) -> Dict[int, List[str]]:
        """Group all parsed log lines by cluster ID.

        Notes:
            This uses the keys of `self.log_to_template`, so the examples are unique
            by exact log line string.

        Args:
            sort_examples (bool): Sort examples alphabetically for stable output.

        Returns:
            Dict[int, List[str]]: Mapping cluster_id -> list of log lines.
        """
        cluster_to_examples: Dict[int, List[str]] = {}
        for log_line, cluster_id in self.log_to_template.items():
            cluster_to_examples.setdefault(cluster_id, []).append(log_line)

        if sort_examples:
            for cluster_id in cluster_to_examples:
                cluster_to_examples[cluster_id].sort()

        return cluster_to_examples

    def save_cluster_examples(
        self,
        output_path: str,
        *,
        sort_clusters_by_count: bool = True,
        sort_examples: bool = False,
        include_statistics: bool = True,
    ) -> None:
        """Save *all* clustered log examples to a JSON file.

        This is separate from `save_templates()` so the template file can stay small.

        Args:
            output_path (str): Path to save the clustered examples JSON.
            sort_clusters_by_count (bool): Output clusters ordered by descending count.
            sort_examples (bool): Sort example strings for stable output.
            include_statistics (bool): Include summary statistics section.
        """
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        cluster_to_examples = self.get_cluster_examples(sort_examples=sort_examples)

        cluster_items = list(self.templates.items())
        if sort_clusters_by_count:
            cluster_items.sort(key=lambda x: x[1].get("count", 0), reverse=True)

        clusters_output: Dict[str, Dict] = {}
        for cluster_id, data in cluster_items:
            all_examples = cluster_to_examples.get(cluster_id, [])
            clusters_output[str(cluster_id)] = {
                "template": data.get("template", ""),
                "count": data.get("count", 0),
                "unique_examples_count": len(all_examples),
                "examples": all_examples,
            }

        output_data: Dict[str, object] = {
            "config": {
                "depth": self.depth,
                "sim_th": self.sim_th,
                "max_children": self.max_children,
            },
            "clusters": clusters_output,
        }

        if include_statistics:
            output_data["statistics"] = self.get_template_statistics()

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"Cluster examples saved to: {output_path}")
    
    def get_template_statistics(self) -> Dict:
        """Get statistics about extracted templates.
        
        Returns:
            Dict: Statistics including number of templates, coverage, etc.
        """
        total_logs = len(self.log_to_template)
        num_templates = len(self.templates)
        
        # Sort templates by frequency
        sorted_templates = sorted(
            self.templates.items(),
            key=lambda x: x[1]["count"],
            reverse=True
        )
        
        stats = {
            "total_logs": total_logs,
            "num_templates": num_templates,
            "templates_by_frequency": [
                {
                    "cluster_id": cluster_id,
                    "template": data["template"],
                    "count": data["count"],
                    "percentage": (data["count"] / total_logs * 100) if total_logs > 0 else 0
                }
                for cluster_id, data in sorted_templates[:20]  # Top 20
            ]
        }
        
        return stats
    
    def save_templates(self, output_path: str) -> None:
        """Save extracted templates to a JSON file.
        
        Args:
            output_path (str): Path to save the templates.
        """
        # Create directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        # Prepare data for JSON serialization
        output_data = {
            "config": {
                "depth": self.depth,
                "sim_th": self.sim_th,
                "max_children": self.max_children
            },
            "statistics": self.get_template_statistics(),
            "templates": {
                str(cluster_id): {
                    "template": data["template"],
                    "count": data["count"],
                    "examples": data["examples"]
                }
                for cluster_id, data in self.templates.items()
            }
        }
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        print(f"Templates saved to: {output_path}")
        print(f"Total templates: {len(self.templates)}")
        print(f"Total logs processed: {len(self.log_to_template)}")
    
    def load_templates(self, input_path: str) -> None:
        """Load templates from a JSON file.
        
        Args:
            input_path (str): Path to load the templates from.
        """
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.templates = {
            int(cluster_id): template_data
            for cluster_id, template_data in data["templates"].items()
        }
        
        print(f"Loaded {len(self.templates)} templates from {input_path}")
    
    def match_log_to_template(self, log_line: str) -> Tuple[str, int, float]:
        """Match a new log line to an existing template.
        
        Args:
            log_line (str): A log line to match.
            
        Returns:
            Tuple[str, int, float]: Template string, cluster ID, and confidence score.
        """
        result = self.template_miner.match(log_line)
        
        if result:
            cluster_id = result.cluster_id
            template = self.templates.get(cluster_id, {}).get("template", "Unknown")
            confidence = 1.0  # Drain doesn't provide confidence, set to 1.0 if matched
            return template, cluster_id, confidence
        else:
            return "No match", -1, 0.0


def parse_client_logs(client_name: str, output_dir: str = "dataset/templates") -> LogParser:
    """Parse logs for a specific client and save templates.
    
    Args:
        client_name (str): Name of the client (e.g., 'maryangel101', 'd2klab').
        output_dir (str): Directory to save the templates.
        
    Returns:
        LogParser: The parser with extracted templates.
    """
    from helper.vocab_extractor import VocabExtractor
    
    print(f"\n{'='*60}")
    print(f"Parsing logs for client: {client_name}")
    print(f"{'='*60}\n")
    
    # Initialize parser
    parser = LogParser(depth=4, sim_th=0.4, max_children=100)
    
    # Load client logs
    extractor = VocabExtractor(client_name=client_name)
    log_lines = extractor.load_client_dataset()
    
    print(f"Loaded {len(log_lines)} log lines")
    
    # Delete timestamps before parsing
    print(f"Removing timestamps from log lines...")
    log_lines = extractor.delete_time_stamp(log_lines)
    print(f"Preprocessed {len(log_lines)} unique log lines after timestamp removal")
    
    # Parse logs
    templates = parser.parse_logs(log_lines)
    
    # Print statistics
    stats = parser.get_template_statistics()
    print(f"\nExtracted {stats['num_templates']} templates from {stats['total_logs']} logs")
    print(f"\nTop 10 most frequent templates:")
    for i, template_info in enumerate(stats['templates_by_frequency'][:10], 1):
        print(f"{i}. [{template_info['count']} logs, {template_info['percentage']:.1f}%]")
        print(f"   {template_info['template']}")
    
    # Save templates
    templates_output_path = os.path.join(output_dir, f"{client_name}_templates.json")
    parser.save_templates(templates_output_path)

    # Save all clustered examples
    examples_output_path = os.path.join(output_dir, f"{client_name}_cluster_examples.json")
    parser.save_cluster_examples(examples_output_path)
    
    return parser


if __name__ == "__main__":
    # Parse logs for all clients
    clients = ["maryangel101", "d2klab"]
    
    for client in clients:
        try:
            parse_client_logs(client)
        except Exception as e:
            print(f"Error parsing logs for {client}: {e}")
