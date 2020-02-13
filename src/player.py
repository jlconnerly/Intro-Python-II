# Write a class to hold player information, e.g. what room they are in currently.

class Player():
    inventory = []
    def __init__(self, race, armor, name, inventory):
        self.race = race
        self.armor = armor
        self.name = name
        self.inventory = inventory
    def move(self, movement):
        print(f"{self.name} moves {movement}.")
    def inventory_check(self):
        inv = []
        for i in self.inventory:
            inv.append(i.name)
        print(f"{inv}")
    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item.name}")
    def drop_item(self, item_name):
        for i in self.inventory:
            if item_name == i.name:
                self.inventory.remove(i)
        print(f"{self.name} dropped {i.name}")

class Item():
    def __init__(self, weight, hp, name, catagory):
        self.weight = weight
        self.hp = hp
        self.name = name
        self.catagory = catagory

player_choice = input("What do you want to do? (type 'move list' to see list. Otherwise enter move)")

if player_choice == "move list":
    print("Press 'N' to move North\nPress 'S' to move South\nYou get the picture...\nType 'open inv' to view inventory\nType 'drop [item]' to drop an item\nType pickup [item] to pick up item\n\n")
player_choice = input("What do you want to do? (type 'move list' to see list. Otherwise enter move)")
uga = Player("Orc", "Heavy", "Uga", [])

uga.move("north")
uga.pick_up_item(Item(5, 12, "Common Shield", "armor"))
uga.pick_up_item(Item(2, 0, "Lesser Soul Gem", "Magic"))
uga.pick_up_item(Item(1, 0, "Tomato", "Food"))

uga.inventory_check()
uga.drop_item("Tomato")
uga.inventory_check()