class Item(object):
    def __init__(self, name, description, value, weight):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight


class Weapon(Item):
    def __init__(self, name, description, value, weight, damage):
        super(Weapon, self).__init__(name, description, value, weight)
        self.damage = damage

    def attack(self):
        print("Attacks for %d of damage", self.damage)

    def pick_up_item(self):
        print("%s is on your hand" % self.name)

    def drop_item(self):
        print("%d has been dropped", self.name)


sword = Weapon("Sword", "Big shiny sword", 20, 9, 20)
knife = Weapon("knife", "small kitchen knife", 15, 3, 13)
Shovel = Weapon("Shovel", "dirty old shovel", 10, 8, 7)
Tomato_sauce = Weapon("Spray bottles with tomato sauce inside", "Cleaning spray bottles containig tomato sauce, this"
                      "could help you defeat the troll", 65, 5, 79)


class Wearable(Item):
    def __init__(self, name, description, value, weight):
        super(Wearable, self).__init__(name, description, value, weight)

    def put_on(self):
        print("You are now wearing the item")


Backpack = Wearable("Backpack", "Black backpack", 2, 2)
Armor = Wearable("Protective Armor", "Armor", 15, 30)
clothing = Wearable("Cloths", "T-shirt and some jeans", 1, 3)


class Consumable(Item):
    def __init__(self, name, description, value, weight,):
        super(Consumable, self).__init__(name, description, value, weight)

    def consume_consumable(self):
        print("That %d was helpful", self.name)


Food = Consumable("Apple", "Red normal size apple", 5, 2, )
Water_bottle = Consumable("Water Bottle", "Individual water bottle", 5, 4, )


class Potions(Consumable):
    def __init__(self, name, description, value, weight):
        super(Potions, self).__init__(name, description, value, weight)


Health_Potion = Consumable("Health Potion", "Tiny bottle, the description reads 'Health Potion'", 20, 2)
Change_characters_potion = Consumable("Change Characters", "The label reads: 'If u want to change characters drink this"
                                      "potion", 20, 2)


class CoatOfInvisibility(Wearable):
    def __init__(self, name, description, value, weight):
        super(CoatOfInvisibility, self).__init__(name, description, value, weight)
        self.invisible = False

    def put_on(self):
        super(CoatOfInvisibility, self).put_on()
        self.invisible = True


coat = CoatOfInvisibility("Coat", "Brown Coat", 10, 5)


Book = Item("Magical Book", "This book looks very old, on the top of it there is a note. The note reads: 'Warning don't"
                            "read this book, if you do you will be in danger.", 100, 10)
Lens = Item("Lens", "This lens looks worthless, but it will be of great use in this world", 100, 1)
Rope = Item("Rope", "White long rope", 10, 10)
