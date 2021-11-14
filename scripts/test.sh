#!/usr/bin/env bash

set -e
set -x

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

cd ..
pytest ./tests/ --cov=./make_responsive_images --cov=./tests --cov-report=term-missing ${@}

bash ./scripts/lint.sh
