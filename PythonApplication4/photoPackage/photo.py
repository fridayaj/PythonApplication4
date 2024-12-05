# photo.py

import os
import platform

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

    def print_photo(self, photo_file_path):
        """
        Prints the photo file path to the console with the preset message,
        and opens the image in the default image viewer.

        :param photo_file_path: The path to the photo file.
        """
        print(f"{self.preset_message} {photo_file_path}")
        
        try:
            # Open the image using the system's default viewer
            system_name = platform.system()
            if system_name == "Windows":
                os.startfile(photo_file_path)
            elif system_name == "Darwin":  # macOS
                os.system(f"open {photo_file_path}")
            else:  # Linux
                os.system(f"xdg-open {photo_file_path}")
        except Exception as e:
            print(f"Error opening photo: {e}")
