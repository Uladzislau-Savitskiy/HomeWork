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
