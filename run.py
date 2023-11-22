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
        self.inventory = self.load_inventory()

def load_inventory(self):
    try:
        with open(self.file_path, "r") as file:
            data = json.loads(file.read())
            return [WonderCabinetInventory(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
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
        
def main():
    cabinet_inventory = WonderCabinetInventory()

    while True:
        print("\n===== Wonder Cabinet Inventory System =====")
        print("1. Add item")
        print("2. Remove item")
        print("3. Search item")
        print("4. Display inventory")
        print("5. Quit")

        choice = input("Enter you choice (1-5):")

        if choice == '1':
            name = input ("Enter item name: ")
            description = input ("Enter item description: ")
            origin = input ("Enter the origin of the item: ")
            care_tips = input ("Enter any special care tips: ")
            new_item = WonderCabinetInventory(name, description, origin, care_tips)
            cabinet_inventory.add_item(new_item)
            
        elif choice == '2':
            item_name = input ("Enter the name of the item to remove: ")
            cabinet_inventory.remove_item(item_name)
            
        elif choice == '3':
            keyword = input ("Enter a keyword to search for: ")
            search_results = cabinet_inventory.search_items(keyword)
            if search_results:
                print("\nSearch Results:")
                cabinet_inventory.display_inventory
            else:
                print("No items found with that keyword!")
                
        elif choice == '4':
             print("\nCurrent Wonder Cabinet Inventory:")
             cabinet_inventory.display_inventory()

        elif choice == '5':
            print("Exiting Wonder Cabinet Inventory System. Goodbuy!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
        if __name__ == "__main__":
            main()