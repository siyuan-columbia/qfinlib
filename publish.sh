#!/bin/bash
# Script to build and publish qfinlib to PyPI

set -e

echo "Building qfinlib package..."

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
fi

# Build the package
echo "Building package..."
poetry build

# Check if we should publish to TestPyPI first
if [ "$1" == "--test" ]; then
    echo "Publishing to TestPyPI..."
    poetry publish --repository testpypi
else
    echo "Publishing to PyPI..."
    echo "Make sure you have configured your PyPI credentials:"
    echo "  poetry config pypi-token.pypi YOUR_API_TOKEN"
    echo ""
    read -p "Continue with publishing to PyPI? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        poetry publish
    else
        echo "Publishing cancelled."
    fi
fi

