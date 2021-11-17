# `make-responsive-images`

Generate responsive images automatically, for websites to use `srcset` and `sizes` in the `<img>` tags.

This way you serve an optimal image for each device viewport size.

<p align="center">
<a href="https://github.com/mccarthysean/make-responsive-images/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/mccarthysean/make-responsive-images/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://codecov.io/gh/mccarthysean/make-responsive-images" target="_blank">
    <img src="https://img.shields.io/codecov/c/github/mccarthysean/make-responsive-images?color=%2334D058" alt="Coverage">
</a>
<a href="https://github.com/mccarthysean/make-responsive-images/actions?query=workflow%3Apypi" target="_blank">
    <img src="https://github.com/mccarthysean/make-responsive-images/workflows/Upload%20Package%20to%20PyPI/badge.svg" alt="Publish">
</a>
<a href="https://pypi.org/project/make-responsive-images" target="_blank">
    <img src="https://img.shields.io/pypi/v/make-responsive-images?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/make-responsive-images/" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/make-responsive-images.svg" alt="Python Versions">
</a>
</p>

## Installation

[Install from PyPI](https://pypi.org/project/make-responsive-images/)

```bash
pip install make-responsive-images
```

## Usage

```bash
resize [OPTIONS] COMMAND [ARGS]...
```

### Options

* `-v, --version`: Show the application's version and exit.
* `--help`: Show this message and exit.

## Commands

* `image`: Resize one image

### Usage

```bash
resize image [OPTIONS] [IMAGE]
```

### Arguments

* `[IMAGE]`: [default: /workspace/tests/fixtures/xfer-original.jpg]

### Options

* `--widths TEXT`: Widths of new images, in pixels  [default: 600,1000,1400]
* `--html / --no-html`: Generate HTML <img> tag  [default: True]
* `--classes TEXT`: Classnames to add to the <img> tag (e.g. class="img-fluid")
* `--img-sizes TEXT`: Sizes for the <img> tag (e.g. sizes="100vw")  [default: 100vw]
* `--lazy / --no-lazy`: Adds loading="lazy" to <img> tag for SEO  [default: False]
* `--alt TEXT`: Adds alt="" to the <img> tag (e.g. alt="Funny image")  [default: ]
* `--dir TEXT`: Images directory to prepend to the src (e.g. src="dir/image")
* `--fmt TEXT`: Image type to save as ("jpg" and "webp" supported)  [default: webp]
* `--qual INTEGER`: Compression to apply (i.e. 0=max, 100=min)  [default: 100]
* `--lower / --no-lower`: Converts filename to lowercase  [default: True]
* `--dashes / --no-dashes`: Converts underscores to dashes for SEO  [default: True]
* `--flask / --no-flask`: Uses Python Flask's 'url_for('static', ...)'  [default: False]
* `--help`: Show this message and exit.

## Author Info

Sean McCarthy is Chief Data Scientist at [IJACK Technologies Inc](https://myijack.com), a leading manufacturer of fully-automated pumps to green the oil and gas industry.

<br>
<a href="https://mccarthysean.dev">
    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/mccarthysean.svg?sanitize=1" alt="Sean McCarthy's blog">
</a>
<a href="https://www.linkedin.com/in/seanmccarthy2/">
    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/linkedin.svg?sanitize=1" alt="LinkedIn">
</a>
<a href="https://github.com/mccarthysean">
    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/github.svg?sanitize=1" alt="GitHub">
</a>
<a href="https://twitter.com/mccarthysean">
    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/twitter.svg?sanitize=1" alt="Twitter">
</a>
<a href="https://www.facebook.com/sean.mccarth">
    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/facebook.svg?sanitize=1" alt="Facebook">
</a>
<a href="https://medium.com/@mccarthysean">
    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/medium.svg?sanitize=1" alt="Medium">
</a>
<a href="https://www.instagram.com/mccarthysean/">
    <img src="https://raw.githubusercontent.com/mccarthysean/make-responsive-images/main/docs/assets/instagram.svg?sanitize=1" alt="Instagram">
</a>
