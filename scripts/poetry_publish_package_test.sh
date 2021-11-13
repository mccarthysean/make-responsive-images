#!/bin/bash

set -e

# https://python-poetry.org/docs/libraries/
# https://python-poetry.org/docs/cli/#publish
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.pypi $PYPI_TOKEN_TEST
poetry publish --build --repository testpypi --username $PYPI_USERNAME_TEST --password $PYPI_PASSWORD_TEST

# Test that it worked
# pip install --index-url https://test.pypi.org/simple/ responsive-images-generator