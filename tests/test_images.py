from pathlib import Path

from responsive_images_generator import __app_name__, __version__, main
from typer.testing import CliRunner

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
    assert len([f for f in images_path.glob("*")]) == 1

    result = runner.invoke(main.app, ["image", str(test_image)])
    assert result.exit_code == 0
    # Should be four files in the folder now
    assert len([f for f in images_path.glob("*")]) == 4
