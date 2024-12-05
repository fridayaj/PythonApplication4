# movie.py
# Part 3 and 4
import json
from cryptography.fernet import Fernet

class TeamMessageDecryptor:
    def __init__(self, key: str):
        self.fernet = Fernet(key)

    def decrypt_message(self, encrypted_message: str) -> str:
        decrypted_bytes = self.fernet.decrypt(encrypted_message.encode('utf-8'))
        return decrypted_bytes.decode('utf-8')

    def decrypt_team_messages(self, filepath: str, group_name: str) -> str:
        with open(filepath, "r") as file:
            data = json.load(file)
    
        if group_name in data:
            encrypted_message = data[group_name][0]  # Assuming the first message in the list
            return self.decrypt_message(encrypted_message)
        else:
            raise ValueError(f"Team '{group_name}' not found in the file.")
# End Part 3 and 4


"""
    # Example usage
    if __name__ == "__main__":
        key = "4I6J3SZup00SUtAdrONuftccUanr6hIzq1JQKne8RsM="  # Replace with your actual Fernet key
        team_name = "AdorableRaccoon"
        filepath = "TeamsAndEncryptedMessagesForDistribution.json"

        try:
            decrypted_message = decrypt_team_messages(team_name, filepath, key)
            print(f"Decrypted message for {team_name}: {decrypted_message}")
        except Exception as e:
            print("Error:", str(e))
"""