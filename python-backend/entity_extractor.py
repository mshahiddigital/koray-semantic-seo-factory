# entity_extractor.py - Koray EAV Triple Extractor v2.1
# Usage: python entity_extractor.py --input_text "Your text here" --output_csv "entities.csv"
# Or via agent: Takes text/CSV, outputs EAV table

import argparse
import pandas as pd
import advertools as adv  # For entity extraction
import spacy  # For advanced NLP
from nltk import word_tokenize  # Basic tokenization

nlp = spacy.load("en_core_web_sm")  # Load spaCy model (pre-installed)

def extract_eav(text):
    """Extract Entity-Attribute-Value triples from text."""
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        # Simple EAV: Entity = ent.text, Attribute = context, Value = nearby nums/adjs
        attr = " ".join([t.text for t in ent.root.head.children if t.dep_ in ["amod", "attr"]])
        value = " ".join([t.text for t in ent.root.children if t.dep_ in ["nummod", "dobj"]])
        entities.append({"Entity": ent.text, "Attribute": attr, "Value": value, "Source": "spaCy"})
    
    # Advertools fallback for KG entities
    adv_entities = adv.extract_entities(text)
    for e in adv_entities.get("entities", []):
        entities.append({"Entity": e, "Attribute": "Prominence", "Value": adv_entities["entity_freq"].get(e, 1), "Source": "advertools"})
    
    return pd.DataFrame(entities)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract EAV triples")
    parser.add_argument("--input_text", type=str, help="Input text or file path")
    parser.add_argument("--output_csv", type=str, default="eav_triples.csv", help="Output CSV")
    args = parser.parse_args()
    
    if args.input_text:
        try:
            with open(args.input_text, "r") as f:
                text = f.read()
        except:
            text = args.input_text
        df = extract_eav(text)
        df.to_csv(args.output_csv, index=False)
        print(f"EAV triples saved to {args.output_csv}")
    else:
        print("Provide --input_text")