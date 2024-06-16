from Inventory import Inventory
from map import DetailedMap, Map


class Interact():
        def __init__(self, rooms_clues):
            self.rooms_clues = rooms_clues
            self.inv = Inventory()
        
                
            }


        def take_clue(self, room_name, clue1):
            if room_name in self.rooms_clues and clue1 in self.rooms_clues[room_name]:
                
                self.collected_clues.append(self.rooms_clues[room_name][clue1])
                del self.rooms_clues[room_name][clue1]
                print(f"You have taken the {clue1} clue from the {room_name}.")
            else:
                print("Invalid room name or clue.")

        def examine_clues(self, clue2):
            if clue2 in self.gen_clue:
                print(self.gen_clue[clue2])
            else:
                print("No clues collected yet.")

        
