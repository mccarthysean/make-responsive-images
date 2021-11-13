#!/bin/bash

set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

# https://python-poetry.org/docs/libraries/
# https://python-poetry.org/docs/cli/#publish
poetry config pypi-token.pypi $PYPI_TOKEN_PROD
poetry publish --build --username $PYPI_USERNAME_PROD --password $PYPI_PASSWORD_PROD