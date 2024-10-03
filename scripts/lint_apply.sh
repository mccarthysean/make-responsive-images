#!/bin/bash

# If there's an error, stop the script
set -e
# Print each command that's executed
set -x

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
# cd ..
echo "Current working directory: $(pwd)"

# Use Ruff to lint everything
echo ""
echo "Running ruff linter..."
# Run the linter
ruff check ../make_responsive_images --fix --config ../pyproject.toml
ruff check ../tests --fix --config ../pyproject.toml

# Run the formatter
echo ""
echo "Running ruff formatter..."
ruff format ../make_responsive_images --config ../pyproject.toml
ruff format ../tests --config ../pyproject.toml

# # Run the pyright linter (takes a bit longer)
# echo ""
# echo "Running pyright linter..."
# pyright ../make_responsive_images --project ../pyproject.toml
# pyright ../tests --project ../pyproject.toml
