#inventory.py
# from map import Map
class Inventory:
    def __init__(self):
        self.items = {"Batons":"2 Batons"}

    def add_item(self, item):
        print(f"Added {item} to inventory")

    def view_inventory(self):
        """
        Lets the user view inventory
        """
        if not self.items:
            print("Your inventory is empty")
            for item, description in self.items.items():
                print(f"{item}: {description}")


   