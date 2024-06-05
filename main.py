#main.py
from map import DetailedMap, Map
from Move import Move


def main():
    move = Move()
    move.describe_current_location()

    while True:
        print("/nEnter 'next' to move to the next location,"+
              " 'previous' to move to the previous location.")
        print("'North', 'East', 'South', 'West'to move within the current location")
        user_input = input("Your choice: ").strip().lower()

        if user_input in ['next', 'previous']:
            move.move_player(user_input)
        elif user_input in ['North', 'East', 'South', 'West']:
            move.move_within_location(user_input)
        elif user_input == "quit":
            print("Thank you for playing")
            break
        else: 
            print("Invalid Output.")
         
if __name__ == "__main__":
    game_map = Map()
    game_map.print_game_map_table() 
    detailed_map = DetailedMap()
    #print("\nHell's Kitchen Docks Map")
    detailed_map.print_detailed_map("Alleyway")
    main()
    


