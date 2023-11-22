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
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [WonderCabinetItem(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_inventory(self):
        data = [{'name': item.name, 'description': item.description, 'origin': item.origin}
                for item in self.inventory]
        with open(self.file_path, 'w') as file:
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
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Search Items")
        print("4. Display Inventory")
        print("0. Exit")

        choice = input("Enter your choice (0-4): ")

        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            origin = input("Enter item origin: ")
            new_item = WonderCabinetItem(name, description, origin)
            cabinet_inventory.add_item(new_item)

        elif choice == '2':
            item_name = input("Enter the name of the item to remove: ")
            cabinet_inventory.remove_item(item_name)

        elif choice == '3':
            keyword = input("Enter a keyword to search for: ")
            search_results = cabinet_inventory.search_items(keyword)
            if search_results:
                print("\nSearch Results:")
                cabinet_inventory.display_inventory()
            else:
                print("No matching items found.")

        elif choice == '4':
            print("\nCurrent Wonder Cabinet Inventory:")
            cabinet_inventory.display_inventory()

        elif choice == '0':
            print("Exiting Wonder Cabinet Inventory System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()
