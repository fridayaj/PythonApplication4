# photo.py

import os
import platform
from PIL import Image  # Correct import for Image

class PhotoPrinter:
    """
    A class to handle photo printing tasks.
    """

    def __init__(self, preset_message="Photo file:"):
        """
        Initialize the PhotoPrinter with a preset message.

        :param preset_message: The message to display with the photo file.
        """
        self.preset_message = preset_message

    def print_image(self, file_path):
        try:
            # Corrected line: using Image.open() instead of image.open()
            image = Image.open(file_path)
            image.show()  # Opens the image with the default viewer
        except Exception as e:
            print(f"Error: {e}")
