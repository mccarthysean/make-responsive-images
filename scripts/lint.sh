#!/bin/bash

set -e
set -x

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"

# Remove unused imports and unused variables
autoflake --in-place --remove-unused-variables --remove-all-unused-imports --verbose --recursive ../responsive_images_generator/

# Nice sorting of imports
isort ../responsive_images_generator

# Opinionated but lovely auto-formatting
black ../responsive_images_generator