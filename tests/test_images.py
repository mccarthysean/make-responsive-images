from pathlib import Path

import pytest
from typer.testing import CliRunner

from make_responsive_images import __app_name__, __version__, main

runner = CliRunner()


def test_version():
    """Test we can see the version number"""
    result = runner.invoke(main.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


def test_image_resize():
    """Test we resize the image into three new images"""

    # First remove all but the original image
    images_path = Path(__file__).parent.joinpath("fixtures")
    test_image = images_path.joinpath("xfer-original.jpg")
    files = images_path.glob("*")
    for f in files:
        if not f.stem == "xfer-original":
            f.unlink()
    # There should only be one left now
    files_remaining = [f for f in images_path.glob("*")]
    assert len(files_remaining) == 1

    fmt = "webp"
    result = runner.invoke(
        main.app,
        [
            "image",
            f"{str(test_image)}",
            "--html",
            "--classes=img-fluid",
            "--dir=img",
            f"--fmt={fmt}",
            "--qual=60",
            "--lower",
            "--dashes",
            "--flask",
        ],
    )
    assert result.exit_code == 0
    # Should be four images in the folder now, plus the html file
    files_new = [f for f in images_path.glob("*")]
    # Four images and one html file for the img tag
    assert len(files_new) == 5

    tag_file: Path = None
    for file_ in files_new:
        if "img-tag-" in file_.stem:
            tag_file = file_
    assert tag_file is not None

    with open(tag_file, "r") as f:
        contents = f.read()

    contents_should_be = r"""<img class="img-fluid" 
  sizes="100vw" 
  alt="" 
  srcset="
    {{ url_for('static', filename='img/xfer-original-600px.webp') }} 600w,
    {{ url_for('static', filename='img/xfer-original-1000px.webp') }} 1000w,
    {{ url_for('static', filename='img/xfer-original-1400px.webp') }} 1400w"
  src="{{ url_for('static', filename='img/xfer-original-1400px.webp') }}" 
  width="1400" height="805">"""
    assert contents == contents_should_be


if __name__ == "__main__":
    # Run Pytest
    pytest.main(["-v", __file__])
