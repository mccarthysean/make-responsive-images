#!/bin/bash

# Set the current working directory to the directory in which the script is located, for CI/CD
cd "$(dirname "$0")"
echo "Current working directory: $(pwd)"

cd ..
typer responsive_images_generator.main utils docs --output /workspace/README.md --name responsive-images-generator