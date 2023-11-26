import json
import os

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
        if any(existing_item.name.lower() == item.name.lower() for existing_item in self.inventory):
            return False
        else:
            self.inventory.append(item)
            self.save_inventory()
            return True

    def remove_item(self, item_name):
        initial_length = len(self.inventory)
        self.inventory = [item for item in self.inventory if item.name != item_name] 
        if len(self.inventory) < initial_length:
            self.save_inventory()
            return True
        else:
            return False

    def search_items(self, keyword): 
        return [item for item in self.inventory if keyword.lower() in item.name.lower()]

    def display_inventory(self):
        for item in self.inventory:
            print(f"\nName: {item.name}, Description: {item.description}, Origin: {item.origin}")

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
        
def main():
    cabinet_inventory = WonderCabinetInventory()

    while True:
        clear_screen()
        print("\n===== Wonder Cabinet Inventory System =====")
        print("1. Add item")
        print("2. Remove item")
        print("3. Search item")
        print("4. Display inventory")
        print("0. Quit")
        print("=" * 43)
        

        choice = input("\nEnter you choice (0-4): ").lower()

        if choice == "1":
            while True:
                clear_screen()
                print("\n===== Add Item to the Inventory =====")
                print("\nEnter 'back' to return to the main menu.")

                name = input("Enter item name: ").lower()

                if name == "back":
                    break

                elif not name:
                    print("Item name cannot be empty. Please enter a valid name.")
                elif any(item.name.lower() == name.lower() for item in cabinet_inventory.inventory):
                    print("This item already exists in the inventory.")
                else:
                     description = input("Enter item description: ")
                     origin = input("Enter the origin of the item: ")
                     new_item = WonderCabinetItem(name, description, origin)
                
                     if cabinet_inventory.add_item(new_item):
                        print("Item successufully added to the inventory.")
                     else:
                        print("Failed to add an item. Please, try again.")
                     break
            
        elif choice == "2":
            clear_screen()
            item_name = input("Enter the name of the item to remove: ").lower()
            removed = cabinet_inventory.remove_item(item_name)

            if removed:
                print("The item was removed successfully.")
            else:
                print("No such item found in the inventory. Nothing was removed.")

            
        elif choice == "3":
            clear_screen()
            keyword = input("Enter a keyword to search for: ").lower()
            search_results = cabinet_inventory.search_items(keyword)
            if search_results:
                print("\nSearch Results:")
                for item in search_results:
                    print(f"Name: {item.name}, Description: {item.description}, Origin: {item.origin} ")
            else:
                print("No items found with that keyword!")
                
        elif choice == "4":
             clear_screen()
             print("\nCurrent Wonder Cabinet Inventory:")
             cabinet_inventory.display_inventory()
             

        elif choice == "0":
            print("Exiting Wonder Cabinet Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")
        input("Press Enter to continue...")
        
if __name__ == "__main__":
    main()