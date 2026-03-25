# semantic_similarity_calculator.py - Koray Semantic Distance Calculator v2.1

import argparse
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(terms1, terms2):
    emb1 = model.encode(terms1)
    emb2 = model.encode(terms2)
    sims = util.cos_sim(emb1, emb2)
    return sims.numpy().tolist()

# Argparse for lists/CSV input