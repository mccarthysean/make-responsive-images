#!/bin/bash

set -e
set -x

# Remove unused imports and unused variables
autoflake --in-place --remove-unused-variables --remove-all-unused-imports --verbose --recursive /workspace/responsive_images_generator/

# Nice sorting of imports
isort /workspace/responsive_images_generator/

# Opinionated but lovely auto-formatting
black /workspace/responsive_images_generator