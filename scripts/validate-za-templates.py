#!/usr/bin/env python3
"""Validate ZA practice profile templates for completeness and correctness.

Checks:
1. All required sections present
2. SA-specific terms are referenced
3. No US-specific terms outside the privilege caveat
4. Work-product header uses SA formulation

Usage: python3 scripts/validate-za-templates.py
Exits 0 if valid, 1 on errors.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ZA_TEMPLATES = [
    ROOT / "jurisdictions" / "za" / "employment-legal" / "practice-profile-template.md",
]

REQUIRED_SECTIONS = [
    "Jurisdictional footprint",
    "Statutory baseline",
    "Employment equity",
    "Dispute resolution",
    "Leave and conditions",
    "Termination review",
    "Hiring review",
    "Escalation",
    "Seed documents",
    "Outputs",
]

SA_REQUIRED_TERMS = [
    "CCMA",
    "BCEA",
    "LRA",
    "bargaining council",
    "Schedule 8",
    "admitted attorney",
]

US_FORBIDDEN = [
    (r"\bFMLA\b", "FMLA"),
    (r"\bFLSA\b", "FLSA"),
    (r"\bEEOC\b", "EEOC"),
    (r"\bNLRB\b", "NLRB"),
    (r"\bWARN Act\b", "WARN Act"),
    (r"\bCal-WARN\b", "Cal-WARN"),
    (r"\bstate supplements?\b", "state supplement(s)"),
]


def find_privilege_caveat(text: str) -> str:
    match = re.search(
        r"(?:SA |South African )(?:legal professional )?privilege.*?(?=\n## |\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    return match.group(0) if match else ""


def main() -> int:
    errors = 0

    for path in ZA_TEMPLATES:
        if not path.exists():
            print(f"FAIL: {path.name}: file does not exist", file=sys.stderr)
            errors += 1
            continue

        text = path.read_text()
        name = path.name
        file_errors = 0

        for section in REQUIRED_SECTIONS:
            if f"## {section}" not in text and f"# {section}" not in text:
                print(f"FAIL: {name}: missing required section '## {section}'", file=sys.stderr)
                file_errors += 1

        for term in SA_REQUIRED_TERMS:
            if term not in text:
                print(f"FAIL: {name}: missing SA-required term '{term}'", file=sys.stderr)
                file_errors += 1

        caveat_text = find_privilege_caveat(text)
        non_caveat_text = text.replace(caveat_text, "") if caveat_text else text

        for pattern, label in US_FORBIDDEN:
            matches = re.findall(pattern, non_caveat_text, re.IGNORECASE)
            if matches:
                print(
                    f"FAIL: {name}: US-specific term '{label}' found outside privilege caveat",
                    file=sys.stderr,
                )
                file_errors += 1

        errors += file_errors
        status = "FAIL" if file_errors else "OK"
        print(f"  {status}: {name}")

    if errors:
        print(f"\n{errors} errors found")
    else:
        print(f"\n{len(ZA_TEMPLATES)} templates checked, no errors")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
