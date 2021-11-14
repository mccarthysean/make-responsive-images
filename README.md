# `make-responsive-images`

Generate responsive images automatically, for websites to use `srcset` in the `<img>` tags.

This way you serve an optimal image for each device viewport size.

<p align="center">
<a href="https://github.com/mccarthysean/make-responsive-images/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/mccarthysean/make-responsive-images/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://github.com/mccarthysean/make-responsive-images/actions?query=workflow%3APublish" target="_blank">
    <img src="https://github.com/mccarthysean/make-responsive-images/workflows/Publish/badge.svg" alt="Publish">
</a>
<a href="https://codecov.io/gh/mccarthysean/make-responsive-images" target="_blank">
    <img src="https://img.shields.io/codecov/c/github/mccarthysean/make-responsive-images?color=%2334D058" alt="Coverage">
</a>
<a href="https://pypi.org/project/make-responsive-images" target="_blank">
    <img src="https://img.shields.io/pypi/v/make-responsive-images?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/make-responsive-images/" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/make-responsive-images.svg" alt="Python Versions">
</a>
</p>

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

* `--widths TEXT`: [default: 600,1000,1400]
* `--widths TEXT`: Widths of new images, in pixels  [default: 600,1000,1400]
* `--html / --no-html`: Generate HTML <img> tag  [default: True]
* `--classes TEXT`: Classnames to add to the <img> tag (e.g. class="img-fluid")
* `--img-sizes TEXT`: Sizes for the <img> tag (e.g. sizes="100vw")  [default: 100vw]
* `--lazy / --no-lazy`: Adds loading="lazy" to <img> tag for SEO  [default: True]
* `--alt TEXT`: Adds alt="" to the <img> tag (e.g. alt="Funny image")  [default: ]
* `--dir TEXT`: Images directory to prepend to the src (e.g. src="<dir>/<image>")
* `--help`: Show this message and exit.
