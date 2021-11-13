#!/bin/bash

set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

# https://python-poetry.org/docs/libraries/
# https://python-poetry.org/docs/cli/#publish
# poetry config repositories.testpypi https://test.pypi.org/legacy/
# poetry config pypi-token.pypi $PYPI_TOKEN_TEST
poetry publish --build --repository testpypi
# poetry publish --build --repository testpypi --username $PYPI_USERNAME_TEST --password $PYPI_PASSWORD_TEST

# Test that it worked
# pip install --index-url https://test.pypi.org/simple/ responsive-images-generator