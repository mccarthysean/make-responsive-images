#!/bin/bash

# set -e
source ./get_envs_before_uploading.sh

# Function to check if a variable is empty
check_var() {
    if [ -z "$1" ]; then
        echo "$2 of $1 is NULL! Exiting now..."
        exit 1
    else
        echo "$2 of $1 is not NULL. Good"
    fi
}

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

# Load environment variables from dotenv / .env file in Bash, and remove comments
export $(cat ../.env | sed 's/#.*//g' | xargs)

# Check if the variables are empty before proceeding
# echo "PYPI_TOKEN_PROD: $PYPI_TOKEN_PROD"
check_var "$PYPI_TOKEN_PROD" "PYPI_TOKEN_PROD"

# First build the files to be uploaded
poetry build

# Publish to the production repository
# https://python-poetry.org/docs/libraries/
# https://python-poetry.org/docs/cli/#publish
# poetry config pypi-token.pypi $PYPI_TOKEN_PROD
# poetry publish --build 
# poetry publish --build --username $PYPI_USERNAME_PROD --password $PYPI_PASSWORD_PROD
poetry publish --username __token__ --password $PYPI_TOKEN_PROD

