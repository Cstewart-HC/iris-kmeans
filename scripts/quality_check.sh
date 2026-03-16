#!/usr/bin/env bash
set -euo pipefail

echo "Running project quality checks"

echo "1) flake8"
flake8 . || true

echo "2) isort (check)"
isort --check-only --diff . || true

echo "3) black (check)"
black --check . || true

echo "4) complexity (radon) — requires radon to be installed"
if command -v radon >/dev/null 2>&1; then
  radon cc -s -a src || true
else
  echo "radon not installed — skipping complexity check"
fi

echo "Quality checks complete. Address warnings as needed."
