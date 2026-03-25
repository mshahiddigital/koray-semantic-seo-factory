# eav_triple_generator.py - Koray EAV Generator v2.1
# Usage: python eav_triple_generator.py --seed_entity "Electric Scooter" --depth 10

import argparse
import pandas as pd
import advertools as adv  # For KG queries
import networkx as nx  # For relation graphs

def generate_eav(seed_entity, depth=5):
    """Generate EAV triples using advertools KG + graph expansion."""
    kg = adv.knowledge_graph(seed_entity)  # Proxy KG
    G = nx.Graph()
    for triple in kg.get("triples", []):
        G.add_edge(triple["subject"], triple["object"], attr=triple["predicate"])
    
    eav = []
    for node in list(G.nodes)[:depth]:
        attrs = [e[2]["attr"] for e in G.edges(node, data=True)]
        eav.append({"Entity": node, "Attribute": attrs[0] if attrs else "N/A", "Value": "Generated"})
    
    return pd.DataFrame(eav)

# Argparse similar to above