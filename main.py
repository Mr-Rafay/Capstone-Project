#main.py
from map import DetailedMap, Map
from Move import Move


def main():
    move = Move()
    map = Map()
    map2 = DetailedMap()
    print("Welcome to Daredevil: Man Without Fear")
    print("You are Daredevil, the protector of Hell's Kitchen")
    print("Your mission is to rid the streets of crime.")

    while True:
        map.print_game_map_table()
        move.describe_current_location()
        print("What do you want to do?")
        print("1. Move between locations")
        print("2. Move within location")
        print("3. View Map")
        print("4. Quit")
        user_choice = input().lower()

        if user_choice == "1":
            print("Choose a location you want to travel to: ")
            map.print_location_table()
            location_name = input("Enter the name of the location: ").strip()
            move.move_player(location_name)
        elif user_choice == "2":
            print("Where do you want to move in this location?")
            action = input().lower()
            if action in ["north", "east", "south", "west"]:
                move.move_within_location(action)
        elif user_choice == "3":
            map2.view_map()
        elif user_choice == "4":
            print("Thanks for playing")
            break 
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()

    


