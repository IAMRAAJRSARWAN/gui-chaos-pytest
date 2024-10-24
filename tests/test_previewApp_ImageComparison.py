import allure
import pytest
import os

from globals.functions.previewApp import PreviewAppFunct
from globals.functions.generics import GenericFunct
from fixtures.constants import IMAGE_1, IMAGE_2

@allure.suite("Image Comparison Test with Preview App by SAVE AS Method")
class TestImageComparisonSaveAs:

    @pytest.fixture
    def baseDir(self):
        """Fixture to return the base directory for image paths."""
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    @allure.step("Open Preview Application and Validate App Opened")
    def test_open_preview_application(self):
        """Test to open the Preview application."""
        actualstate = PreviewAppFunct.openApplication('Preview')

        # ASSERT APP IS OPENED
        PreviewAppFunct.assertAppOpenState(actualstate)

    @allure.step("Navigate Directory and Select Image Open")
    def test_select_image(self, baseDir):
        """Navigate to Directory and Open the Image"""
        file_path_1 = os.path.join(baseDir, "fixtures", "images", IMAGE_1)
        file_path_2 = os.path.join(baseDir, "fixtures", "images", IMAGE_2)

        # ASSERT IMAGES ARE EXIST
        PreviewAppFunct.assertcheckFileExists(file_path_1)
        PreviewAppFunct.assertcheckFileExists(file_path_2)

        PreviewAppFunct.selectImage(baseDir, IMAGE_1)

    @allure.step("Save the opened image as Reference Image")
    def test_save_as_reference_imageFile(self, baseDir):
        """Save the opened image as a reference image."""
        ref_filename = "REF_Image.png"
        file_path = os.path.join(baseDir, "fixtures", "images", ref_filename)

        PreviewAppFunct.saveAsImage(ref_filename)

        # ASSERT SAVE AS IMAGE IS EXIST
        PreviewAppFunct.assertcheckFileExists(file_path)

    @allure.step("Verify and Compare the IMAGE_1 Vs Saved REF Image")
    def test_compare_images(self, baseDir):
        """Test comparing IMAGE_1 and REF_Image."""
        image1_path = os.path.join(baseDir, "fixtures", "images", "IMAGE_1.png")
        image2_path = os.path.join(baseDir, "fixtures", "images", "REF_Image.png")
        diff_image_path = os.path.join(baseDir, "fixtures", "images", "diff_image.png")

        # Compare the images
        if not GenericFunct.compare_images(image1_path, image2_path, diff_image_path):
            assert False, "The images are not identical!"

@allure.suite("Image Comparison Test with Preview App by EXPORT Method")
class TestImageComparisonExportAs:

    @pytest.fixture
    def baseDir(self):
        """Fixture to return the base directory for image paths."""
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    @allure.step("Open Preview Application and Validate App Opened")
    def test_open_preview_application(self):
        """Test to open the Preview application."""
        actualstate = PreviewAppFunct.openApplication('Preview')

        # ASSERT APP IS OPENED
        PreviewAppFunct.assertAppOpenState(actualstate)

    @allure.step("Navigate Directory and Select Image Open")
    def test_select_image(self, baseDir):
        """Navigate to Directory and Open the Image"""
        file_path_1 = os.path.join(baseDir, "fixtures", "images", IMAGE_1)
        file_path_2 = os.path.join(baseDir, "fixtures", "images", IMAGE_2)

        # ASSERT IMAGES ARE EXIST
        PreviewAppFunct.assertcheckFileExists(file_path_1)
        PreviewAppFunct.assertcheckFileExists(file_path_2)

        PreviewAppFunct.selectImage(baseDir, IMAGE_1)

    @allure.step("Export the Image as JPEG Format")
    def test_Export_JPEG_imageFile(self, baseDir):
        """Save the opened image as a reference image."""
        exp_filename = "IMAGE_1"
        file_path = os.path.join(baseDir, "fixtures", "images", exp_filename)

        PreviewAppFunct.exportImageAsJPEG(exp_filename)

        # ASSERT SAVE AS IMAGE IS EXIST
        PreviewAppFunct.assertcheckFileExists(file_path)

    @allure.step("Verify and Compare the Exported IMAGE_1.jpg Vs IMAGE_2.png")
    def test_compare_images(self, baseDir):
        """Test comparing IMAGE_1.jpg and IMAGE_2.png"""
        image1_path = os.path.join(baseDir, "fixtures", "images", "IMAGE_1.jpg")
        image2_path = os.path.join(baseDir, "fixtures", "images", "IMAGE_2.png")
        diff_image_path = os.path.join(baseDir, "fixtures", "screenshots", "diff_image.png")

        # Compare the images
        if not GenericFunct.compare_images(image1_path, image2_path, diff_image_path):
            assert False, "The images are not identical!"

@pytest.fixture(scope="session", autouse=True)
def test_tearDown():
    yield
    baseDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    PreviewAppFunct.closeApplication()
    GenericFunct.cleanup(baseDir)