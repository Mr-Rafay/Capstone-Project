#move.py
from map import DetailedMap, Map


class Move:
    def __init__(self):
        self.map = Map()
        self.detailed_map = DetailedMap()
        self.player_position = 0


    def move_player(self, direction):
        if direction == 'next' and self.player_position <len(self.map.overall_map_room) - 1:
            self.player_position += 1
        elif direction == 'previous' and self.player_position > 0:
            self.player_position -= 1

        self.describe_current_location()


    def describe_current_location(self):
        location,_ = self.detailed_map.overall_map_room[self.player_position]
        print(f"Current location: {location}")
        self.detailed_map.print_detailed_map(location)

    """
    def search_area(self):
        location, rooms = self.map.overall_map_room[self.player_position]
        print(f"searching in {location}")
        print(f"you found:" , ','.join(rooms))


    def quit_game(self:)
      print("Thank you for playing. Goodbye")
      exit()
    """#I have put doc strings because this will come into play late on.