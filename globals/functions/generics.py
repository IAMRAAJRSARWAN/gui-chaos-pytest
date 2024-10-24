import os
import imagehash
import allure
from PIL import Image, ImageChops

class GenericFunct:
    """Generic Functions"""

    @staticmethod
    def baseDir():
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    @staticmethod
    def compare_images(image1_path, image2_path, diff_image_path):
        """Compare two images and save the diff image if they are different."""
        try:
            img1 = Image.open(image1_path)
            img2 = Image.open(image2_path)

            # Compute hash difference (you can adjust the threshold for sensitivity)
            hash1 = imagehash.average_hash(img1)
            hash2 = imagehash.average_hash(img2)

            # If the images are identical, return True
            if hash1 == hash2:
                return True

            # If the images are different, create a diff image
            diff = ImageChops.difference(img1, img2)

            # Save the diff image to the given path
            diff.save(diff_image_path)

            # Attach the diff image to Allure report
            with open(diff_image_path, 'rb') as image_file:
                allure.attach(image_file.read(), name="Diff Image", attachment_type=allure.attachment_type.PNG)

            # Return False as the images are not identical
            return False

        except Exception as e:
            print(f"Error comparing images: {e}")
            return False

    @staticmethod
    def cleanup(baseDir):
        files_to_delete = ['IMAGE_1.jpg', 'REF_Image.png']

        for file_name in files_to_delete:
            file_path = os.path.join(baseDir, 'fixtures', 'images', file_name )
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Deleted {file_name} successfully.")
                else:
                    print(f"{file_name} does not exist, skipping deletion.")
            except Exception as e:
                print(f"Error deleting {file_name}: {e}")

        files_to_delete = ['diff_image.png']

        for file_name in files_to_delete:
            file_path = os.path.join(baseDir, 'fixtures', 'screenshots', file_name )
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Deleted {file_name} successfully.")
                else:
                    print(f"{file_name} does not exist, skipping deletion.")
            except Exception as e:
                print(f"Error deleting {file_name}: {e}")