import logging
from pathlib import Path
from typing import Optional

import typer
from PIL import Image

from . import __app_name__, __version__

app = typer.Typer(
    name="resize",
    # invoke_without_command means that if no subcommand is provided, the main function is called
    invoke_without_command=True,
    # no_args_is_help=True means that if no arguments are provided, the help message is shown
    no_args_is_help=False,
    # add_completion=True means that the command will support shell completion
    add_completion=True,
    # help is the help message for the main command
    help="Resize images",
    pretty_exceptions_enable=True,
    pretty_exceptions_short=True,
    pretty_exceptions_show_locals=True,
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def resize_image(
    file: Path,
    widths: list,
    fmt: str,
    qual: int,
    lower: bool,
    dashes: bool,
) -> list:
    """Resize the image to the widths specified"""

    # Convert to RGB so we can save as .webp
    image = Image.open(file).convert("RGB")

    # filter out duplicates and larger than original
    sizes_set = set()
    for width in widths:
        width = min(width, image.width)
        # orig_aspect = image.width / float(image.height)
        ratio = width / float(image.width)
        width = int(image.width * ratio + 0.5)
        height = int(image.height * ratio + 0.5)
        sizes_set.add((width, height))
    sizes = sorted(sizes_set)

    largest_size = sizes[-1]
    second_largest_size = sizes[-2]

    # If the largest image size is not at least 20% larger than the second largest size,
    # then remove the second-largest size
    if largest_size[0] < second_largest_size[0] * 1.2:
        # remove the second-largest size
        sizes.pop(-2)

    # if sizes[0] == image.size:
    #     # smallest size is original image
    #     return [image]

    # create the resized images
    resized = []
    filenames = []
    for width, height in sizes:
        if (width, height) == (image.width, image.height):
            new_image = image
        else:
            # new_image = image.resize((width, height), Image.ANTIALIAS)
            new_image = image.resize((width, height), Image.Resampling.NEAREST)

        resized.append(new_image)

        # Save the image
        fmt = fmt.lower()
        if fmt not in ("jpg", "webp"):
            raise TypeError('fmt must be either "jpg" or "webp"')

        filename_new = f"{file.stem}-{width}px.{fmt}"

        if lower:
            filename_new = filename_new.lower()

        if dashes:
            filename_new = filename_new.replace("_", "-")

        path_new = file.parent.joinpath(filename_new)
        fmt2 = "jpeg" if fmt == "jpg" else fmt
        # Set quality to max 100, min 0
        quality = max(0, min(100, qual))
        # The optimize flag will do an extra pass on the image to find a way
        # to reduce its size as much as possible
        new_image.save(path_new, fmt2, quality=quality, optimize=True)

        # filename_new = f"{file.stem}-{width}px.jpg"
        # path_new = file.parent.joinpath(filename_new)
        # new_image.save(path_new, "JPEG", quality=50, optimize=True)

        filenames.append((filename_new, width, height))

        # if crop:
        #     new_image = ImageOps.fit(
        #         orig_image,
        #         (width, height),
        #         method=Image.BICUBIC,
        #         centering=(crop[0] / 100.0, crop[1] / 100.0),
        #     )
        # else:
        #     new_image = orig_image.app(
        #         (width, height),
        #         resample=Image.BICUBIC
        #     )

    return filenames


def make_html(
    orig_img_file: Path,
    filenames: list,
    classes: str,
    img_sizes: str,
    lazy: bool,
    alt: str,
    dir: str,
    flask: bool,
) -> str:
    """Resize the image to the widths specified"""

    html_str = "<img "

    if classes:
        html_str += f'class="{classes}" '
    if lazy:
        html_str += 'loading="lazy" '

    html_str += f'\n  sizes="{img_sizes}" '
    html_str += f'\n  alt="{alt}" '

    def _get_filename(dir: str, filename: str, flask: bool) -> str:
        """Get the filename with the directory prepended"""
        if dir:
            filepath: str = str(Path(dir).joinpath(filename))
            if flask:
                return r"{{ " + f"url_for('static', filename='{filepath}')" + r" }}"
            return filepath
        return str(filename)

    srcset_str = '\n  srcset="'
    n_filenames = len(filenames)
    filename: str = "no_filename_found"
    for num, (filename, width, height) in enumerate(filenames):
        is_last = num == (n_filenames - 1)
        filename2 = _get_filename(dir=dir, filename=filename, flask=flask)
        if not is_last:
            srcset_str += "\n    " + filename2 + f" {width}w,"
        else:
            srcset_str += "\n    " + filename2 + f' {width}w"'
            srcset_str += '\n  src="' + filename2 + '" '
            srcset_str += f'\n  width="{width}" height="{height}"'

    html_str += srcset_str
    html_str += ">"

    html_path = orig_img_file.parent.joinpath(f"img-tag-{filename}.html")
    with open(html_path, "w") as f:
        f.write(html_str)

    return html_str


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def version(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> bool:
    """Show the application's version and exit."""
    if version:
        return True
    return False


@app.command()
def image(
    image: str = typer.Argument(
        str(
            Path(__file__)
            .parent.parent.joinpath("tests")
            .joinpath("fixtures")
            .joinpath("xfer-original.jpg")
        ),
        help="Image file location",
    ),
    widths: str = typer.Option("600,1000,1400", help="Widths of new images, in pixels"),
    html: bool = typer.Option(True, help="Generate HTML <img> tag"),
    classes: str = typer.Option(
        "img-fluid", help='Classnames to add to the <img> tag (e.g. class="img-fluid")'
    ),
    img_sizes: str = typer.Option(
        "100vw", help='Sizes for the <img> tag (e.g. sizes="100vw")'
    ),
    lazy: bool = typer.Option(False, help='Adds loading="lazy" to <img> tag for SEO'),
    alt: str = typer.Option(
        "", help='Adds alt="" to the <img> tag (e.g. alt="Funny image")'
    ),
    dir: str = typer.Option(
        "img", help='Images directory to prepend to the src (e.g. src="dir/images")'
    ),
    fmt: str = typer.Option(
        "webp", help='Image type to save as ("jpg" and "webp" supported)'
    ),
    qual: int = typer.Option(100, help="Compression to apply (i.e. 0=max, 100=min)"),
    lower: bool = typer.Option(True, help="Converts filename to lowercase"),
    dashes: bool = typer.Option(True, help="Converts underscores to dashes for SEO"),
    flask: bool = typer.Option(
        False, help="Uses Python Flask's 'url_for('static', ...)'"
    ),
    delete: bool = typer.Option(True, help="Delete the original image after resizing"),
) -> bool:
    """This function is the entry point of the CLI."""

    typer.secho(f"Image: {image}", fg=typer.colors.GREEN)
    typer.echo(f"Widths needed: {widths}")
    typer.echo(f"HTML wanted: {html}")
    typer.echo(f"Classes wanted: {classes}")
    typer.echo(f"Image sizes wanted: {img_sizes}")
    typer.echo(f"Lazy loading wanted: {lazy}")
    typer.echo(f"Alt text wanted: {alt}")
    typer.echo(f"Directory to append: {dir}")
    typer.echo(f"Image format wanted: {fmt}")
    typer.echo(f"Quality/compression wanted: {qual}")
    typer.echo(f"Lowercase filename wanted: {lower}")
    typer.echo(f"Dashes wanted: {dashes}")
    typer.echo(f"Flask url_for() wanted: {flask}")
    typer.echo(f"Delete original image: {delete}")

    widths_split = widths.split(",")
    widths_list = [int(width) for width in widths_split]

    file = Path(image)
    filenames = resize_image(
        file=file,
        widths=widths_list,
        fmt=fmt,
        qual=qual,
        lower=lower,
        dashes=dashes,
    )
    typer.echo(f"filenames: {filenames}")

    if html:
        html_str: str = make_html(
            orig_img_file=file,
            filenames=filenames,
            classes=classes,
            img_sizes=img_sizes,
            lazy=lazy,
            alt=alt,
            dir=dir,
            flask=flask,
        )
        typer.echo(f"HTML <img> tag: \n\n{html_str}")

    if delete:
        file.unlink()
        typer.echo(f"Deleted original image: {file}")

    typer.echo("\n\nDone!\n")

    return True


if __name__ == "__main__":
    app()
