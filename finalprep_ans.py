rooms = {
"Bedroom": {"pathways": {"d": "Bathroom", "s": "Hallway"}, "open_with": ""},
"Hallway": {"pathways": {"w": "Bedroom", "a": "Kitchen"}, "open_with": ""},
"Bathroom": {"pathways": {"a": "Bedroom"}, "open_with": "Key 1"},
"Kitchen": {"pathways": {"d": "Hallway", "w": "Outside"}, "open_with": ""},
"Outside": {"pathways": {"s": "Kitchen"}, "open_with": "Key 2"},
}

pickable_objects = {
"Key 1": {"location": "Hallway", "picked": False},
"Key 2": {"location": "Bathroom", "picked": False},
"Key 3": {"location": "Kitchen", "picked": False},
}


# Question: Get the pathways for Bathroom.
# Expected output:
# {"a": "Bedroom"}
# for room or pathways not found, return {} (an empty dictionary)
def get_bathroom_pathways():
    bath_paths = rooms.get("Bathroom", {}).get("pathways", {})
    return bath_paths


# Question: Print the pathways for all rooms.
# Expected output:
# Bedroom {'d': 'Bathroom', 's': 'Hallway'}
# Hallway {'w': 'Bedroom', 'a': 'Kitchen'}
# Bathroom {'a': 'Bedroom'}
# Kitchen {'d': 'Hallway', 'w': 'Outside'}
# Outside {'s': 'Kitchen'}
# for room or pathways not found, print {} (an empty dictionary)
def get_all_room_pathways():
    for room in rooms.keys():
        path = rooms[room].get("pathways", {})
        print(f"{room} {path}")



# Question: Get the "w" direction room name in pathways for all rooms.
# Expected output:
# Bedroom with w direction: Not found
# Hallway with w direction: Bedroom
# Bathroom with w direction: Not found
# Kitchen with w direction: Outside
# Outside with w direction: Not found
def get_w_pathways_for_all_rooms():
    for room in rooms.keys():
        path = rooms[room].get("pathways", {}).get("w", "Not found")
        print(f"{room} with w direction: {path}")



# Question: Print rooms that open with a key and print both the room name and key.
# Expected output:
# Bathroom: Key 1
# Outside: Key 2
def print_rooms_that_open_with_keys():
    for room_name, room_info in rooms.items():
        key = room_info.get("open_with", "")
        if key != "":
            print(f"{room_name}: {key}")


# Question: Print each key and the room it opens. If a key does not open a room, print the key by itself.
# Expected output:
# Key 1 Bathroom
# Key 2 Outside
# Key 3
def print_key_room_matches():
    for key in pickable_objects.keys():
        found = False
        for room, info in rooms.items():
            if key == info.get("open_with", ""):
                found = True
                print(key, room)
        if not found:
            print(key)





# Question: Starting from a room, which exits lead to locked rooms?
# Expected output:
# exits_to_locked_rooms_from("Kitchen") should return ['Outside']
# exits_to_locked_rooms_from("Hallway") should return []
def exits_to_locked_rooms_from(room_name):
    
    locked_pathways = []

    room_directions = rooms.get(room_name, {}).get("pathways", {})
    if room_directions == {}:
        return []
    
    for next_room_name in room_directions.values():
        key = rooms.get(next_room_name, {}).get("open_with", "")
        if key:
            locked_pathways.append(next_room_name)

    return locked_pathways
    



# Question: What key do you need to enter a target room, and where is that key located?
# Expected output:
# travel_hint_to("Bathroom") should output: Bathroom needs Key 1. Key 1 is in Hallway.
# travel_hint_to("Outside") should output: Outside needs Key 2. Key 2 is in Bathroom.
# travel_hint_to("Kitchen") should output: Kitchen does not require a key.
def travel_hint_to(room_name):
    room = rooms.get(room_name, {})
    if not room:
        return
    
    key_needed = room.get("open_with", "")

    if key_needed == "":
        print(f"{room_name} does not require a key.")
        return

    key_location = pickable_objects.get(key_needed, {}).get("location", "")

    print(f"{room_name} needs {key_needed}. {key_needed} is in {key_location}.")



# Question: Return a list of pathways leading to rooms that are directly accessible.
# Expected output:
# get_directions("Bedroom") should return ['s']
# get_directions("Hallway") should return ['w', 'a']
# get_directions("Kitchen") should return ['d']
# get_directions("Garage") should return []
def get_directions(location):
    
    open_directions = []
    
    if rooms.get(location, {}) == {}:
        return []

    for path, room_name in rooms[location].get("pathways", {}).items():
        if rooms.get(room_name, {}).get("open_with", "") == "":
            open_directions.append(path)

    return open_directions


print("Bathroom pathways")
print(get_bathroom_pathways())

print("All rooms pathways")
get_all_room_pathways()

print("Get w directions for all rooms")
get_w_pathways_for_all_rooms()

print("Print rooms that open with keys")
print_rooms_that_open_with_keys()

print("Print key and rooms match")
print_key_room_matches()


print("Room that leads to locked rooms")
print(exits_to_locked_rooms_from("Kitchen"))

print("Key needed and location")
travel_hint_to("Bathroom")

print("Open directions")
print(get_directions("Hallway"))