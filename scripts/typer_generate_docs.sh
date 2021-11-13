#!/bin/bash

set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

cd ..
echo ""
echo "Ensure you run 'poetry install' before generating the docs..."
resize --version
echo ""
echo "Ensure you have typer-cli installed before generating the docs..."
typer --version
echo ""
typer make_responsive_images.main utils docs --output ./docs/index-typer-auto-generated.md --name make-responsive-images