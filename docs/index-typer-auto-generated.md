# `make-responsive-images`

**Usage**:

```console
$ make-responsive-images [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-v, --version`: Show the application's version and exit.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `image`: Resize one image

## `make-responsive-images image`

Resize one image

**Usage**:

```console
$ make-responsive-images image [OPTIONS] [IMAGE]
```

**Arguments**:

* `[IMAGE]`: Image file location  [default: /workspace/tests/fixtures/xfer-original.jpg]

**Options**:

* `--widths TEXT`: Widths of new images, in pixels  [default: 600,1000,1400]
* `--html / --no-html`: Generate HTML <img> tag  [default: True]
* `--classes TEXT`: Classnames to add to the <img> tag (e.g. class="img-fluid")
* `--img-sizes TEXT`: Sizes for the <img> tag (e.g. sizes="100vw")  [default: 100vw]
* `--lazy / --no-lazy`: Adds loading="lazy" to <img> tag for SEO  [default: True]
* `--alt TEXT`: Adds alt="" to the <img> tag (e.g. alt="Funny image")  [default: ]
* `--dir TEXT`: Images directory to prepend to the src (e.g. src="<dir>/<image>")
* `--help`: Show this message and exit.
