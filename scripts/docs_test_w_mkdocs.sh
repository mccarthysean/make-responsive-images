#!/usr/bin/env bash

# Preview the docs
echo ""
echo "Running mkdocs serve..."
mkdocs serve --config-file ./mkdocs.yml --dev-addr 0.0.0.0:8008
