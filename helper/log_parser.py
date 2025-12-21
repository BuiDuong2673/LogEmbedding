"""Log template extraction using Drain algorithm."""
import sys
import os
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Iterable
from collections import Counter
import random
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

        self._template_miner_config = config
        self.template_miner = TemplateMiner(config=self._template_miner_config)
        self.templates: Dict[int, Dict] = {}
        self.log_to_template: Dict[str, int] = {}
        self.template_to_cluster_id: Dict[str, int] = {}
        self.exact_template_to_cluster_id: Dict[str, int] = {}
        # When rebuilding the matcher from examples, Drain internal cluster IDs won't
        # match saved cluster IDs. This mapping converts Drain cluster_id -> saved cluster_id.
        self.drain_cluster_id_to_stable_cluster_id: Dict[int, int] = {}
    
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

        # Keep a stable lookup by template string
        if template and cluster_id is not None:
            self.template_to_cluster_id[template] = cluster_id
        
        return template, cluster_id

    def rebuild_matcher_from_templates(self) -> None:
        """Rebuild internal Drain matcher using the currently loaded templates.

        This enables matching/classification after loading templates from JSON
        without re-parsing the full raw log dataset.
        """
        self.template_miner = TemplateMiner(config=self._template_miner_config)
        self.template_to_cluster_id = {}
        self.exact_template_to_cluster_id = {}
        self.drain_cluster_id_to_stable_cluster_id = {}

        # First build a deterministic mapping from exact saved template text -> cluster_id.
        # If duplicates exist, keep the cluster with the higher count.
        for cluster_id, data in self.templates.items():
            template_text = (data or {}).get("template")
            if not template_text:
                continue

            prev_id = self.exact_template_to_cluster_id.get(template_text)
            if prev_id is None:
                self.exact_template_to_cluster_id[template_text] = cluster_id
            else:
                prev_count = int(self.templates.get(prev_id, {}).get("count", 0))
                new_count = int((data or {}).get("count", 0))
                if new_count > prev_count:
                    self.exact_template_to_cluster_id[template_text] = cluster_id

        # Feed templates as "messages" to create clusters.
        for cluster_id, data in self.templates.items():
            template_text = (data or {}).get("template")
            if not template_text:
                continue

            result = self.template_miner.add_log_message(template_text)
            mined_template = result.get("template_mined")
            if mined_template:
                # Map mined template string back to original cluster ID.
                # If duplicates exist, keep the cluster with higher count.
                prev_id = self.template_to_cluster_id.get(mined_template)
                if prev_id is None:
                    self.template_to_cluster_id[mined_template] = cluster_id
                else:
                    prev_count = int(self.templates.get(prev_id, {}).get("count", 0))
                    new_count = int((data or {}).get("count", 0))
                    if new_count > prev_count:
                        self.template_to_cluster_id[mined_template] = cluster_id

    @staticmethod
    def _iter_selected_clusters(
        clusters: Dict[str, Dict],
        *,
        max_clusters: Optional[int],
        sort_by_count: bool,
    ) -> Iterable[Tuple[int, Dict]]:
        items: List[Tuple[int, Dict]] = [
            (int(cid), payload) for cid, payload in (clusters or {}).items() if payload is not None
        ]
        if sort_by_count:
            items.sort(key=lambda x: int((x[1] or {}).get("count", 0)), reverse=True)
        if max_clusters is not None:
            items = items[: max_clusters]
        return items

    def rebuild_matcher_from_cluster_examples(
        self,
        clusters: Dict[str, Dict],
        *,
        examples_per_cluster: int = 20,
        max_clusters: Optional[int] = None,
        seed: int = 0,
        sort_by_count: bool = True,
    ) -> None:
        """High-coverage rebuild: feed sampled real examples to Drain.

        This tends to achieve much higher match coverage vs feeding only template strings.

        Args:
            clusters: The `clusters` dict from `*_cluster_examples.json`.
            examples_per_cluster: How many examples to sample per cluster.
            max_clusters: Optional cap on number of clusters to include.
            seed: RNG seed for stable sampling.
            sort_by_count: Prefer high-frequency clusters first.
        """
        self.template_miner = TemplateMiner(config=self._template_miner_config)
        self.template_to_cluster_id = {}
        self.drain_cluster_id_to_stable_cluster_id = {}

        rng = random.Random(seed)

        votes: Dict[int, Counter] = {}
        for stable_cluster_id, payload in self._iter_selected_clusters(
            clusters, max_clusters=max_clusters, sort_by_count=sort_by_count
        ):
            examples: List[str] = list((payload or {}).get("examples", []))
            if not examples:
                continue

            if examples_per_cluster <= 0:
                continue

            take = min(examples_per_cluster, len(examples))
            sampled = rng.sample(examples, k=take) if len(examples) >= take else examples

            for line in sampled:
                if not line or not str(line).strip():
                    continue

                res = self.template_miner.add_log_message(str(line).strip())
                drain_cluster_id = int(res.get("cluster_id"))
                mined_template = res.get("template_mined")

                votes.setdefault(drain_cluster_id, Counter())[stable_cluster_id] += 1
                if mined_template:
                    prev = self.template_to_cluster_id.get(mined_template)
                    if prev is None:
                        self.template_to_cluster_id[mined_template] = stable_cluster_id

        # Finalize Drain-cluster -> stable-cluster mapping by majority vote.
        for drain_cluster_id, counter in votes.items():
            stable_cluster_id, _ = counter.most_common(1)[0]
            self.drain_cluster_id_to_stable_cluster_id[drain_cluster_id] = stable_cluster_id

    @staticmethod
    def _cluster_to_template_str(cluster: object) -> Optional[str]:
        """Best-effort extraction of the template string from a Drain3 cluster."""
        if cluster is None:
            return None

        # Most common in drain3: LogCluster.get_template()
        getter = getattr(cluster, "get_template", None)
        if callable(getter):
            try:
                return getter()
            except Exception:
                pass

        # Fallbacks (depending on drain3 version)
        for attr in ("template", "template_mined"):
            value = getattr(cluster, attr, None)
            if isinstance(value, str) and value:
                return value

        return None
    
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

        # Rebuild a matcher so we can classify new inputs using match().
        self.rebuild_matcher_from_templates()
        
        print(f"Loaded {len(self.templates)} templates from {input_path}")

    def load_cluster_examples(self, input_path: str) -> Dict[str, Dict]:
        """Load cluster examples from `*_cluster_examples.json`.

        Returns:
            Dict[str, Dict]: The `clusters` mapping.
        """
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("clusters", {})
    
    def match_log_to_template(self, log_line: str) -> Tuple[str, int, float]:
        """Match a new log line to an existing template.
        
        Args:
            log_line (str): A log line to match.
            
        Returns:
            Tuple[str, int, float]: Template string, cluster ID, and confidence score.
        """
        # Deterministic fast-path: if input exactly equals a saved template text,
        # return that mapping without invoking fuzzy matching.
        exact_id = self.exact_template_to_cluster_id.get(log_line)
        if exact_id is not None:
            template = self.templates.get(exact_id, {}).get("template", log_line)
            return template, exact_id, 1.0

        result = self.template_miner.match(log_line)

        if not result:
            return "No match", -1, 0.0

        drain_cluster_id = getattr(result, "cluster_id", None)
        if isinstance(drain_cluster_id, int) and drain_cluster_id in self.drain_cluster_id_to_stable_cluster_id:
            stable_cluster_id = self.drain_cluster_id_to_stable_cluster_id[drain_cluster_id]
            template = self.templates.get(stable_cluster_id, {}).get("template")
            if template:
                return template, stable_cluster_id, 1.0

        mined_template = self._cluster_to_template_str(result)
        if mined_template and mined_template in self.template_to_cluster_id:
            stable_cluster_id = self.template_to_cluster_id[mined_template]
            template = self.templates.get(stable_cluster_id, {}).get("template", mined_template)
            return template, stable_cluster_id, 1.0

        # Fallback: if we cannot map, return Drain's cluster_id (may differ from saved IDs)
        cluster_id = getattr(result, "cluster_id", -1)
        template = self.templates.get(cluster_id, {}).get("template", mined_template or "Unknown")
        return template, int(cluster_id) if cluster_id is not None else -1, 1.0


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
