#!/bin/bash

set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
cd ..
echo "Current working directory: $(pwd)"

echo ""
echo "Ensure you have dos2unix installed (i.e. apt update && apt install dos2unix)..."
dos2unix --version
sudo find . -type f -print0 | xargs -0 dos2unix

# alternatively... run:
# sed -i -e 's/\r$//' scriptname.sh