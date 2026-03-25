# topicality_scorer.py - Koray Topical Authority Scorer v2.1
# Usage: python topicality_scorer.py --content "Your page text" --competitors "comp1.txt,comp2.txt"

import argparse
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def score_topicality(content, competitors):
    """Proxy score for Topical Authority: Coverage (similarity) × Historical (length proxy) × Retrieval (entity density)."""
    emb_content = model.encode(content)
    scores = []
    for comp in competitors:
        emb_comp = model.encode(comp)
        coverage = util.cos_sim(emb_content, emb_comp)[0][0] * 100  # Similarity %
        historical = len(content.split()) / 1000  # Words as proxy
        retrieval = len(adv.extract_entities(content)["entities"]) / len(content.split()) * 100  # Entity density
        total = coverage * historical * retrieval / 100  # Simplified formula
        scores.append({"Competitor": comp[:50], "Score": total})
    
    return pd.DataFrame(scores)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Score topical authority")
    parser.add_argument("--content", type=str, required=True, help="Your content text/file")
    parser.add_argument("--competitors", type=str, help="Comma-separated competitor texts/files")
    parser.add_argument("--output_csv", type=str, default="topical_scores.csv")
    args = parser.parse_args()
    
    with open(args.content, "r") if ".txt" in args.content else args.content as c:
        content = c if isinstance(c, str) else c.read()
    comps = []
    for comp in args.competitors.split(","):
        with open(comp.strip(), "r") as f:
            comps.append(f.read())
    
    df = score_topicality(content, comps)
    df.to_csv(args.output_csv, index=False)
    print(f"Topicality scores saved to {args.output_csv}")