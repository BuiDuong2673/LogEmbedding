"""Test script for log template extraction."""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from helper.log_parser import LogParser, parse_client_logs


def test_single_client(client_name: str = "maryangel101"):
    """Test template extraction on a single client.
    
    Args:
        client_name (str): Name of the client to test.
    """
    print(f"\n{'#'*70}")
    print(f"# Testing Log Template Extraction for: {client_name}")
    print(f"{'#'*70}\n")
    
    # Parse logs and extract templates
    parser = parse_client_logs(client_name, output_dir="dataset/templates")
    
    # Show detailed examples
    print(f"\n{'='*60}")
    print("Sample Templates with Examples:")
    print(f"{'='*60}\n")
    
    # Get top 5 templates
    sorted_templates = sorted(
        parser.templates.items(),
        key=lambda x: x[1]["count"],
        reverse=True
    )[:5]
    
    for i, (cluster_id, data) in enumerate(sorted_templates, 1):
        print(f"\nTemplate {i} (Cluster {cluster_id}):")
        print(f"  Count: {data['count']}")
        print(f"  Template: {data['template']}")
        print(f"  Examples:")
        for j, example in enumerate(data['examples'][:3], 1):
            print(f"    {j}. {example[:100]}..." if len(example) > 100 else f"    {j}. {example}")
    
    return parser


def test_template_matching(parser: LogParser):
    """Test matching new logs to existing templates.
    
    Args:
        parser (LogParser): Parser with extracted templates.
    """
    print(f"\n{'='*60}")
    print("Testing Template Matching:")
    print(f"{'='*60}\n")
    
    # Test with some example logs
    test_logs = [
        "Error: build failed at step 5",
        "Warning: timeout occurred after 300 seconds",
        "Info: process completed successfully"
    ]
    
    for log in test_logs:
        template, cluster_id, confidence = parser.match_log_to_template(log)
        print(f"Log: {log}")
        print(f"  → Template: {template}")
        print(f"  → Cluster ID: {cluster_id}")
        print(f"  → Confidence: {confidence}\n")


def compare_clients():
    """Compare template extraction results across clients."""
    print(f"\n{'#'*70}")
    print(f"# Comparing Template Extraction Across Clients")
    print(f"{'#'*70}\n")
    
    clients = ["maryangel101", "d2klab"]
    results = {}
    
    for client in clients:
        try:
            parser = parse_client_logs(client, output_dir="dataset/templates")
            stats = parser.get_template_statistics()
            results[client] = {
                "parser": parser,
                "stats": stats
            }
        except Exception as e:
            print(f"Error processing {client}: {e}\n")
            results[client] = None
    
    # Print comparison
    print(f"\n{'='*60}")
    print("Comparison Summary:")
    print(f"{'='*60}\n")
    
    for client, data in results.items():
        if data:
            stats = data["stats"]
            print(f"{client}:")
            print(f"  Total Logs: {stats['total_logs']}")
            print(f"  Unique Templates: {stats['num_templates']}")
            print(f"  Compression Ratio: {stats['total_logs'] / max(stats['num_templates'], 1):.2f}:1")
            print()


if __name__ == "__main__":
    # Test 1: Single client with detailed output
    print("\n" + "="*70)
    print("TEST 1: Single Client Template Extraction (maryangel101)")
    print("="*70)
    parser = test_single_client("maryangel101")
    
    # Test 2: Template matching
    # test_template_matching(parser)
    
    # Test 3: Compare all clients
    # Uncomment the following line to test all clients
    # compare_clients()
    
    print("\n" + "="*70)
    print("✓ Template extraction completed successfully!")
    print("✓ Check 'dataset/templates/' directory for output files")
    print("="*70 + "\n")
