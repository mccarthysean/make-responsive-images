#!/bin/bash

set -e
set -x

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

# Remove unused imports and unused variables
autoflake --in-place --remove-unused-variables --remove-all-unused-imports --verbose --recursive ../make_responsive_images/ ../tests

# Nice sorting of imports
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 88 --recursive --thirdparty ../make_responsive_images ../tests

# Opinionated but lovely auto-formatting
black ../make_responsive_images ../tests

# Run mypy
mypy --config-file ../mypy.ini ../make_responsive_images --disallow-untyped-defs
