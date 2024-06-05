#main.py
from map import DetailedMap, Map

if __name__ == "__main__":
    game_map = Map()
    game_map.print_game_map_table() 
    detailed_map = DetailedMap()
    #print("\nHell's Kitchen Docks Map")
    detailed_map.print_detailed_map("Alleyway")
    


