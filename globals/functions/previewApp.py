import subprocess
import time
import os
import pyautogui

class PreviewAppFunct:
    """Actions Functions of Preview App"""

    @staticmethod
    def openApplication(appname):
        """Method to open the Preview application on macOS."""
        try:
            subprocess.Popen(['open', '-a', appname])
            time.sleep(2)  # Wait for the application to launch
            return True
        except FileNotFoundError as e:
            print(f"Error Opening Application: {e}")
            return False

    @staticmethod
    def selectImage(image_path):
        """Method to select an image using pyautogui."""

        if not os.path.isfile(image_path):
            print(f"Error: The image file '{image_path}' does not exist.")
            return False

        directory, file_name = os.path.split(image_path)

        pyautogui.hotkey('command', 'o')
        time.sleep(1)  # Wait for the dialog to open

        pyautogui.write(directory, interval=0.05)
        pyautogui.press('enter')
        time.sleep(1)  # Wait for the directory to open

        pyautogui.write(file_name, interval=0.05)
        pyautogui.press('enter')  # Select the file
        time.sleep(2)  # Wait for the image to load in Preview

        return False

    @staticmethod
    def saveAsImage(ref_fileName):
        """Method to save the opened image as a reference image."""
        # Open the "Save As" dialog in Preview
        pyautogui.hotkey('command', 'shift', 's')
        time.sleep(2)  # Wait for the dialog to open

        # Type the reference image name
        pyautogui.write(ref_fileName, interval=0.05)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)

    @staticmethod
    def exportImageAsJPEG():
        """Method to export the currently opened image in Preview as JPG format."""

        pyautogui.hotkey('command', 'shift', '/')
        time.sleep(2)

        # Type 'Export' to search for the Export option
        pyautogui.write('Export', interval=0.1)
        time.sleep(2)

        pyautogui.press('down')
        time.sleep(2)

        # Press 'Return' to select Export from the menu
        pyautogui.press('enter')
        time.sleep(2)

        # Type the file name
        # Unstable Actions #Skipped
        # pyautogui.write(export_file_name, interval=0.05)
        # time.sleep(1)  # Wait a bit before pressing Tab

        # Press "Tab" to move to the file format dropdown
        pyautogui.press('tab', presses=4, interval=0.5)
        time.sleep(2)

        # Type 'j or jpeg' to select the "JPEG" option
        pyautogui.press('j')
        time.sleep(2)

        # Press "Tab" to move to Save Button
        pyautogui.press('tab', presses=3, interval=0.5)
        time.sleep(2)

        # # Press 'Enter' again to save the file
        pyautogui.press('enter')
        time.sleep(2)  # Wait for the export to complete

    @staticmethod
    def closeApplication():
        try:
            # Kill the Preview app
            subprocess.call(['pkill', 'Preview'])
            time.sleep(2)
            print("Preview app closed successfully.")
        except Exception as e:
            print(f"Error closing Preview app: {e}")

    """Assert Functions"""

    @staticmethod
    def assertAppOpenState(actualState):
        """Check if the application is open, raise an error if not."""
        if not actualState:
            raise AssertionError("Error: Failed to open the Preview application.")

    @staticmethod
    def assertcheckFileExists(filepath):
        """Check if the specified file exists and raise an exception if not."""
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"Error: The file '{filepath}' was not found.")
        return True