
#!/usr/bin/env bash

set -e

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

mkdocs serve --dev-addr 0.0.0.0:8008
