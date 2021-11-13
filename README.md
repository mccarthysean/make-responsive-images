# responsive-images-generator

<p align="center">
    <em>A summary phrase to catch attention!</em>
</p>

<p align="center">
<a href="https://github.com/mccarthysean/responsive-images-generator/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/mccarthysean/responsive-images-generator/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://github.com/mccarthysean/responsive-images-generator/actions?query=workflow%3APublish" target="_blank">
    <img src="https://github.com/mccarthysean/responsive-images-generator/workflows/Publish/badge.svg" alt="Publish">
</a>
<a href="https://codecov.io/gh/mccarthysean/responsive-images-generator" target="_blank">
    <img src="https://img.shields.io/codecov/c/github/mccarthysean/responsive-images-generator?color=%2334D058" alt="Coverage">
</a>
<a href="https://pypi.org/project/responsive-images-generator" target="_blank">
    <img src="https://img.shields.io/pypi/v/responsive-images-generator?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/responsive-images-generator/" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/responsive-images-generator.svg" alt="Python Versions">
</a>

## Installing responsive-images-generator

Install the latest release:

```bash
pip install responsive-images-generator
```

Or you can clone `responsive-images-generator` and start locally

```bash

# ensure you have Poetry installed
pip install --user poetry

# install all dependencies (including dev)
poetry install

# develop!

```

## Example Usage

```python
import responsive-images-generator

# do stuff
```

Only **Python 3.6+** is supported as required by the black, pydantic packages

## Publishing to Pypi

### Poetry's documentation

Note that it is recommended to use [API tokens](https://pypi.org/help/#apitoken) when uploading packages to PyPI.

>Once you have created a new token, you can tell Poetry to use it:

<https://python-poetry.org/docs/repositories/#configuring-credentials>

We do this using GitHub Actions' Workflows and Repository Secrets!

### Repo Secrets

Go to your repo settings and add a `PYPI_TOKEN` environment variable:

![Github Actions setup of Poetry token environment variable](images/Github-Secrets-PYPI_TOKEN-Setup.png)

### Inspect the GitHub Actions Publish Workflows

```yml
name: Publish

on:
  release:
    types:
      - created

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      ...
      ...
      ...
      - name: Publish
        env:
          PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}
        run: |
          poetry config pypi-token.pypi $PYPI_TOKEN
          bash scripts/publish.sh
```

> That's it!

When you make a release on GitHub, the publish workflow will run and deploy to PyPi! 🚀🎉😎

## Contributing Guide

Welcome! 😊👋

> Please see the [Contributing Guide](CONTRIBUTING.md).
