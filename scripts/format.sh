#!/bin/sh -e
set -x

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place make-responsive-images tests --exclude=__init__.py
black make-responsive-images tests
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 88 --recursive --thirdparty make-responsive-images --apply make-responsive-images tests
