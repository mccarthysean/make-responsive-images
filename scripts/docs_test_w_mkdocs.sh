#!/usr/bin/env bash

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

# Preview the docs
echo ""
echo "Running mkdocs serve..."
mkdocs serve --config-file ../mkdocs.yml --dev-addr 0.0.0.0:8008
