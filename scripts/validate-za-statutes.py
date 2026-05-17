#!/usr/bin/env python3
"""Validate ZA statute YAML files against the shared schema.

Usage: validate-za-statutes.py
Discovers all .yaml files under jurisdictions/za/statutes/, validates each
against scripts/za-statute-schema.yaml, and checks temporal integrity.

Exits 0 if all valid, 1 if any invalid or no files found.
"""
import sys
from pathlib import Path

import jsonschema
import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "scripts" / "za-statute-schema.yaml"
STATUTES_DIR = REPO_ROOT / "jurisdictions" / "za" / "statutes"


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text())


def check_temporal_integrity(data: dict) -> list[str]:
    """Check that effective_until is not before effective_from in any section."""
    errors = []
    for name, section in data.get("sections", {}).items():
        eff_from = section.get("effective_from")
        eff_until = section.get("effective_until")
        if eff_from is not None and eff_until is not None:
            if eff_until < eff_from:
                errors.append(
                    f"  {name}: effective_until ({eff_until}) is before "
                    f"effective_from ({eff_from})"
                )
    return errors


def main() -> int:
    schema = load_yaml(SCHEMA_PATH)
    files = sorted(STATUTES_DIR.glob("*.yaml"))

    if not files:
        print("FAIL: no .yaml files found in", STATUTES_DIR, file=sys.stderr)
        return 1

    ok = True
    for path in files:
        rel = path.relative_to(REPO_ROOT)
        data = load_yaml(path)

        # Schema validation
        try:
            jsonschema.validate(instance=data, schema=schema)
        except jsonschema.ValidationError as e:
            json_path = "/".join(str(p) for p in e.absolute_path)
            print(f"FAIL: {rel} — {e.message} at {json_path}", file=sys.stderr)
            ok = False
            continue

        # Temporal integrity
        temporal_errors = check_temporal_integrity(data)
        if temporal_errors:
            print(f"FAIL: {rel} — temporal integrity errors:", file=sys.stderr)
            for err in temporal_errors:
                print(err, file=sys.stderr)
            ok = False
            continue

        print(f"OK: {rel}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
