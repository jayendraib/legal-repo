#!/usr/bin/env python3
"""Validate the ZA skill router's cross-references.

Usage: validate-za-router.py
Reads jurisdictions/za/employment-legal/router.md, extracts the embedded YAML
block, and verifies that every skill directory, topic file, and statute file
referenced in the router actually exists.

Also warns about orphaned topic files (present on disk but not referenced by
any skill in the router).

Exits 0 if all references resolve, 1 if any are missing or the router cannot
be parsed.
"""
import re
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
ROUTER_PATH = REPO_ROOT / "jurisdictions" / "za" / "employment-legal" / "router.md"
SKILLS_DIR = REPO_ROOT / "employment-legal" / "skills"
TOPICS_DIR = REPO_ROOT / "jurisdictions" / "za" / "employment-legal" / "topics"
STATUTES_DIR = REPO_ROOT / "jurisdictions" / "za" / "statutes"

YAML_FENCE = re.compile(r"```yaml\s*\n(.*?)```", re.DOTALL)


def extract_yaml(text: str) -> str | None:
    """Return the first fenced YAML block from markdown text."""
    m = YAML_FENCE.search(text)
    return m.group(1) if m else None


def main() -> int:
    if not ROUTER_PATH.exists():
        print(f"FAIL: router file not found: {ROUTER_PATH}", file=sys.stderr)
        return 1

    raw = ROUTER_PATH.read_text()
    yaml_text = extract_yaml(raw)
    if yaml_text is None:
        print("FAIL: no ```yaml``` block found in router.md", file=sys.stderr)
        return 1

    try:
        router = yaml.safe_load(yaml_text)
    except yaml.YAMLError as e:
        print(f"FAIL: YAML parse error in router.md: {e}", file=sys.stderr)
        return 1

    if not isinstance(router, dict) or len(router) == 0:
        print("FAIL: router YAML must be a non-empty mapping", file=sys.stderr)
        return 1

    errors: list[str] = []
    all_referenced_topics: set[str] = set()

    for skill, refs in router.items():
        # Skill directory
        skill_dir = SKILLS_DIR / skill
        if not skill_dir.is_dir():
            errors.append(f"{skill}: skill directory not found: {skill_dir.relative_to(REPO_ROOT)}")

        if not isinstance(refs, dict):
            errors.append(f"{skill}: expected a mapping with 'topics' and 'statutes'")
            continue

        # Topic files
        for topic in refs.get("topics", []):
            all_referenced_topics.add(topic)
            topic_file = TOPICS_DIR / f"{topic}.md"
            if not topic_file.exists():
                errors.append(f"{skill}: topic file not found: {topic_file.relative_to(REPO_ROOT)}")

        # Statute files
        for statute in refs.get("statutes", []):
            statute_file = STATUTES_DIR / f"{statute}.yaml"
            if not statute_file.exists():
                errors.append(f"{skill}: statute file not found: {statute_file.relative_to(REPO_ROOT)}")

    if errors:
        print("FAIL: router cross-reference errors", file=sys.stderr)
        for err in errors:
            print(f"  {err}", file=sys.stderr)
        return 1

    # Warn about orphaned topic files
    existing_topics = {p.stem for p in TOPICS_DIR.glob("*.md")}
    orphaned = sorted(existing_topics - all_referenced_topics)
    for name in orphaned:
        print(f"WARN: orphaned topic file not referenced by any skill: topics/{name}.md")

    skill_count = len(router)
    print(f"OK: {skill_count} skills, all references resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
