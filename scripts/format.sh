#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place responsive-images-generator tests --exclude=__init__.py
black responsive-images-generator tests
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 88 --recursive --thirdparty responsive-images-generator --apply responsive-images-generator tests
