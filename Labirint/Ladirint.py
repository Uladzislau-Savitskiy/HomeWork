import random


class Object:

    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        return self.name


class CreationProcess:

    list_doors: list = []
    list_rooms: list = []
    doors_with_rooms: dict = {}
    we_in_this_room_now = None

    @classmethod
    def get_name_room(cls, door):
        return cls.doors_with_rooms.get(door)

    @classmethod
    def create_room(cls):
        room_names: list = [
            "Загадочная пещера",
            "Космическая станция",
            "Подводный грот",
            "Замок проклятий",
            "Волшебный сад",
            "Лаборатория времени",
            "Пиратская бухта",
            "Забытая библиотека",
            "Драконье логово",
            "Шпионская комната",
            "Сокровищница",
            "Таинственная лощина",
            "Магическая кузница",
            "Арктическая пещера",
            "Логово волков",
            "Подземный лабиринт",
            "Выход",
            "Заброшенный особняк",
            "Звездный корабль",
            "Джунглевая чаща"
        ]
        for name in room_names:
            obj = Object(name)
            cls.list_rooms.append(obj)
        random.shuffle(cls.list_rooms)

    @classmethod
    def create_door(cls):
        for i in range(1, 21):
            i = Object(f"Дверь {i}")
            cls.list_doors.append(i)

    @classmethod
    def connecting_the_doors_to_the_rooms(cls):
        cls.doors_with_rooms: dict = dict(zip(cls.list_doors, cls.list_rooms))

    @classmethod
    def start_room(cls):
        not_the_start_room = "Выход"
        cls.we_in_this_room_now = random.choice(cls.list_rooms)
        while cls.we_in_this_room_now == not_the_start_room:
            cls.we_in_this_room_now = random.choice(cls.list_rooms)
        return cls.we_in_this_room_now

    @classmethod
    def the_doors_that_are_in_the_room(cls):
        if cls.we_in_this_room_now == 'Выход':
            return print("Вы вышли из лабиринта")
        counter_doors = random.randint(2, 5)
        random_doors = (random.sample(list(cls.doors_with_rooms.keys()), counter_doors))
        random_doors = [str(door) for door in random_doors]
        return random_doors


creation_process = CreationProcess()
creation_process.create_room()
creation_process.create_door()
creation_process.connecting_the_doors_to_the_rooms()
start_room = creation_process.start_room()
print(f"""
Добро пожаловать в лабиринт.
Вы находитесь в {start_room}.
    """)
while True:
    doors_in_room = creation_process.the_doors_that_are_in_the_room()
    for i in doors_in_room:
        print(i)
    user_selection = input("Выберите дверь: ")
    if user_selection not in doors_in_room:
        raise ValueError("Недопустимый выбор!")
    creation_process.we_in_this_room_now = creation_process.get_name_room(user_selection)
    print(f"Вы находитесь в {creation_process.we_in_this_room_now}")
