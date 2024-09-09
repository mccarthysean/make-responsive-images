#!/bin/bash

echo "Setting up environment variables before uploading..."

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
cd ..
echo "Current working directory: $(pwd)"

# Set variable names from .env file
export $(cat ../.env | grep -v "^#" | xargs)

# To ensure we use BuildKit for faster, more efficient builds
export DOCKER_BUILDKIT=1
export BUILDKIT_INLINE_CACHE=1
export COMPOSE_DOCKER_CLI_BUILD=1

echo "PYPI_TOKEN_PROD: $PYPI_TOKEN_PROD"