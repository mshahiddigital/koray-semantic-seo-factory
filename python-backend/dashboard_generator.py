# dashboard_generator.py - Koray KPI Dashboard Generator v2.3
# Usage: python dashboard_generator.py --data_csv "scores.csv" --output_png "dashboard.png"

import argparse
import pandas as pd
import matplotlib.pyplot as plt

def generate_dashboard(data_csv):
    """Generate visual dashboard for Topical Authority KPIs."""
    df = pd.read_csv(data_csv)  # Assume columns: Score, Component, Date
    fig, ax = plt.subplots()
    ax.bar(df['Component'], df['Score'])
    ax.set_title("Topical Authority Dashboard")
    ax.set_ylabel("Score /100")
    return fig

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate KPI dashboard PNG")
    parser.add_argument("--data_csv", type=str, required=True, help="CSV with scores e.g. component,score,date")
    parser.add_argument("--output_png", type=str, default="dashboard.png")
    args = parser.parse_args()
    
    fig = generate_dashboard(args.data_csv)
    fig.savefig(args.output_png)
    print(f"Dashboard saved to {args.output_png}")