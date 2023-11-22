import json

class WonderCabinetItem:
    def __init__(self, name, description, origin):
        self.name = name
        self.description = description
        self.origin = origin
       
class WonderCabinetInventory:
    def __init__(self, file_path="wonder_cabinet_inventory.json"):
        self.file_path = file_path
        self.inventory = self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [WonderCabinetItem(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_inventory(self):
        data = [{"name": item.name, "description": item.description, "origin": item.origin}
                for item in self.inventory]
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=2)

    def add_item(self, item):
        self.inventory.append(item)
        self.save_inventory()

    def remove_item(self, item_name):
        self.inventory = [item for item in self.inventory if item.name != item_name] 
        self.save_inventory()

    def search_items(self, keyword): 
        return [item for item in self.inventory if keyword.lower() in item.name.lower()]

    def display_inventory(self):
        for item in self.inventory:
            print(f"Name: {item.name}, Description: {item.description}, Origin: {item.origin}")
        
def main():
    cabinet_inventory = WonderCabinetInventory()

    while True:
        print("\n===== Wonder Cabinet Inventory System =====")
        print("1. Add item")
        print("2. Remove item")
        print("3. Search item")
        print("4. Display inventory")
        print("0. Quit")
        print("=" * 42)
        

        choice = input("Enter you choice (0-4): ")

        if choice == "1":
            while True:
                name = input("Enter item name: ")
                if not name:
                    print("Item name cannot be empty. Please enter a valid name.")
                elif any(item.name.lower() == name.lower() for item in cabinet_inventory.inventory):
                    print("This item already exists in the inventory.")
                else:
                    break

            description = input("Enter item description: ")
            origin = input("Enter the origin of the item: ")
            new_item = WonderCabinetItem(name, description, origin)
            cabinet_inventory.add_item(new_item)
            print(f"Item '{name}' successufully added to the inventory")
            
        elif choice == "2":
            item_name = input("Enter the name of the item to remove: ")
            removed = cabinet_inventory.remove_item(item_name)
            if removed:
                print(f"Item '{item_name}' removed successfully.")
            else:
                print(" No Item  with the name '{item_name}' found in the inventory. Nothing was removed.")
            
        elif choice == "3":
            keyword = input("Enter a keyword to search for: ")
            search_results = cabinet_inventory.search_items(keyword)
            if search_results:
                print("\nSearch Results:")
                cabinet_inventory.display_inventory()
            else:
                print("No items found with that keyword!")
                
        elif choice == "4":
             print("\nCurrent Wonder Cabinet Inventory:")
             cabinet_inventory.display_inventory()

        elif choice == "0":
            print("Exiting Wonder Cabinet Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")
        
if __name__ == "__main__":
    main()