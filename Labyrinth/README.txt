Maze
Description:
    The task is to create a labyrinth game space. The idea is to create a scalable program that can be further developed and
    fine-tuned. The player will move through the maze, going from room to room until he finds his way out. The labyrinth
    will be designed manually, either by scheme or randomly, depending on the chosen complexity of implementation.

Acceptance criteria:
    Entities:
        Rooms
        Doors
        Player
        The rooms have doors.
        Doors lead to the rooms.
        The player chooses which door to enter and enters the next room.
        You can choose which room will be the winning room.

Basic option:
    Rooms:
        Have doors
        The player can look around
        Attributes:
            Name
            Doors
        Methods:
            Add door
            View all doors in the room
    Doors:
        Lead to other rooms
        Attributes:
            Room 1
            Room 2
        Methods:
            Get the room where the door leads
    Player:
        Can choose which door to go through
        Can look around
        Attributes:
            Name
            The location where the player is located
        Methods:
            Look around
            Enter a room
Creating a Labyrinth:
    The labyrinth is created manually by creating rooms as objects and connecting them with doors.
    The player is placed in the first room that is created.
    After the labyrinth is created, a loop is started where the player is prompted via 'input' to choose which room to go to.

Difficult Option:
After implementing the Basic option, the following additions are made:
    a. New entity: Key
        If the player has the key in their inventory, they can open the door.
        When the door is opened, the key breaks.

    b. Player:
        Has a safety margin.
        Strength points are equal to the number of rooms.
        The game ends when the player's strength points run out.
        At the beginning of the game, the player is placed in a random point of the labyrinth.
        Has an inventory.

    c. Room:
        Takes away 1 point from the player's strength.
        Can contain different objects such as a key.
        There is a chance that a key will be present in the room.
        When the player looks around the room, they can see the key (if it is present in the room).

    d. Doors:
        Can be closed.
        Can be opened with a key.
        Can lead to a dead end.

Creating a Labyrinth:
The labyrinth is created based on a pre-defined list.
Impossible Option:
After implementing the Difficult option and the 'Dice' homework, the following additions are made:
    a. New entity: Dice
        Takes inspiration from the previous homework.
        The number of faces can be chosen when creating the game (e.g., a cube with values from 1 to 20).
        The dice is rolled during checks.

    b. Check: (if the die value is from 1 to 20)
        1-2: Critical failure.
        3-10: Failure.
        11-19: Success.
        20: Critical success.

    c. New entity: Chest
        Can sometimes be found in rooms upon inspection.
        Sometimes requires a key to open, and sometimes it doesn't.
        Can be an enemy and attack the player with 1 to 5 dice points (rolls the dice).
        Can restore 1 to 5 dice points (rolls the dice).

    d. New entity: Enemy
        Moves through the labyrinth just like the player but is controlled by the computer.
        When encountering the player:
            - Kills the player (critical failure).
            - Deals 5-10 damage (modified by the dice roll).
            - If the player avoids the battle, the opponent moves to a random point in the maze, within a maximum distance of 5 rooms from the player (critical success).
            - The opponent cannot be in the winning room.

Extras:
The player can attempt to break through a closed door:
Critical failure: The door becomes a dead end.
Failure: The door cannot be hacked anymore, but it can still be opened with a key.
Success: The door
