#!/bin/bash

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

cd ..
typer make_responsive_images.main utils docs --output ./README-typer.md --name make-responsive-images