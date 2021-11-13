#!/usr/bin/env bash

set -e
set -x

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

pytest ../tests/ --cov=responsive_images_generator --cov=tests --cov-report=term-missing ${@}

bash ./lint.sh
