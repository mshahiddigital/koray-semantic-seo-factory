# browser_qa.py - Post-Deploy Technical SEO QA Checker
# Usage: python browser_qa.py --url "https://yoursite.com/page-slug" --checks "all"
# Usage: python browser_qa.py --url_list "deployed_pages.json" --output "qa_report.json"
# Outputs: JSON QA report { url, pass, score, checks, issues }
#
# Uses: requests + BeautifulSoup (no browser required)
# Optionally uses: Playwright for JS-rendered pages (if installed)
# Required: pip install requests beautifulsoup4 lxml

import argparse
import json
import sys
import time
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# HTTP fetch with retry
# ---------------------------------------------------------------------------

def fetch_page(url: str, timeout: int = 15, retries: int = 2) -> tuple[int, str, dict]:
    """Fetch a URL. Returns (status_code, html_content, headers)."""
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; KoraySEO-QA/1.0; +https://koray-seo-factory)"
    }
    for attempt in range(retries + 1):
        try:
            resp = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
            return resp.status_code, resp.text, dict(resp.headers)
        except requests.RequestException as e:
            if attempt == retries:
                return 0, "", {"error": str(e)}
            time.sleep(2)
    return 0, "", {}


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------

def check_http_status(status_code: int) -> dict:
    """Check that the page returns 200 OK."""
    passed = status_code == 200
    return {
        "check": "http_status",
        "passed": passed,
        "severity": "critical",
        "value": status_code,
        "message": "Page returns 200 OK" if passed else f"Page returned HTTP {status_code} — not indexable",
    }


def check_h1(soup: BeautifulSoup) -> dict:
    """Check that exactly one H1 exists and is not empty."""
    h1_tags = soup.find_all("h1")
    count = len(h1_tags)
    if count == 1:
        h1_text = h1_tags[0].get_text(strip=True)
        passed = bool(h1_text)
        return {
            "check": "h1",
            "passed": passed,
            "severity": "critical",
            "value": h1_text[:100],
            "message": f"H1 present: '{h1_text[:80]}'" if passed else "H1 tag exists but is empty",
        }
    elif count == 0:
        return {
            "check": "h1",
            "passed": False,
            "severity": "critical",
            "value": None,
            "message": "No H1 tag found — required for entity prominence",
        }
    else:
        h1_texts = [t.get_text(strip=True) for t in h1_tags]
        return {
            "check": "h1",
            "passed": False,
            "severity": "high",
            "value": h1_texts,
            "message": f"Multiple H1 tags found ({count}) — reduces entity clarity",
        }


def check_title_tag(soup: BeautifulSoup) -> dict:
    """Check that <title> tag exists and is not empty."""
    title = soup.find("title")
    if title:
        text = title.get_text(strip=True)
        passed = bool(text) and len(text) >= 10
        return {
            "check": "title_tag",
            "passed": passed,
            "severity": "high",
            "value": text[:100],
            "message": f"Title: '{text[:80]}'" if passed else "Title tag too short or empty",
        }
    return {
        "check": "title_tag",
        "passed": False,
        "severity": "high",
        "value": None,
        "message": "No <title> tag found",
    }


def check_meta_description(soup: BeautifulSoup) -> dict:
    """Check that meta description exists and is within length bounds."""
    meta = soup.find("meta", attrs={"name": "description"})
    if meta:
        content = meta.get("content", "").strip()
        length = len(content)
        passed = 50 <= length <= 160
        return {
            "check": "meta_description",
            "passed": passed,
            "severity": "medium",
            "value": content[:200],
            "message": (
                f"Meta description OK ({length} chars)"
                if passed
                else f"Meta description length is {length} chars (target: 50–160)"
            ),
        }
    return {
        "check": "meta_description",
        "passed": False,
        "severity": "medium",
        "value": None,
        "message": "No meta description tag found",
    }


def check_canonical(soup: BeautifulSoup, url: str) -> dict:
    """Check that canonical tag exists and points to the correct URL."""
    canonical = soup.find("link", attrs={"rel": "canonical"})
    if canonical:
        href = canonical.get("href", "").rstrip("/")
        expected = url.rstrip("/")
        passed = href == expected or href.rstrip("/") == expected.rstrip("/")
        return {
            "check": "canonical",
            "passed": passed,
            "severity": "high",
            "value": href,
            "message": (
                f"Canonical correctly points to {href}"
                if passed
                else f"Canonical mismatch: found '{href}', expected '{expected}'"
            ),
        }
    return {
        "check": "canonical",
        "passed": False,
        "severity": "high",
        "value": None,
        "message": "No canonical tag found — duplicate content risk",
    }


