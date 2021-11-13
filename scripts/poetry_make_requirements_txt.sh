#!/bin/bash

set -e

poetry export --no-interaction --no-ansi --without-hashes --dev --format requirements.txt --output /workspace/requirements.txt
