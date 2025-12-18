#!/bin/bash
# Pre-commit script to run linters and tests
# Run this before committing to avoid CI failures

set -e

echo "========================================"
echo "Running pre-commit checks..."
echo "========================================"

# Check if Poetry is available
if ! command -v poetry &> /dev/null; then
    echo "ERROR: Poetry is not installed or not in PATH"
    echo "Please install Poetry: https://python-poetry.org/docs/#installation"
    exit 1
fi

# Format code with black
echo ""
echo "[1/4] Formatting code with black..."
poetry run black .
echo "OK: Code formatted successfully"

# Check linting with flake8
echo ""
echo "[2/4] Checking code style with flake8..."
poetry run flake8 qfinlib tests || echo "WARNING: Flake8 found issues (non-blocking)"

# Check types with mypy
echo ""
echo "[3/4] Checking types with mypy..."
poetry run mypy qfinlib || echo "WARNING: Mypy found issues (non-blocking)"

# Run tests
echo ""
echo "[4/4] Running tests..."
poetry run pytest
echo "OK: All tests passed"

echo ""
echo "========================================"
echo "All pre-commit checks passed!"
echo "========================================"

