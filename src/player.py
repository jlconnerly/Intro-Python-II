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

class Item():
    def __init__(self, weight, hp, name, catagory):
        self.weight = weight
        self.hp = hp
        self.name = name
        self.catagory = catagory
    
uga = Player("Orc", "Heavy", "Uga", [])

uga.move("north")
uga.pick_up_item(Item(5, 12, "Common Shield", "armor"))

uga.inventory_check()
