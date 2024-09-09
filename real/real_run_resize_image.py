from pathlib import Path
from unittest.mock import patch
import unittest
from typer.testing import CliRunner

from make_responsive_images import __app_name__, __version__, main

runner = CliRunner()

IMAGES_FOLDER = Path("/myijack/assets/img/")
IMAGE_TO_RESIZE = IMAGES_FOLDER.joinpath("rcom/rcom-charts-normal.PNG")

class TestMain(unittest.TestCase):
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
                "--qual=60",
                "--lower",
                "--dashes",
                "--flask",
            ],
        )
        self.assertTrue(result.exit_code == 0)

if __name__ == "__main__":
    unittest.main()
