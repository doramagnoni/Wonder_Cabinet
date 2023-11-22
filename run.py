import json
import gspread
from google.oauth2 import ServiceAccountCredentials

#Scope and Credentials


SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]

try:
    CREDS = ServiceAccountCredentials.from_json_keyfile_name("creds.json")
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

except xceptions.DefaultCredentialsError:
    print("Failed to load credentials. Check the path to your service account JSON file.")

class WonderCabinetItem:
    def __init__(self, name, description, origin, care_tips):
        self.name = name
        self.description = description
        self.origin = origin
        self.care_tips = care_tips


        

class WonderCabinetInventory:
    def __init__(self, file_path="wonder_cabinet_inventory.json"):
        self.file_path = file_path
        self.inventory = self._load_inventory()

def load_inventory(self):
    try:
        with open(self.file_path, 'r') as file:
            data = json.loads(file.read())
            return [WonderCabinetInventory(**item) for item in data]
    except FileNotFoundError:
        return []

