#!/usr/bin/env bash

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
cd ..
echo "Current working directory: $(pwd)"

# echo ""
# echo "Running mkdocs build..."
# python -m mkdocs build --config-file ./mkdocs.yml

# Overwrite the root-level README.md file
echo ""
echo "Copying docs/index.md to README.md (i.e. overwriting README.md)..."
cp ./docs/index.md ./README.md

# Preview the docs
echo ""
echo "Running mkdocs serve..."
mkdocs serve --config-file ./mkdocs.yml --dev-addr 0.0.0.0:8008