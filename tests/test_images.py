from pathlib import Path

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
            "--dir=static/img",
            f"--fmt={fmt}",
            "--qual=60",
            "--lower",
            "--dashes",
        ],
    )
    assert result.exit_code == 0
    # Should be four images in the folder now, plus the html file
    files_new = [f for f in images_path.glob("*")]
    assert len(files_new) == 5

    img_tag_file = images_path.joinpath("img_tag.html")
    assert img_tag_file in files_new
    with open(img_tag_file, "r") as f:
        contents = f.read()

    contents_should_be = f"""<img class="img-fluid" 
  sizes="100vw" 
  alt="" 
  src="static/img/xfer-original.{fmt}" 
  srcset="
    static/img/xfer-original-600px.{fmt} 600w,
    static/img/xfer-original-1000px.{fmt} 1000w,
    static/img/xfer-original-1400px.{fmt} 1400w"
  width="1400" height="805">"""
    assert contents == contents_should_be
