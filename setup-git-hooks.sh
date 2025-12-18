#!/bin/bash
# Setup script to install git pre-commit hooks

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_HOOKS_DIR="$SCRIPT_DIR/.git/hooks"
HOOKS_SOURCE_DIR="$SCRIPT_DIR/.githooks"

echo "Setting up git pre-commit hooks..."

# Check if .git directory exists
if [ ! -d "$SCRIPT_DIR/.git" ]; then
    echo "Error: .git directory not found. Are you in a git repository?"
    exit 1
fi

# Create .git/hooks directory if it doesn't exist
mkdir -p "$GIT_HOOKS_DIR"

# Copy pre-commit hook
if [ -f "$HOOKS_SOURCE_DIR/pre-commit" ]; then
    cp "$HOOKS_SOURCE_DIR/pre-commit" "$GIT_HOOKS_DIR/pre-commit"
    chmod +x "$GIT_HOOKS_DIR/pre-commit"
    echo "✓ Pre-commit hook installed successfully"
else
    echo "Error: pre-commit hook not found in .githooks/"
    exit 1
fi

echo ""
echo "Git hooks are now set up!"
echo "Pre-commit checks will run automatically before each commit."
echo ""
echo "To skip the hook, use: git commit --no-verify"

