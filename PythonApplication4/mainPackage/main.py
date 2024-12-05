# main.py

from functionPackage.function import Functions
from moviePackage.movie import TeamMessageDecryptor
from photoPackage.photo import *

# Part 7
if __name__ == "__main__":
    # Instantiate the Functions class
    func = Functions()

# Part 2
    # Path to UCEnglish.txt
    english_path = "data/UCEnglish.txt"
    try:
        lines_list = func.read_english_file_to_list(english_path)
        print(f"Loaded {len(lines_list)} lines from {english_path}.")
        print("First 5 lines:", lines_list[:5])
    except Exception as e:
        print(f"Error: {e}")

    # Path to EncryptedGroupHints.json
    encrypt_path = "data/EncryptedGroupHints Fall 2024 Section 001.json"
    group_name = "AdorableRaccoon"  # Specify the group you want to use

    try:
        encrypted_indexes = func.load_encrypted_data(encrypt_path, group_name)
        print(f"Loaded encrypted data for '{group_name}': {encrypted_indexes}")

        # Decrypt the location using the encrypted indexes and UCEnglish.txt lines
        decrypted_location = func.decrypt_location_data(encrypted_indexes, lines_list)
        print(f"Decrypted Location: {decrypted_location}")
    except Exception as e:
        print(f"Error: {e}")
# End Part 2

# Part 3 and 4

 # Decrypt the team message
    # Path to TeamsAndEncryptedMessagesForDistribution.json
    message_filepath = "data/TeamsAndEncryptedMessagesForDistribution.json"
    fernet_key = "4I6J3SZup00SUtAdrONuftccUanr6hIzq1JQKne8RsM="  # Replace with the actual key

    try:
        # Instantiate the TeamMessageDecryptor class
        decryptor = TeamMessageDecryptor(fernet_key)

        # Decrypt the message for the same group
        decrypted_message = decryptor.decrypt_team_messages(message_filepath, group_name)
        print(f"Decrypted Message for '{group_name}': {decrypted_message}")
    except Exception as e:
        print(f"Error decrypting team message: {e}")
# End Part 3 and 4

# Part 6
    """
    Main function to demonstrate the PhotoPrinter class.
    """
    photo_path = "data/example_photo.jpg"
    # Instantiate the PhotoPrinter with a custom preset message
    printer = PhotoPrinter("Displaying photo file:")

    # Use the print_photo method with the correct file path
    printer.print_photo(photo_path)
    # End Part 6


