# schema_validator.py - Local JSON-LD Schema.org Validator
# Usage: python schema_validator.py --schema_file "schema.json"
# Usage: python schema_validator.py --schema_json '{"@type": "FAQPage", ...}'
# Outputs: JSON result { valid: bool, score, errors, warnings, types_found }
#
# Validates against Schema.org required properties — no external API needed.
# Supports: LocalBusiness, FAQPage, HowTo, Article, Product, Organization,
#           BreadcrumbList, MedicalClinic, Service, Person

import argparse
import json
import sys
from typing import Any


# ---------------------------------------------------------------------------
# Required property definitions per Schema.org type
# ---------------------------------------------------------------------------

REQUIRED_PROPERTIES = {
    "LocalBusiness": {
        "required": ["name", "address"],
        "recommended": ["telephone", "url", "openingHours", "geo", "priceRange"],
        "address_required": ["streetAddress", "addressLocality", "addressCountry"],
    },
    "MedicalClinic": {
        "required": ["name", "address", "medicalSpecialty"],
        "recommended": ["telephone", "url", "openingHours", "availableService"],
        "address_required": ["streetAddress", "addressLocality", "addressCountry"],
    },
    "FAQPage": {
        "required": ["mainEntity"],
        "recommended": [],
        "mainEntity_required": ["@type", "name", "acceptedAnswer"],
        "acceptedAnswer_required": ["@type", "text"],
    },
    "HowTo": {
        "required": ["name", "step"],
        "recommended": ["totalTime", "estimatedCost", "supply", "tool"],
        "step_required": ["@type", "text"],
    },
    "Article": {
        "required": ["headline", "author", "datePublished"],
        "recommended": ["publisher", "dateModified", "image", "description"],
        "author_required": ["@type", "name"],
        "publisher_required": ["@type", "name"],
    },
    "BlogPosting": {
        "required": ["headline", "author", "datePublished"],
        "recommended": ["publisher", "dateModified", "image", "description"],
        "author_required": ["@type", "name"],
    },
    "Product": {
        "required": ["name"],
        "recommended": ["description", "image", "brand", "offers", "aggregateRating"],
        "offers_required": ["@type", "price", "priceCurrency"],
    },
    "Organization": {
        "required": ["name"],
        "recommended": ["url", "logo", "contactPoint", "sameAs"],
    },
    "BreadcrumbList": {
        "required": ["itemListElement"],
        "itemListElement_required": ["@type", "position", "name", "item"],
    },
    "Service": {
        "required": ["name", "provider"],
        "recommended": ["description", "areaServed", "serviceType", "offers"],
    },
    "Person": {
        "required": ["name"],
        "recommended": ["url", "jobTitle", "affiliation", "sameAs"],
    },
    "WebPage": {
        "required": ["name"],
        "recommended": ["url", "description", "breadcrumb"],
    },
    "WebSite": {
        "required": ["name", "url"],
        "recommended": ["potentialAction", "sameAs"],
    },
    "ItemList": {
        "required": ["itemListElement"],
        "itemListElement_required": ["@type", "position"],
    },
    "Event": {
        "required": ["name", "startDate", "location"],
        "recommended": ["endDate", "description", "organizer", "offers"],
    },
    "Recipe": {
        "required": ["name", "recipeIngredient", "recipeInstructions"],
        "recommended": ["author", "datePublished", "image", "description", "prepTime", "cookTime"],
    },
    "Review": {
        "required": ["itemReviewed", "reviewRating", "author"],
        "recommended": ["datePublished", "reviewBody"],
        "reviewRating_required": ["@type", "ratingValue"],
    },
}

# Types that should not be used standalone (always embedded)
EMBEDDED_ONLY_TYPES = {"PostalAddress", "ContactPoint", "GeoCoordinates", "Offer",
                       "AggregateRating", "Question", "Answer", "ListItem", "HowToStep"}


# ---------------------------------------------------------------------------
# Validation logic
# ---------------------------------------------------------------------------

def get_schema_type(schema: dict) -> str:
    """Extract the @type from a schema dict, handling arrays."""
    schema_type = schema.get("@type", "")
    if isinstance(schema_type, list):
        # Return the most specific known type
        for t in schema_type:
            if t in REQUIRED_PROPERTIES:
                return t
        return schema_type[0] if schema_type else ""
    return schema_type


def validate_address(address: Any) -> list:
    """Validate PostalAddress sub-object."""
    errors = []
    if isinstance(address, str):
        return []  # Plain string address is acceptable but not ideal
    if isinstance(address, dict):
        addr_required = REQUIRED_PROPERTIES["LocalBusiness"]["address_required"]
        for field in addr_required:
            if field not in address:
                errors.append(f"address.{field} is missing (required for rich results)")
    return errors


def validate_faq_entities(entities: Any) -> list:
    """Validate FAQPage mainEntity array."""
    errors = []
    if not isinstance(entities, list):
        entities = [entities]
    for i, entity in enumerate(entities):
        if not isinstance(entity, dict):
            errors.append(f"mainEntity[{i}] must be an object")
            continue
        if entity.get("@type") != "Question":
            errors.append(f"mainEntity[{i}].@type must be 'Question'")
        if "name" not in entity:
            errors.append(f"mainEntity[{i}].name (the question text) is missing")
        answer = entity.get("acceptedAnswer", {})
        if not isinstance(answer, dict):
            errors.append(f"mainEntity[{i}].acceptedAnswer must be an object")
        elif "text" not in answer:
            errors.append(f"mainEntity[{i}].acceptedAnswer.text is missing")
    return errors


