import json

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
