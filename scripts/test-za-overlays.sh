#!/usr/bin/env bash
# Run all ZA overlay validation checks.
# Usage: bash scripts/test-za-overlays.sh
# Exits 0 if all pass, 1 if any fail.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$SCRIPT_DIR")"
ERRORS=0

echo "=== ZA Overlay Validation ==="
echo ""

echo "--- 1. Statute YAML schema ---"
if python3 "$SCRIPT_DIR/validate-za-statutes.py"; then
    echo "PASS: statute validation"
else
    echo "FAIL: statute validation"
    ERRORS=$((ERRORS + 1))
fi
echo ""

echo "--- 2. Router cross-references ---"
if python3 "$SCRIPT_DIR/validate-za-router.py"; then
    echo "PASS: router validation"
else
    echo "FAIL: router validation"
    ERRORS=$((ERRORS + 1))
fi
echo ""

echo "--- 3. Template completeness ---"
if python3 "$SCRIPT_DIR/validate-za-templates.py"; then
    echo "PASS: template validation"
else
    echo "FAIL: template validation"
    ERRORS=$((ERRORS + 1))
fi
echo ""

echo "--- 4. US concept leak check ---"
US_CONCEPTS='FMLA|FLSA|at.will employment|EEOC|NLRB|WARN Act|Cal-WARN|PAGA'
LEAKS=$(grep -rinE "$US_CONCEPTS" \
    "$ROOT/jurisdictions/za/employment-legal/topics/" \
    "$ROOT/jurisdictions/za/statutes/" \
    2>/dev/null || true)

# Filter out legitimate references in privilege caveat explanations
FILTERED=$(echo "$LEAKS" | grep -v "privilege" | grep -v "FRCP" | grep -v "^$" || true)

if [ -n "$FILTERED" ]; then
    echo "FAIL: US concepts found in ZA overlay files:"
    echo "$FILTERED"
    ERRORS=$((ERRORS + 1))
else
    echo "PASS: no US concept leaks"
fi
echo ""

echo "=== Results ==="
if [ "$ERRORS" -eq 0 ]; then
    echo "ALL CHECKS PASSED"
    exit 0
else
    echo "$ERRORS CHECK(S) FAILED"
    exit 1
fi
