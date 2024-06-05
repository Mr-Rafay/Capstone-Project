#map.py
from tabulate import tabulate


# overall_map_room
class Map:

    def __init__(self):
        self.overall_map_room = [
            ("Hell's Kitchen Docks", [
                "Shipping Bay", "Smuggler's Den", "Warehouse",
                "Secret Passage", "Office", "Lookout Point"]
            ),
            ("Gang Hideout", [
                "Main Hall", "Weapon Storage", "Leader's Room", "Secret Exit",
                "Surveillance Room", "Torture Chamber"]
            ),
            ("Hell's Kitchen Downtown", [
                "Bar", "Apartment Block", "Grocery Store", "Bank",
                "Police Station", "Hospital"]
            ),
            ("Alleyway", [
                "Backstreet", "Hidden Nook", "Garbage Dump", "Fire Escape",
                "Dead End", "Underground Entrance"]
            ),
            ("New York Bulletin Building", [
                "Newsroom", "Editor's Office", "Archive Room", "Cafeteria",
                "Printing Press", "Rooftop"]
            ),
            ("Prison", [
                "Cell Block", "Guard Room", "Warden's Office", "Cafeteria",
                "Gym", "Solitary Confinement"]
            ),
            ("Wilson Fisk's Penthouse", [
                "Living Room", "Study", "Art Gallery", "Safe Room",
                "Master Bedroom", "Private Balcony"
            ])
        ]

    def print_game_map_table(self):
        headers = ['Location', 'Rooms']
        table_data = [(location, ', '.join(rooms))
                      for location, rooms in self.overall_map_room]
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

class DetailedMap(Map):
    def __init__(self):
        super().__init__()

    def print_detailed_map(self, location):
        for loc, rooms in self.overall_map_room:
            if loc == location:
                rows = [rooms[i:i+3] for i in range(0, len(rooms), 3)]
                print(tabulate(rows, tablefmt='grid'))
                return 
        print(f"No detailed map found for {location}")
