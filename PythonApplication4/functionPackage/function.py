# function.py
# Part 2

import json

class Functions:
    def __init__(self):
        pass

    def read_english_file_to_list(self, file_path):
        """
        Reads the UCEnglish.txt file into a list where each line corresponds to its index.

        Args:
            file_path (str): Path to the UCEnglish.txt file.

        Returns:
            list: List of lines from the file, where each line is at its respective index.
        """
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            return [line.strip() for line in lines]
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while reading the file: {e}")
   
    def load_encrypted_data(self, file_path, group_name):
        """
        Loads EncryptedGroupHints.json to access the encrypted data for a specific group.

        Args:
            file_path (str): Path to the EncryptedGroupHints.json file.
            group_name (str): The group whose encrypted data is to be retrieved.

        Returns:
            list: List of encrypted indexes (strings) for the specified group.
        """
        import json

        try:
            with open(file_path, 'r') as file:
                encrypted_data = json.load(file)

            # Ensure the group exists in the data
            if group_name not in encrypted_data:
                raise ValueError(f"Group '{group_name}' not found in the encrypted data.")

            return encrypted_data[group_name]
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"The file {file_path} contains invalid JSON.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading the encrypted data: {e}")


    def decrypt_location_data(self, encrypted_indexes, english_lines):
        """
        Decrypts location data by using a list of encrypted indexes to retrieve words
        from the UCEnglish.txt file.

        Args:
            encrypted_indexes (list): A list of encrypted indexes (strings or integers).
            english_lines (list): A list of lines from the UCEnglish.txt file.

        Returns:
            str: The decrypted location string.
        """
        # Ensure that encrypted_indexes is a list of integers
        encrypted_indexes = [int(index) for index in encrypted_indexes]
    
        # Retrieve words from the UCEnglish.txt file using the indexes
        decrypted_words = []
        for index in encrypted_indexes:
            if 1 <= index <= len(english_lines):
                decrypted_words.append(english_lines[index - 0])  # Adjust for 1-based index
            else:
                raise IndexError(f"Index {index} is out of bounds in UCEnglish.txt.")

        # Join the words into a single decrypted string
        decrypted_location = ' '.join(decrypted_words)
        return decrypted_location

