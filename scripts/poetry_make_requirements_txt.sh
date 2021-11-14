#!/bin/bash

set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

poetry export --no-interaction --no-ansi --without-hashes --dev --format requirements.txt --output /workspace/requirements.txt
