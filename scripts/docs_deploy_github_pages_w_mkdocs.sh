#!/usr/bin/env bash

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
cd ..
echo "Current working directory: $(pwd)"

# Overwrite the root-level README.md file
echo ""
echo "Copying docs/index.md to README.md (i.e. overwriting README.md)..."
cp ./docs/index.md ./README.md

# Publish the docs to GitHub Pages
echo ""
echo "Running mkdocs gh-deploy to 'gh-pages' branch..."
mkdocs gh-deploy --config-file ./mkdocs.yml
