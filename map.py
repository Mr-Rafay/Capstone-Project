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

    def print_game_map_table(self, filename="Location_map.txt"):
        headers = ['Location', 'Rooms']
        table_data = [(location, ', '.join(rooms))
                      for location, rooms in self.overall_map_room]
        table = tabulate(table_data, headers=headers, tablefmt='grid')

        try:
            with open(filename, 'w') as file:
                file.write(table)
        except IOError:
            print("Unble to export map layout")

    def print_location_table(self):
        """
        Prints just the location names in a table. 
        """
        locations = [location for location, _ in self.overall_map_room]
        rows = [locations[i:i +7]for i in range(0, len(locations), 7)]
        print(tabulate(rows, tablefmt='grid', headers=["Locations"]))
        
    def get_location_index(self, location_name):
        """
        Will collect the index of a location in the overall map list
        """
        for index, (location, _) in enumerate(self.overall_map_room):
            if location == location_name:
                return index 
            return -1

class DetailedMap(Map):
    def __init__(self):
        super().__init__()

    def print_detailed_map(self, location, filename='Rooms_map.txt'):
        for loc, rooms in self.overall_map_room:
            if loc == location:
                rows = [rooms[i:i+3] for i in range(0, len(rooms), 3)]
                table = tabulate(rows, tablefmt='grid')
                try:
                    with open(filename, 'w') as file:
                        file.write(table)
                except IOError:
                    print(f"Unable to export detailed map for {location}")
                return 
        print(f"No detailed map found for {location}")

    def view_map(self, filename="detailed_map"):
        """
        Displays the map file content
        """
        try:
            with open(filename, 'r') as file:
                print(file.read())
        except IOError:
            print("Error: Unable to read the map file.")