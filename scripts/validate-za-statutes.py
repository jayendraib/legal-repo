#!/usr/bin/env python3
"""Validate ZA statute YAML files against the shared schema.

Usage: validate-za-statutes.py
Discovers all .yaml files under jurisdictions/za/statutes/, validates each
against the expected schema structure, and checks temporal integrity.

Exits 0 if all valid, 1 if any invalid or no files found.
"""
import re
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
STATUTES_DIR = REPO_ROOT / "jurisdictions" / "za" / "statutes"

REQUIRED_TOP_LEVEL = ["statute", "authority", "last_confirmed", "source_url", "sections"]
REQUIRED_SECTION_FIELDS = ["ref", "value", "effective_from", "effective_until", "effect"]
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate_statute(data: dict, filename: str) -> list[str]:
    errors = []

    for field in REQUIRED_TOP_LEVEL:
        if field not in data:
            errors.append(f"missing required top-level field: {field}")

    if "statute" in data and (not isinstance(data["statute"], str) or len(data["statute"]) < 5):
        errors.append("'statute' must be a string of at least 5 characters")

    if "last_confirmed" in data and isinstance(data["last_confirmed"], str):
        if not DATE_PATTERN.match(data["last_confirmed"]):
            errors.append(f"'last_confirmed' must match YYYY-MM-DD, got: {data['last_confirmed']}")

    if "source_url" in data and isinstance(data["source_url"], str):
        if not data["source_url"].startswith(("http://", "https://")):
            errors.append(f"'source_url' must start with http:// or https://, got: {data['source_url']}")

    sections = data.get("sections", {})
    if not isinstance(sections, dict) or len(sections) == 0:
        errors.append("'sections' must be a non-empty mapping")
        return errors

    for key, section in sections.items():
        if not isinstance(section, dict):
            errors.append(f"sections/{key}: must be a mapping")
            continue

        for field in REQUIRED_SECTION_FIELDS:
            if field not in section:
                errors.append(f"sections/{key}: missing required field: {field}")

        if "effect" in section and (not isinstance(section["effect"], str) or len(section["effect"]) < 5):
            errors.append(f"sections/{key}: 'effect' must be a string of at least 5 characters")

        if "currency" in section and section["currency"] != "ZAR":
            errors.append(f"sections/{key}: 'currency' must be 'ZAR', got: {section['currency']}")

        for date_field in ("effective_from", "effective_until", "gazette_date"):
            val = section.get(date_field)
            if val is not None and isinstance(val, str) and not DATE_PATTERN.match(val):
                errors.append(f"sections/{key}: '{date_field}' must be null or YYYY-MM-DD, got: {val}")

        eff_from = section.get("effective_from")
        eff_until = section.get("effective_until")
        if eff_from is not None and eff_until is not None:
            if eff_until < eff_from:
                errors.append(
                    f"sections/{key}: effective_until ({eff_until}) is before "
                    f"effective_from ({eff_from})"
                )

    return errors


def main() -> int:
    files = sorted(STATUTES_DIR.glob("*.yaml"))

    if not files:
        print(f"FAIL: no .yaml files found in {STATUTES_DIR}", file=sys.stderr)
        return 1

    all_ok = True
    for path in files:
        rel = path.relative_to(REPO_ROOT)
        try:
            data = yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            print(f"FAIL: {rel} — YAML parse error: {e}", file=sys.stderr)
            all_ok = False
            continue

        errors = validate_statute(data, path.name)
        if errors:
            print(f"FAIL: {rel}", file=sys.stderr)
            for err in errors:
                print(f"  {err}", file=sys.stderr)
            all_ok = False
        else:
            section_count = len(data.get("sections", {}))
            print(f"OK: {rel} ({section_count} sections)")

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
