#!/usr/bin/env bash

set -e
set -x

mypy responsive-images-generator --disallow-untyped-defs
black responsive-images-generator tests --check
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 88 --recursive --check-only --thirdparty responsive-images-generator responsive-images-generator tests
