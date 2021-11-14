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
isort --profile black ./make_responsive_images ./tests --check-only

# Remove unused imports and unused variables
echo ""
echo "Running autoflake..."
autoflake --in-place --remove-unused-variables --remove-all-unused-imports --verbose --recursive ./make_responsive_images/ ./tests

# Opinionated but lovely auto-formatting
echo ""
echo "Running black..."
black ./make_responsive_images ./tests --check

echo ""
echo "Running flake8..."
flake8 ./make_responsive_images ./tests

echo ""
echo "Running mypy..."
mypy --config-file ./mypy.ini ./make_responsive_images --disallow-untyped-defs

# Security checks with Bandit and Safety
echo ""
echo "Running bandit..."
bandit -r "./make_responsive_images"
bandit -r "./tests" --configfile "./.bandit_4_tests.yml"

echo ""
echo "Running safety..."
safety check