#!/bin/bash

set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
cd ..
echo "Current working directory: $(pwd)"

echo -e "\nRunning poetry to update the lock file..."

poetry lock --no-update

echo -e "\nDone."
