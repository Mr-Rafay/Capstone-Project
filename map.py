from tabulate import tabulate

# overall_map_room
overall_map_room = [
    ("Hell's Kitchen Docks", ["Shipping Bay", "Smuggler's Den", "Warehouse", 
                             "Secret Passage", "Office", "Lookout Point"]),
    ("Gang Hideout", ["Main Hall", "Weapon Storage", "Leader's Room", "Secret Exit", 
                     "Surveillance Room", "Torture Chamber"]),
    ("Hell's Kitchen Downtown", ["Bar", "Apartment Block", "Grocery Store", 
                                "Bank", "Police Station", "Hospital"]),
    ("Alleyway", ["Backstreet", "Hidden Nook", "Garbage Dump", "Fire Escape", 
                 "Dead End", "Underground Entrance"]),
    ("New York Bulletin Building", ["Newsroom", "Editor's Office", "Archive Room",
                                    "Cafeteria", "Printing Press", "Rooftop"]),
    ("Prison", ["Cell Block", "Guard Room", "Warden's Office",
                "Cafeteria", "Gym", "Solitary Confinement"]),
    ("Wilson Fisk's Penthouse", ["Living Room", "Study", "Art Gallery",
                                "Safe Room", "Master Bedroom", "Private Balcony"])
]

def print_game_map_table(map_list):
    headers = ['Location', 'Rooms']
    table_data = [(location, ', '.join(rooms)) for location, rooms in map_list]
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

