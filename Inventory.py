#inventory.py
# from map import Map
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, description):
        self.items[item] = description
        print(f"Added {item}" to inventory)

    def remove_item(self, item):
        if item in self.items:
            del self.items:
            print(f"Removed {item} from the inventory.")
        else:
            print(f"You don't have {item} in your inventory")
    
    def view_inventory(self):
        if not self.itmes:
            print("Your inventory is empty")
            for item, description in self.items.items():
                print(f"{item}": {desctiption})

    def use_item(self, item):
        if item in self.items:
            print(f"You used {item} : {self.items[item]}")
            self.remove_item(item)
        else:
            print(f"You don't have {item} in your inventory.")