def check_schema_json_ld(soup: BeautifulSoup) -> dict:
    """Check that at least one valid JSON-LD schema block exists in the DOM."""
    scripts = soup.find_all("script", attrs={"type": "application/ld+json"})
    if not scripts:
        return {
            "check": "schema_json_ld",
            "passed": False,
            "severity": "high",
            "value": None,
            "message": "No JSON-LD schema blocks found in DOM",
        }

    types_found = []
    parse_errors = []

    for script in scripts:
        try:
            data = json.loads(script.string or "")
            schema_type = data.get("@type", "unknown")
            if isinstance(schema_type, list):
                types_found.extend(schema_type)
            else:
                types_found.append(schema_type)
        except json.JSONDecodeError as e:
            parse_errors.append(str(e))

    passed = len(parse_errors) == 0 and len(types_found) > 0
    return {
        "check": "schema_json_ld",
        "passed": passed,
        "severity": "high",
        "value": types_found,
        "message": (
            f"Schema found: {', '.join(types_found)}"
            if passed
            else f"Schema parse errors: {'; '.join(parse_errors)}"
        ),
    }


def check_heading_hierarchy(soup: BeautifulSoup) -> dict:
    """Check that heading hierarchy is logical (H1 → H2 → H3, no skips)."""
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    issues = []
    prev_level = 0
    for h in headings:
        level = int(h.name[1])
        if level > prev_level + 1 and prev_level > 0:
            issues.append(f"Heading skip: H{prev_level} → H{level} ('{h.get_text(strip=True)[:50]}')")
        prev_level = level

    passed = len(issues) == 0
    return {
        "check": "heading_hierarchy",
        "passed": passed,
        "severity": "medium",
        "value": [h.name for h in headings],
        "message": "Heading hierarchy is logical" if passed else f"Hierarchy issues: {'; '.join(issues[:3])}",
    }


def check_images_alt(soup: BeautifulSoup) -> dict:
    """Check that all <img> tags have non-empty alt attributes."""
    images = soup.find_all("img")
    if not images:
        return {
            "check": "images_alt",
            "passed": True,
            "severity": "low",
            "value": 0,
            "message": "No images found on page",
        }
    missing = [img.get("src", "")[:60] for img in images if not img.get("alt", "").strip()]
    passed = len(missing) == 0
    return {
        "check": "images_alt",
        "passed": passed,
        "severity": "medium",
        "value": {"total": len(images), "missing_alt": len(missing)},
        "message": (
            f"All {len(images)} images have alt text"
            if passed
            else f"{len(missing)} of {len(images)} images missing alt text"
        ),
    }


def check_internal_links(soup: BeautifulSoup, base_domain: str) -> dict:
    """Check that internal links exist and have non-generic anchor text."""
    all_links = soup.find_all("a", href=True)
    internal = [a for a in all_links if base_domain in a.get("href", "") or a.get("href", "").startswith("/")]
    generic_anchors = {"click here", "read more", "here", "this", "learn more", "more"}
    weak = [a.get_text(strip=True) for a in internal if a.get_text(strip=True).lower() in generic_anchors]

    passed = len(internal) > 0 and len(weak) == 0
    return {
        "check": "internal_links",
        "passed": passed,
        "severity": "medium",
        "value": {"internal_count": len(internal), "weak_anchors": weak},
        "message": (
            f"{len(internal)} internal links found with descriptive anchors"
            if passed
            else f"{len(internal)} internal links found; {len(weak)} with generic anchor text"
        ),
    }


def check_robots_meta(soup: BeautifulSoup) -> dict:
    """Check that robots meta does not block indexing."""
    robots = soup.find("meta", attrs={"name": "robots"})
    if robots:
        content = robots.get("content", "").lower()
        blocking = "noindex" in content or "nofollow" in content
        return {
            "check": "robots_meta",
            "passed": not blocking,
            "severity": "critical",
            "value": content,
            "message": (
                f"Robots meta: {content}"
                if not blocking
                else f"Page is blocked: robots meta contains '{content}'"
            ),
        }
    return {
        "check": "robots_meta",
        "passed": True,
        "severity": "low",
        "value": "no robots meta tag — default allows indexing",
        "message": "No robots meta tag — indexing allowed by default",
    }


