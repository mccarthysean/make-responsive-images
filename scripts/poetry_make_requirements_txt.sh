#!/bin/bash

set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

echo -e "\nRunning poetry to generate requirements.txt..."

poetry config virtualenvs.create false
poetry config warnings.export false
poetry export --no-interaction --no-ansi --without-hashes --with dev --format requirements.txt --output /workspace/requirements.txt

echo -e "\nDone."
