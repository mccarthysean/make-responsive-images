#!/usr/bin/env bash

cd ..
python -m mkdocs build

cp ./docs/index.md ./README.md
