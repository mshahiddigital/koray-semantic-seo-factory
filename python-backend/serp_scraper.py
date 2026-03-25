# serp_scraper.py - Koray SERP Scraper v2.1
# Usage: python serp_scraper.py --query "electric scooters pakistan" --output_csv "serp.csv"

import argparse
import advertools as adv
import pandas as pd

def scrape_serp(query):
    """Scrape SERP using advertools (no real internet needed via proxy)."""
    df = adv.serp_goog(q=query, cx="your-cx", key="your-key")  # Use env keys
    return df[["rank", "title", "displayed_link", "snippet"]]

# Argparse to save CSV