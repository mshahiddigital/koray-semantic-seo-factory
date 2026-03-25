# research_compiler.py - Koray Research Sheet Compiler v2.3 (Updated)
# Usage: python research_compiler.py --input_json "workflow_data.json" --output_csv "research_sheet.csv"

import argparse
import json
import pandas as pd

def compile_research(input_data):
    """Compile all Koray workflow research into a single CSV sheet (enhanced for multi-tab proxy)."""
    sections = []
    # Flatten data (expanded structure)
    sections.append({'Section': 'Central Entity', 'Details': input_data.get('central_entity', 'N/A'), 'Sources': 'Mapper Agent', 'Score': input_data.get('prominence_score', 'N/A')})
    # Add Core/Outer with scores
    for section_type, sections in input_data.get('topical_map', {}).items():
        for sec in sections:
            sections.append({'Section': section_type, 'Details': str(sec), 'Sources': 'Mapper Agent', 'Score': sec.get('score', 'N/A')})
    # Add Query Clusters with gain
    for cluster in input_data.get('query_clusters', []):
        sections.append({'Section': 'Query Cluster', 'Details': str(cluster['Queries']), 'Sources': 'Researcher Agent', 'Score': cluster.get('Similarity', 'N/A')})
    # Add Gaps with priority
    for gap in input_data.get('gaps', []):
        sections.append({'Section': 'Semantic Gap', 'Details': str(gap), 'Sources': 'Researcher Agent', 'Score': gap.get('Info_Gain', 'N/A')})
    # Add Scores
    sections.append({'Section': 'Topical Authority Score', 'Details': input_data.get('topical_score', 'N/A'), 'Sources': 'Auditor Agent', 'Score': '-'})
    
    df = pd.DataFrame(sections)
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile Koray research into CSV sheet (enhanced)")
    parser.add_argument("--input_json", type=str, required=True, help="JSON file/path with workflow data")
    parser.add_argument("--output_csv", type=str, default="research_sheet.csv", help="Output CSV")
    args = parser.parse_args()
    
    with open(args.input_json, "r") as f:
        input_data = json.load(f)
    
    df = compile_research(input_data)
    df.to_csv(args.output_csv, index=False)
    print(f"Enhanced research sheet saved to {args.output_csv}")
    print(df.to_csv(index=False))  # Print for chat copy