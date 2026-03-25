# gap_report_pipeline.py - Koray Semantic Gap Pipeline v2.1
# Chains query_clusterer + entity_extractor for full report

import argparse
import pandas as pd
from query_clusterer import cluster_queries  # Import from same folder
from entity_extractor import extract_eav

def generate_gap_report(queries, content, competitors, num_clusters=5):
    """Pipeline: Cluster queries → Extract EAV → Find gaps (missing EAV in clusters)."""
    df_clusters = cluster_queries(queries, num_clusters)
    gaps = []
    my_eav = extract_eav(content)
    for comp in competitors:
        comp_eav = extract_eav(comp)
        missing = set(comp_eav["Entity"]) - set(my_eav["Entity"])  # Simple set diff
        for m in missing:
            # Improved: Assign to a relevant cluster (simplistic: first cluster for demo; enhance with similarity if needed)
            gaps.append({"Gap_Entity": m, "In_Cluster": df_clusters["Cluster"].iloc[0], "Info_Gain": len(m)})  # Proxy gain
    
    return pd.DataFrame(gaps)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate semantic gap report")
    parser.add_argument("--queries", type=str, required=True, help="Comma-separated queries or CSV path")
    parser.add_argument("--content", type=str, required=True, help="Your content text or file path")
    parser.add_argument("--competitors", type=str, required=True, help="Comma-separated competitor texts or file paths")
    parser.add_argument("--num_clusters", type=int, default=5, help="Number of clusters for query clustering")
    parser.add_argument("--output_csv", type=str, default="gap_report.csv", help="Output CSV path")
    args = parser.parse_args()

    # Load queries
    if args.queries.endswith(".csv"):
        df_queries = pd.read_csv(args.queries)
        queries = df_queries["query"].tolist()  # Assume 'query' column
    else:
        queries = [q.strip() for q in args.queries.split(",")]

    # Load content
    try:
        with open(args.content, "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = args.content

    # Load competitors
    competitors = []
    for comp_path in args.competitors.split(","):
        try:
            with open(comp_path.strip(), "r") as f:
                competitors.append(f.read())
        except FileNotFoundError:
            competitors.append(comp_path.strip())

    # Generate report
    df_gaps = generate_gap_report(queries, content, competitors, args.num_clusters)
    df_gaps.to_csv(args.output_csv, index=False)
    print(f"Gap report saved to {args.output_csv}")