#!/usr/bin/env bash

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

cd ..
python -m mkdocs build

cp ../docs/index.md ../README.md
