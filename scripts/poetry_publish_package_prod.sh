#!/bin/bash

set -e

# https://python-poetry.org/docs/libraries/
# https://python-poetry.org/docs/cli/#publish
poetry config pypi-token.pypi $PYPI_TOKEN_PROD
poetry publish --build --username $PYPI_USERNAME_PROD --password $PYPI_PASSWORD_PROD