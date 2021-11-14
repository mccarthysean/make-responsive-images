#!/bin/bash

set -e
set -x

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
cd ..
echo "Current working directory: $(pwd)"

# Nice sorting of imports
echo ""
echo "Running isort..."
isort --profile black ./make_responsive_images ./tests

# Opinionated but lovely auto-formatting
echo ""
echo "Running black..."
black ./make_responsive_images ./tests

# Remove unused imports and unused variables
echo ""
echo "Running autoflake..."
autoflake --in-place --remove-unused-variables --remove-all-unused-imports --verbose --recursive ./make_responsive_images/ ./tests
