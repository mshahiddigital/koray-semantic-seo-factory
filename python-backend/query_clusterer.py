# query_clusterer.py - Koray Query Network Clusterer v2.1
# Usage: python query_clusterer.py --queries "query1,query2" --output_csv "clusters.csv"

import argparse
import pandas as pd
from sentence_transformers import SentenceTransformer, util  # Semantic similarity
import numpy as np
from sklearn.cluster import KMeans  # Clustering

model = SentenceTransformer("all-MiniLM-L6-v2")  # Pre-installed

def cluster_queries(queries, num_clusters=5):
    """Cluster queries into networks using semantic embeddings."""
    embeddings = model.encode(queries)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(embeddings)
    
    clusters = []
    for i in range(num_clusters):
        cluster_queries = [q for q, l in zip(queries, labels) if l == i]
        clusters.append({"Cluster": i, "Queries": cluster_queries, "Centroid_Similarity": np.mean(util.cos_sim(embeddings)[labels == i])})
    
    return pd.DataFrame(clusters)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cluster queries")
    parser.add_argument("--queries", type=str, help="Comma-separated queries or CSV path")
    parser.add_argument("--num_clusters", type=int, default=5, help="Number of clusters")
    parser.add_argument("--output_csv", type=str, default="query_clusters.csv")
    args = parser.parse_args()
    
    if args.queries.endswith(".csv"):
        df = pd.read_csv(args.queries)
        queries = df["query"].tolist()  # Assume 'query' column
    else:
        queries = args.queries.split(",")
    
    df_clusters = cluster_queries(queries, args.num_clusters)
    df_clusters.to_csv(args.output_csv, index=False)
    print(f"Query clusters saved to {args.output_csv}")