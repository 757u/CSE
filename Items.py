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


Apple = Consumable("Apple", "Red normal size apple", 5, 2, )
Sandwich = Consumable("Sandwich", "Yummyyy! Ham sandwich", 5, 3)


class Drinkable(Consumable):
    def __init__(self, name, description, value, weight):
        super(Drinkable, self).__init__(name, description, value, weight)


Water_bottle = Drinkable("Water Bottle", "Individual water bottle", 5, 4)
Orange_Juice = Drinkable("Orange Juice", "Orange juice can", 5, 4)


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


class Lens(Item):
    def __init__(self):
        super(Lens, self).__init__("Lens", "This lens looks worthless, but it will be of great use in this world",
                                   100, 1)


Lens = Lens()


class Key(Item):
    def __init__(self):
        super(Key, self).__init__("Key", "Very small gold key", 80, 1)

    def pick_up_key(self):
        print("%d is in your hand", self.name)

    def put_key_in_backpack(self):
        print("%d is in the backpack", self.name)


class Chest(Item):
    def __init__(self):
        super(Chest, self).__init__("Chest", "Old big dirty chest", 30, 70)

    def open_chest(self):
        print("%d has open", self.name)

    def take_item(self):
        print("item is out of the chest")


class Book(Item):
    def __init__(self):
        super(Book, self).__init__("Magical Book", "This book looks very old, on the top of it there is a note. "
                                                   "The note reads: 'Warning don't"
                                                   "read this book, if you do you will be in danger.", 100, 10)

    def open_book(self):
        print("%d is now open", self.name)

    def read_book(self):
        print("The %d reads:...", self.name)


book = Book()


class Pen(Item):
    def __init__(self):
        super(Pen, self).__init__("Dip Pen", "Wood Dip pen", 5, 1)

    def pick_up_item(self):
        print("%d has been picked up", self.name)


Pen = Pen()


class Rope(Item):
    def __init__(self):
        super(Rope, self).__init__("Rope", "White long rope", 10, 10)


Rope = Rope()


class Glasses(Item):
    def __init__(self):
        super(Glasses, self).__init__("Glasses", "clear black glasses", 2, 2)

    def see_through_glasses(self):
        print("%d are on your face", self.name)


class FlyingShoes(Wearable):
    def __init__(self):
        super(FlyingShoes, self).__init__("Flying shoes", "Black sneakers with small white wings", 15, 9)
        self.flying = False

    def put_on(self):
        super(FlyingShoes, self).put_on()
        self.flying = True

print(Rope)