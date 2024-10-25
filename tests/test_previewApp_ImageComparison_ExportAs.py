import allure
import pytest
import os

from globals.functions.previewApp import PreviewAppFunct
from globals.functions.generics import GenericFunct
from fixtures.constants import IMAGE_1, IMAGE_2, APPNAME, FIXTURES, SOURCE_IMAGES, REF_FILE_NAME, SCREENSHOTS, \
    DIFF_FILE_NAME, EXP_FILE_NAME

@allure.suite("Image Comparison Test with Preview App by EXPORT Method")
class TestImageComparisonExportAs:

    @pytest.fixture
    def baseDir(self):
        """Fixture to return the base directory for image paths."""
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    @allure.step("Open Preview Application and Validate App Opened")
    def test_open_preview_application(self):
        """Test to open the Preview application."""

        actualstate = PreviewAppFunct.openApplication(APPNAME)

        # ASSERT APP IS OPENED
        PreviewAppFunct.assertAppOpenState(actualstate)

    @allure.step("Navigate Directory and Select Image Open")
    def test_select_image(self, baseDir):
        """Navigate to Directory and Open the Image"""

        image1_path = os.path.join(baseDir, FIXTURES, SOURCE_IMAGES, IMAGE_1)
        image2_path = os.path.join(baseDir, FIXTURES, SOURCE_IMAGES, IMAGE_2)

        # ASSERT IMAGES ARE EXIST
        PreviewAppFunct.assertcheckFileExists(image1_path)
        PreviewAppFunct.assertcheckFileExists(image2_path)

        PreviewAppFunct.selectImage(image1_path)

    @allure.step("Export the Image as JPEG Format")
    def test_export_JPEG_imageFile(self, baseDir):
        """Export The Image as JPEG Format"""

        image1_path = os.path.join(baseDir, FIXTURES, SOURCE_IMAGES, EXP_FILE_NAME)

        PreviewAppFunct.exportImageAsJPEG()

        # ASSERT SAVE AS IMAGE IS EXIST
        PreviewAppFunct.assertcheckFileExists(image1_path)

    @allure.step("Verify and Compare the Exported IMAGE_1.jpg Vs IMAGE_2.png")
    def test_compare_images(self, baseDir):
        """Test comparing IMAGE_1.jpg and IMAGE_2.png"""

        image1_path = os.path.join(baseDir, FIXTURES, SOURCE_IMAGES, EXP_FILE_NAME)
        image2_path = os.path.join(baseDir, FIXTURES, SOURCE_IMAGES, IMAGE_2)
        diff_image_path = os.path.join(baseDir, FIXTURES, SCREENSHOTS, DIFF_FILE_NAME)

        # Compare the images
        if not GenericFunct.compare_images_average_hash(image1_path, image2_path, diff_image_path):
            assert False, "The images are not identical!"

        # ASSERT DIFF IMAGE IS EXIST
        PreviewAppFunct.assertcheckFileExists(diff_image_path)

@pytest.fixture(scope="session", autouse=True)
def test_tearDown():
    yield
    PreviewAppFunct.closeApplication()
    GenericFunct.cleanup()