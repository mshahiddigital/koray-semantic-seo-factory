# coverage_auditor.py - Koray Coverage Auditor v2.1
# Chains entity_extractor + topicality_scorer

from entity_extractor import extract_eav
from topicality_scorer import score_topicality

def audit_coverage(my_content, comp_contents):
    my_eav = extract_eav(my_content)
    scores = score_topicality(my_content, comp_contents)
    coverage_pct = len(my_eav) / sum([len(extract_eav(c)) for c in comp_contents]) * 100
    return {"Coverage %": coverage_pct, "Scores": scores}

# Argparse for full audit report