def validate_howto_steps(steps: Any) -> list:
    """Validate HowTo step array."""
    errors = []
    if not isinstance(steps, list):
        errors.append("HowTo.step must be an array")
        return errors
    for i, step in enumerate(steps):
        if not isinstance(step, dict):
            errors.append(f"step[{i}] must be an object")
            continue
        if "text" not in step and "itemListElement" not in step:
            errors.append(f"step[{i}].text or step[{i}].itemListElement is required")
    return errors


def validate_breadcrumb_items(items: Any) -> list:
    """Validate BreadcrumbList itemListElement array."""
    errors = []
    if not isinstance(items, list):
        errors.append("BreadcrumbList.itemListElement must be an array")
        return errors
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"itemListElement[{i}] must be an object")
            continue
        if "position" not in item:
            errors.append(f"itemListElement[{i}].position is required")
        if "name" not in item:
            errors.append(f"itemListElement[{i}].name is required")
    return errors


def validate_single_schema(schema: dict) -> dict:
    """Validate a single schema object. Returns { valid, errors, warnings, type }."""
    errors = []
    warnings = []

    # Check @context
    context = schema.get("@context", "")
    if "schema.org" not in str(context):
        errors.append('@context must contain "schema.org" (e.g. "https://schema.org")')

    schema_type = get_schema_type(schema)

    if not schema_type:
        errors.append("@type is missing — required for all Schema.org markup")
        return {"valid": False, "errors": errors, "warnings": warnings, "type": "unknown"}

    if schema_type in EMBEDDED_ONLY_TYPES:
        warnings.append(f"{schema_type} is typically embedded inside another schema, not used standalone")

    rules = REQUIRED_PROPERTIES.get(schema_type)
    if not rules:
        warnings.append(f"@type '{schema_type}' is not in the validator's known types — manual review recommended")
        return {"valid": True, "errors": errors, "warnings": warnings, "type": schema_type}

    # Check required properties
    for prop in rules.get("required", []):
        if prop not in schema:
            errors.append(f"{schema_type}.{prop} is required but missing")

    # Check recommended properties (warnings only)
    for prop in rules.get("recommended", []):
        if prop not in schema:
            warnings.append(f"{schema_type}.{prop} is recommended for better rich result eligibility")

    # Type-specific deep validation
    if schema_type in ("LocalBusiness", "MedicalClinic") and "address" in schema:
        errors.extend(validate_address(schema["address"]))

    if schema_type == "FAQPage" and "mainEntity" in schema:
        errors.extend(validate_faq_entities(schema["mainEntity"]))

    if schema_type == "HowTo" and "step" in schema:
        errors.extend(validate_howto_steps(schema["step"]))

    if schema_type == "BreadcrumbList" and "itemListElement" in schema:
        errors.extend(validate_breadcrumb_items(schema["itemListElement"]))

    if schema_type == "Article" and "datePublished" in schema:
        date = schema["datePublished"]
        if len(date) < 10:
            warnings.append("datePublished should be ISO 8601 format (YYYY-MM-DD or full datetime)")

    # Author validation for Article types
    if schema_type in ("Article", "BlogPosting") and "author" in schema:
        author = schema["author"]
        if isinstance(author, dict) and "@type" not in author:
            errors.append("Article.author must have @type (Person or Organization)")

    valid = len(errors) == 0
    return {"valid": valid, "errors": errors, "warnings": warnings, "type": schema_type}


# ---------------------------------------------------------------------------
# Multi-schema page validator
# ---------------------------------------------------------------------------

def validate_page_schemas(schemas: list | dict) -> dict:
    """Validate all schema blocks on a page.

    Accepts: a single schema dict or a list of schema dicts.
    Returns: { valid, score, types_found, results, total_errors, total_warnings }
    """
    if isinstance(schemas, dict):
        schemas = [schemas]

    results = []
    all_errors = []
    all_warnings = []
    types_found = []

    for i, schema in enumerate(schemas):
        result = validate_single_schema(schema)
        result["index"] = i
        results.append(result)
        all_errors.extend(result["errors"])
        all_warnings.extend(result["warnings"])
        types_found.append(result["type"])

    total = len(results)
    passing = sum(1 for r in results if r["valid"])
    score = round((passing / total) * 100) if total > 0 else 0

    return {
        "valid": len(all_errors) == 0,
        "score": score,
        "types_found": types_found,
        "results": results,
        "total_errors": len(all_errors),
        "total_warnings": len(all_warnings),
        "errors": all_errors,
        "warnings": all_warnings,
    }


# ---------------------------------------------------------------------------
# CLI interface
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate JSON-LD Schema.org markup locally")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--schema_file", type=str, help="Path to JSON file containing schema(s)")
    group.add_argument("--schema_json", type=str, help="Inline JSON string of schema(s)")
    parser.add_argument("--output", type=str, default=None, help="Save results to JSON file")
    args = parser.parse_args()

    if args.schema_file:
        with open(args.schema_file, "r", encoding="utf-8") as f:
            schemas = json.load(f)
    else:
        schemas = json.loads(args.schema_json)

    result = validate_page_schemas(schemas)
    output_json = json.dumps(result, indent=2, ensure_ascii=False)
    print(output_json)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_json)
        print(f"Validation results saved to {args.output}", file=sys.stderr)

    # Exit code: 0 = valid, 1 = invalid (allows shell scripting)
    sys.exit(0 if result["valid"] else 1)
