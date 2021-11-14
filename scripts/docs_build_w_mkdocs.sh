#!/usr/bin/env bash

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
cd ..
echo "Current working directory: $(pwd)"

python -m mkdocs build

# Overwrite the root-level README.md file
cp ./docs/index.md ./README.md

# Preview the docs
mkdocs serve --dev-addr 0.0.0.0:8008