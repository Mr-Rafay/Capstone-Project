
def get_current_location_index(map_list, current_location):
    for index, (location, _) in enumerate(map_list):
        if location == current_location:
            return index
    return -1

def move_to_location(map_list, current_location, new_location):
    current_index = get_current_location_index(map_list, current_location)
    if current_index == -1:
        print("Invalid current location")
        return current_location

    if new_location in [location for location, _ in map_list]:
        return new_location
    else:
        print("Invalid new location")
        return current_location


