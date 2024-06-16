from Interact import Interact
from Inventory import Inventory
from map import DetailedMap, Map
from move import Move


def main():
    move = Move()
    map = Map()
    map2 = DetailedMap()
    int = Interact(map.rooms_clues.keys())
    inv = Inventory()
    print("Welcome to Daredevil: Man Without Fear")
    print("You are Daredevil, the protector of Hell's Kitchen")
    print("Your mission is to rid the streets of crime.")

    while True:
        map.print_game_map_table()
        move.describe_current_location()
        move.describe_current_room()
        print("\nWhat do you want to do?")
        print("1. Move between locations")
        print("2. Move within location")
        print("3. View Current Location Map")
        print("4. View Locations Map")
        print("5. View Inventory")
        print("6. Interact")
        print("7. Quit")
        user_choice = input().lower()

        if user_choice == "1":
            map.print_location_table()
            location_name = input("Choose a location to travel to: ").strip()
            move.move_to_location(location_name)
        elif user_choice == "2":
            action = input("Where do you want to move within the location? (north, " 
            + "south, east, west): ").lower()
            move.move_within_location(action)
        elif user_choice == "3":
            location_name = (list(move.map.overall_map_room.keys())
                             [move.player_position])
            map2.print_detailed_map(location_name)
            map2.view_map()
        elif user_choice == "4":
            map.print_location_table()
        elif user_choice == "5":
            inv.view_inventory()
        elif user_choice == "6":
            print(" ")
        elif user_choice == "7":
            print("Thanks for playing")
            break 
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()






