#!/usr/bin/env bash

set -e
set -x

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
cd ..
echo "Current working directory: $(pwd)"

pytest ./tests/ --cov=./make_responsive_images --cov=./tests --cov-report=xml ${@}