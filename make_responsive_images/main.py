import logging
from pathlib import Path
from typing import Optional

import typer

from . import __app_name__, __version__
from .utils import make_html, resize_image

app = typer.Typer()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> bool:
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
        None, help='Classnames to add to the <img> tag (e.g. class="img-fluid")'
    ),
    img_sizes: str = typer.Option(
        "100vw", help='Sizes for the <img> tag (e.g. sizes="100vw")'
    ),
    lazy: bool = typer.Option(False, help='Adds loading="lazy" to <img> tag for SEO'),
    alt: str = typer.Option(
        "", help='Adds alt="" to the <img> tag (e.g. alt="Funny image")'
    ),
    dir: str = typer.Option(
        None, help='Images directory to prepend to the src (e.g. src="dir/image")'
    ),
    fmt: str = typer.Option(
        "webp", help='Image type to save as ("jpg" and "webp" supported)'
    ),
    qual: int = typer.Option(100, help="Compression to apply (i.e. 0=max, 100=min)"),
    lower: bool = typer.Option(True, help="Converts filename to lowercase"),
    dashes: bool = typer.Option(True, help="Converts underscores to dashes for SEO"),
) -> None:
    """Resize one image"""

    typer.secho(f"Image: {image}", fg=typer.colors.GREEN)
    typer.echo(f"Widths needed: {widths}")
    typer.echo(f"HTML wanted: {html}")

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
        make_html(
            orig_img_file=file,
            filenames=filenames,
            classes=classes,
            img_sizes=img_sizes,
            lazy=lazy,
            alt=alt,
            dir=dir,
            fmt=fmt,
        )
