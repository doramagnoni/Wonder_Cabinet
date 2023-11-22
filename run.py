import json
import gspread
from google.oauth2 import ServiceAccountCredentials

#Scope and Credentials


SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]

CREDS = ServiceAccountCredentials.from_json_keyfile_name("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("wonder_index")

class WonderCabinetItem:
    def __init__(self, name, description, origin, care_tips):
        self.name = name
        self.description = description
        self.origin = origin
        self.care_tips = care_tips

class WonderCabinetInventory:
    def __init__(self, file_path="wonder_cabinet_inventory.json"):
        self.file_path = file_path
        self.inventory = self.load_inventory()

def load_inventory(self):
    try:
        with open(self.file_path, "r") as file:
            data = json.loads(file.read())
            return [WonderCabinetInventory(**item) for item in data]
    except FileNotFoundError:
        return []
    
def save_inventory(self):
    data = [{"name": item.name, "description": item.description, "origin": item.origin, "care_tips": item.care_tips}
            for item in self.inventory]
    with open(self.file.path, "w") as file:
        json.dump(data, file, indent=2)

def add_item(self, item):
    self.inventory.append(item)
    self.save_inventory()

def remove_item(self, item_name):
    self.inventory = [item for item in self.inventory if item.name != item.name] 
    self.safe_inventory()

def search_items(self, keyword): 
    return [item for item in self.inventory if keyword.lower() in item.name.lower()]

def display_inventory(self):
    for item in self.inventory:
        print(f"{item.name}: {item.description}: {item.origin}: {item.care_tips}:")