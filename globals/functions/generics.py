import os
import imagehash
import allure
from PIL import Image, ImageChops

class GenericFunct:
    """Image Processing Functions"""

    @staticmethod
    def baseDir():
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    @staticmethod
    def compare_images_average_hash(image1_path, image2_path, diff_image_path):
        """Compare two images and save the diff image if they are different."""
        try:
            img1 = Image.open(image1_path)
            img2 = Image.open(image2_path)

            # Compute AverageHash difference
            avg_hash1 = imagehash.average_hash(img1)
            avg_hash2 = imagehash.average_hash(img2)

            # If the images are identical, return True
            if avg_hash1 == avg_hash2:
                return True
            os.makedirs(os.path.dirname(diff_image_path), exist_ok=True) # Ensure the directory exists for the diff image path
            diff = ImageChops.difference(img1, img2) # If the images are different, create a diff image
            diff.save(diff_image_path) # Save the diff image to the given path

            # Attach the diff image to Allure report
            with open(diff_image_path, 'rb') as image_file:
                allure.attach(image_file.read(), name="Diff Image", attachment_type=allure.attachment_type.PNG)
            # Attach Failure Diff Images to Allure Report
            failure_reason = "Average Hash Image Comparison Failed."
            allure.attach(failure_reason, name="Failure Reason", attachment_type=allure.attachment_type.TEXT)

            # Return False as the images are not identical
            return False

        except (ValueError, IOError, TypeError) as exception:
            error_message = "Error During AverageHash Image Comparison: {exception}"
            allure.attach(error_message, name="Error", attachment_type=allure.attachment_type.TEXT)
            print(error_message)
            return False

    @staticmethod
    def compare_images_perceptual_hash(image1_path, image2_path, diff_image_path):
        """Compare two images and save the diff image if they are different."""
        try:
            img1 = Image.open(image1_path)
            img2 = Image.open(image2_path)

            # Compute PerceptualHash Difference
            per_hash1 = imagehash.phash(img1)
            per_hash2 = imagehash.phash(img2)

            # If the images are identical, return True
            if per_hash1 == per_hash2:
                return True
            os.makedirs(os.path.dirname(diff_image_path), exist_ok=True) # Ensure the directory exists for the diff image path
            diff = ImageChops.difference(img1, img2) # If the images are different, create a diff image
            diff.save(diff_image_path) # Save the diff image to the given path

            # Attach the diff image to Allure report
            with open(diff_image_path, 'rb') as image_file:
                allure.attach(image_file.read(), name="Diff Image", attachment_type=allure.attachment_type.PNG)
            # Attach Failure Diff Images to Allure Report
            failure_reason = "Perceptual Hash Image Comparison Failed."
            allure.attach(failure_reason, name="Failure Reason", attachment_type=allure.attachment_type.TEXT)

            # Return False as the images are not identical
            return False

        except (ValueError, IOError, TypeError) as exception:
            error_message = "Error During PerceptualHash Image Comparison: {exception}"
            allure.attach(error_message, name="Error", attachment_type=allure.attachment_type.TEXT)
            print(error_message)
            return False

    @staticmethod
    def compare_images_color_hash(image1_path, image2_path, diff_image_path):
        """Compare two images and save the diff image if they are different."""
        try:
            img1 = Image.open(image1_path)
            img2 = Image.open(image2_path)

            # Compute PerceptualHash Difference
            clr_hash1 = imagehash.colorhash(img1)
            clr_hash2 = imagehash.colorhash(img2)

            # If the images are identical, return True
            if clr_hash1 == clr_hash2:
                return True
            os.makedirs(os.path.dirname(diff_image_path), exist_ok=True) # Ensure the directory exists for the diff image path
            diff = ImageChops.difference(img1, img2)  # If the images are different, create a diff image
            diff.save(diff_image_path) # Save the diff image to the given path

            # Attach the diff image to Allure report
            with open(diff_image_path, 'rb') as image_file:
                allure.attach(image_file.read(), name="Diff Image", attachment_type=allure.attachment_type.PNG)
            # Attach Failure Diff Images to Allure Report
            failure_reason = "Color Hash Image Comparison Failed."
            allure.attach(failure_reason, name="Failure Reason", attachment_type=allure.attachment_type.TEXT)

            # Return False as the images are not identical
            return False

        except (ValueError, IOError, TypeError) as exception:
            error_message = "Error During PerceptualHash Image Comparison: {exception}"
            allure.attach(error_message, name="Error", attachment_type=allure.attachment_type.TEXT)
            print(error_message)
            return False

    """Generic Functions"""

    @staticmethod
    def cleanup():
        files_to_delete = {
            'fixtures/sourceImages': ['IMAGE_1.jpg', 'REF_Image.png'],
            'fixtures/screenshots': ['DIFF_Image.png']
        }

        baseDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))

        for directory, file_names in files_to_delete.items():
            for file_name in file_names:
                file_path = os.path.join(baseDir, directory, file_name)
                try:
                    if os.path.exists(file_path):
                        os.remove(file_path)
                        print(f'Deleted {file_name} successfully.')
                    else:
                        print(f'{file_name} does not exist, skipping deletion.')
                except Exception as e:
                    print(f'Error deleting {file_name}: {e}')