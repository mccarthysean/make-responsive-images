import sys
import unittest
from pathlib import Path

import pytest
from typer.testing import CliRunner

workspace_dir = Path(__file__).resolve().parents[1]

sys.path.append(str(workspace_dir))

from make_responsive_images import __version__, main

runner = CliRunner()

IMAGES_FOLDER = Path("/myijack/assets/img/")
IMAGE_TO_RESIZE = IMAGES_FOLDER.joinpath("rcom/rcom-charts-normal.PNG")


class TestMain(unittest.TestCase):
    """Test the main function"""

    def test_version(self):
        """Test the version of the app"""
        result = runner.invoke(main.app, ["--version"])
        self.assertTrue(result.exit_code == 0)
        self.assertTrue(__version__ in result.stdout)

    def test_image_resize(self):
        """Test we resize the image into three new images"""

        fmt = "webp"
        result = runner.invoke(
            main.app,
            [
                "image",
                f"{str(IMAGE_TO_RESIZE)}",
                "--html",
                "--classes=img-fluid",
                "--dir=img",
                f"--fmt={fmt}",
                "--qual=100",
                "--lower",
                "--dashes",
                "--flask",
            ],
        )
        self.assertTrue(result.exit_code == 0)


if __name__ == "__main__":
    # unittest.main()
    # Run Pytest
    pytest.main(["-v", __file__])
