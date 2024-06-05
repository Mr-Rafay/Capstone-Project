from map import DetailedMap, Map


class Move:
    def __init__(self):
        self.map = Map()
        self.detailed_map = DetailedMap()
        self.player_position = 0
        self.room_position = (0, 0)  # Starting position within the detailed map

    def move_player(self, direction):
        if direction == 'next' and self.player_position < len(self.map.overall_map_room) - 1:
            self.player_position += 1
            self.room_position = (0, 0)  # Reset room position when moving to a new location
        elif direction == 'previous' and self.player_position > 0:
            self.player_position -= 1
            self.room_position = (0, 0)  # Reset room position when moving to a new location
        else:
            print("You cannot move in that direction")

        self.describe_current_location()

    def move_within_location(self, direction):
        _, rooms = self.detailed_map.overall_map_room[self.player_position]
        max_x = len(rooms) - 1  # Maximum x-coordinate (row index)
        max_y = len(rooms[0]) - 1  # Maximum y-coordinate (column index)

        self.room_position = self.move(self.room_position, direction, max_x, max_y)
        self.describe_current_room()

    def move(self, current_position, direction, max_x, max_y):
        x, y = current_position
        if direction == "north" and x > 0:
            current_position = (x - 1, y)
        elif direction == "south" and x < max_x:
            current_position = (x + 1, y)
        elif direction == "west" and y > 0:
            current_position = (x, y - 1)
        elif direction == "east" and y < max_y:
            current_position = (x, y + 1)
        else:
            print("You cannot move in that direction")
        return current_position

    def describe_current_location(self):
        location, _ = self.detailed_map.overall_map_room[self.player_position]
        print(f"Current location: {location}")
        self.detailed_map.print_detailed_map(location)
        self.describe_current_room()

    def describe_current_room(self):
        location, rooms = self.detailed_map.overall_map_room[self.player_position]
        x, y = self.room_position
        current_room = rooms[x][y]
        print(f"Current room in {location}: {current_room}")