def check_page_speed_signals(headers: dict) -> dict:
    """Check server-level performance signals from response headers."""
    issues = []
    value = {}

    # Check compression
    encoding = headers.get("Content-Encoding", "").lower()
    if encoding in ("gzip", "br", "zstd"):
        value["compression"] = encoding
    else:
        issues.append(f"No compression detected (Content-Encoding: {encoding or 'none'})")

    # Check caching
    cache_control = headers.get("Cache-Control", "")
    if cache_control:
        value["cache_control"] = cache_control
    else:
        issues.append("No Cache-Control header — browser caching may not be configured")

    passed = len(issues) == 0
    return {
        "check": "page_speed_signals",
        "passed": passed,
        "severity": "medium",
        "value": value,
        "message": (
            f"Compression: {value.get('compression', 'none')}; Cache-Control: {value.get('cache_control', 'none')}"
            if passed
            else "; ".join(issues)
        ),
    }


# ---------------------------------------------------------------------------
# Full QA run for a single URL
# ---------------------------------------------------------------------------

def run_qa(url: str) -> dict:
    """Run all QA checks on a single URL. Returns full QA report."""
    status_code, html, headers = fetch_page(url)
    parsed = urlparse(url)
    base_domain = parsed.netloc

    checks = []

    # HTTP status — if failed, skip DOM checks
    status_check = check_http_status(status_code)
    checks.append(status_check)

    if not status_check["passed"]:
        return {
            "url": url,
            "passed": False,
            "score": 0,
            "checks": checks,
            "issues": [f"HTTP {status_code} — page not reachable, all DOM checks skipped"],
        }

    soup = BeautifulSoup(html, "lxml")

    checks.extend([
        check_robots_meta(soup),
        check_h1(soup),
        check_title_tag(soup),
        check_meta_description(soup),
        check_canonical(soup, url),
        check_schema_json_ld(soup),
        check_heading_hierarchy(soup),
        check_images_alt(soup),
        check_internal_links(soup, base_domain),
        check_page_speed_signals(headers),
    ])

    # Score: weighted by severity
    severity_weights = {"critical": 3, "high": 2, "medium": 1, "low": 0.5}
    total_weight = sum(severity_weights.get(c["severity"], 1) for c in checks)
    passed_weight = sum(
        severity_weights.get(c["severity"], 1)
        for c in checks if c["passed"]
    )
    score = round((passed_weight / total_weight) * 100) if total_weight > 0 else 0

    issues = [
        f"[{c['severity'].upper()}] {c['message']}"
        for c in checks if not c["passed"]
    ]

    return {
        "url": url,
        "passed": score >= 80,
        "score": score,
        "checks": checks,
        "issues": issues,
    }


# ---------------------------------------------------------------------------
# Batch QA run
# ---------------------------------------------------------------------------

def run_batch_qa(url_list: list) -> dict:
    """Run QA on a list of URLs. Returns aggregate report."""
    results = []
    for url in url_list:
        print(f"Checking: {url}", file=sys.stderr)
        result = run_qa(url)
        results.append(result)
        time.sleep(0.5)  # Polite crawl rate

    passing = [r for r in results if r["passed"]]
    failing = [r for r in results if not r["passed"]]
    avg_score = round(sum(r["score"] for r in results) / len(results)) if results else 0

    return {
        "total": len(results),
        "passed": len(passing),
        "failed": len(failing),
        "average_score": avg_score,
        "results": results,
        "critical_failures": [r["url"] for r in failing if r["score"] < 50],
    }


# ---------------------------------------------------------------------------
# CLI interface
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Post-deploy Technical SEO QA Checker")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", type=str, help="Single URL to check")
    group.add_argument("--url_list", type=str, help="JSON file with list of URLs to check")
    parser.add_argument("--output", type=str, default=None, help="Save report to JSON file")
    args = parser.parse_args()

    if args.url:
        result = run_qa(args.url)
        output = result
    else:
        with open(args.url_list, "r", encoding="utf-8") as f:
            data = json.load(f)
        urls = data if isinstance(data, list) else [r["url"] for r in data.get("results", [])]
        output = run_batch_qa(urls)

    output_json = json.dumps(output, indent=2, ensure_ascii=False)
    print(output_json)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_json)
        print(f"QA report saved to {args.output}", file=sys.stderr)

    # Exit: 0 = all passed, 1 = some failed
    passed = output.get("passed", False) if args.url else output.get("failed", 0) == 0
    sys.exit(0 if passed else 1)
