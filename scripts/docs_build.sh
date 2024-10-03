#!/usr/bin/env bash

# Fail on any error.
set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

echo ""
echo "Running mkdocs build..."
python -m mkdocs build --config-file ../mkdocs.yml

# Overwrite the root-level README.md file
echo ""
echo "Copying docs/index.md to README.md (i.e. overwriting README.md)..."
cp ../docs/index.md ../README.md

echo ""
echo "Done."
