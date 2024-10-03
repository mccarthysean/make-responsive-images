#!/bin/bash
# This script is not currently used

set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
cd ..
echo "Current working directory: $(pwd)"

echo ""
# echo "Ensure you run 'poetry install' before generating the docs..."
echo "Checking 'resize'..."
poetry run resize --version
echo ""
echo "Ensure you have typer-cli installed before generating the docs..."
typer --version
echo ""
typer make_responsive_images.main utils docs --output ./docs/index-typer-auto-generated.md --name make-responsive-images

echo -e "\n New file created: docs/index-typer-auto-generated.md"

echo -e "\nDone."
