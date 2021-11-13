#!/usr/bin/env bash

set -e
set -x

pytest ../tests/ --cov=responsive_images_generator --cov=tests --cov-report=term-missing ${@}
bash ./lint.sh
