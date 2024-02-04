import random


class Rooms:
    def __init__(self, name: str):
        self.name = name
        self.doors = []

    def add_door(self, door):
        self.doors.append(door)

    def player_can_look_around(self):
        print(f"You're in the {self.name}.")
        self.view_all_doors_in_the_room()

    def view_all_doors_in_the_room(self):
        print(f"This room has {len(self.doors)} doors:")
        for number, door in enumerate(self.doors):
            print(f"{number + 1}. {door.name}")


class Doors:
    def __init__(self, name, room):
        self.name = name
        self.portal_in_room = room

    def get_the_room_where_the_door_leads(self):
        return self.portal_in_room


class Player:
    def __init__(self, name, start_location):
        self.name = name
        self.location = start_location

    def look_around(self):
        self.location.player_can_look_around()

    def enter_a_room(self, door_number):
        if door_number <= len(self.location.doors):
            door = self.location.doors[door_number - 1]
            print(f"You walk through the door {door.name}.")
            new_room = door.portal_in_room
            self.location = new_room
            print(f"You entered the {self.location.name} room.")
        else:
            print("There is no such door.")


def create_labyrinth():
    all_rooms = []
    all_doors = []
    rooms_name = [
        "Room with a fireplace", "Room with paintings", "Room with books", "Room with mirrors", "Room with flowers",
        "Room with a fountain", "Room with musical instruments", "Room with chess", "Room with puzzles",
        "Room with treasures", "Exit"
    ]
    doors_name = [
        "Door with a fiery pattern", "Door with a watery pattern", "Door with an earthy pattern",
        "Door with an airy pattern", "Door with a wooden pattern", "Door with a metallic pattern",
        "Door with a stone pattern", "Door with a glass pattern", "Door with a paper pattern",
        "Door with a golden pattern", "Door with a silver pattern", "Door with a bronze pattern",
        "Door with an iron pattern", "Door with a copper pattern", "Door with a lead pattern"
    ]

    for i in range(len(rooms_name)):
        all_rooms.append(Rooms(rooms_name[i]))

    for i in range(len(doors_name)):
        all_doors.append(Doors(doors_name[i], all_rooms[i % len(all_rooms)]))

    for room in all_rooms:
        count_door = random.randint(2, 4)
        available_doors = all_doors.copy()
        random.shuffle(available_doors)

        for _ in range(count_door):
            door = available_doors.pop()
            room.add_door(door)

    return all_rooms, all_doors


rooms, doors = create_labyrinth()
player = Player('Vlad', rooms[0])
game = True

while game:
    player.look_around()
    door_number = int(input("Enter the door number you want to enter: "))
    player.enter_a_room(door_number)

    if player.location.name == 'Exit':
        print("Congratulations! You found the room with treasures and won the game!")
        game = False
