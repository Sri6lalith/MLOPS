import sys

class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def apply_effect(self, player):
        self.effect(player)

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def move(self, direction, current_room):
        if direction in current_room.exits:
            return current_room.exits[direction]
        else:
            print("You can't go that way.")
            return current_room

    def interact(self, obj):
        print(f"You see {obj.description}")

    def attack(self, enemy):
        print(f"You attack {enemy.name}")
        enemy.health -= 10
        if enemy.health <= 0:
            print(f"You have defeated {enemy.name}!")
        else:
            print(f"{enemy.name} has {enemy.health} health left.")

    def pick_up(self, item):
        self.inventory.append(item)
        print(f"You have picked up {item.name}")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                item.apply_effect(self)
                self.inventory.remove(item)
                return
        print("You don't have that item.")

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def get_description(self):
        return self.description

    def get_exits(self):
        return self.exits

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)


# Effect functions
def heal(player):
    player.health += 20
    print(f"{player.name} has been healed. Health is now {player.health}.")

def increase_strength(player):
    print(f"{player.name} feels stronger!")

# Setup game
def setup_game():
    # Rooms
    room1 = Room("Room 1", "A small, dimly lit room.")
    room2 = Room("Room 2", "A large, brightly lit room.")
    room3 = Room("Room 3", "A dark, scary room.")

    room1.add_exit("north", room2)
    room2.add_exit("south", room1)
    room2.add_exit("east", room3)
    room3.add_exit("west", room2)

    # Items
    healing_potion = Item("Healing Potion", "A potion that heals you.", heal)
    strength_potion = Item("Strength Potion", "A potion that makes you stronger.", increase_strength)

    room1.add_item(healing_potion)
    room2.add_item(strength_potion)

    # Player
    player = Player("Hero")

    return player, room1

# Game loop
def game_loop():
    player, current_room = setup_game()

    while True:
        print(f"\n{current_room.get_description()}")
        command = input("> ").strip().lower()

        if command in ["north", "south", "east", "west"]:
            current_room = player.move(command, current_room)
        elif command == "look":
            print(f"You see: {[item.name for item in current_room.items]}")
        elif command.startswith("pick up "):
            item_name = command[len("pick up "):]
            item = next((item for item in current_room.items if item.name.lower() == item_name), None)
            if item:
                player.pick_up(item)
                current_room.items.remove(item)
            else:
                print("There's no such item here.")
        elif command.startswith("use "):
            item_name = command[len("use "):]
            player.use_item(item_name)
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    game_loop()
