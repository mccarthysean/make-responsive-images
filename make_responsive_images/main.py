import logging
from pathlib import Path
from typing import Optional

import typer

from . import __app_name__, __version__
from .utils import resize_image

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
        )
    ),
    widths: str = typer.Option("600,1000,1400"),
) -> None:
    """Resize one image"""

    typer.secho(f"Image: {image}", fg=typer.colors.GREEN)
    typer.secho(f"Widths needed: {widths}", fg=typer.colors.GREEN)

    widths_split = widths.split(",")
    widths_list = [int(width) for width in widths_split]

    file = Path(image)
    images = resize_image(file, widths=widths_list)

    typer.secho(f"Images: {images}", fg=typer.colors.GREEN)
