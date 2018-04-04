# import               import random
# class definitions    class item(object):
# instantiate          hdm = Room(....)
# -items
# -Characters
# -Rooms
# Controller


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


class Wearable(Item):
    def __init__(self, name, description, value, weight):
        super(Wearable, self).__init__(name, description, value, weight)

    def put_on(self):
        print("You are now wearing the item")


class Consumable(Item):
    def __init__(self, name, description, value, weight,):
        super(Consumable, self).__init__(name, description, value, weight)

    def consume_consumable(self):
        print("That %d was helpful", self.name)


class Drinkable(Consumable):
    def __init__(self, name, description, value, weight):
        super(Drinkable, self).__init__(name, description, value, weight)


class Potions(Consumable):
    def __init__(self, name, description, value, weight):
        super(Potions, self).__init__(name, description, value, weight)


class CoatOfInvisibility(Wearable):
    def __init__(self, name, description, value, weight):
        super(CoatOfInvisibility, self).__init__(name, description, value, weight)
        self.invisible = False

    def put_on(self):
        super(CoatOfInvisibility, self).put_on()
        self.invisible = True


class Lens(Item):
    def __init__(self):
        super(Lens, self).__init__("Lens", "This lens looks worthless, but it will be of great use in this world",
                                   100, 1)


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


class Pen(Item):
    def __init__(self):
        super(Pen, self).__init__("Dip Pen", "Wood Dip pen", 5, 1)

    def pick_up_item(self):
        print("%d has been picked up", self.name)


class Rope(Item):
    def __init__(self):
        super(Rope, self).__init__("Rope", "White long rope", 10, 10)


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


class Character(object):
    def __init__(self, name, description, health, death, damage):
        self.name = name
        self.description = description
        self.health = health
        self.death = death
        self.damage = damage

    def eat(self):
        if self.eat:
            print("That was good!")
            self.health += 5

    def pick_up_items(self):
        if self.pick_up_items:
            print("Item has been picked up")

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.damage))
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.death = True
            print("You died")


class Room(object):
    def __init__(self, name, up, north, south, east, west, southeast, southwest, northeast, northwest, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.southwest = southwest
        self.northeast = northeast
        self.northwest = northwest
        self.description = description
        self.up = up

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


sword = Weapon("Sword", "Big shiny sword", 20, 9, 20)
knife = Weapon("knife", "small kitchen knife", 15, 3, 13)
Shovel = Weapon("Shovel", "dirty old shovel", 10, 8, 7)
Tomato_sauce = Weapon("Spray bottles with tomato sauce inside", "Cleaning spray bottles containig tomato sauce, this"
                      "could help you defeat the troll", 65, 5, 79)
Backpack = Wearable("Backpack", "Black backpack", 2, 2)
Armor = Wearable("Protective Armor", "Armor", 15, 30)
clothing = Wearable("Cloths", "T-shirt and some jeans", 1, 3)
Apple = Consumable("Apple", "Red normal size apple", 5, 2, )
Sandwich = Consumable("Sandwich", "Yummy! Ham sandwich", 5, 3)
Water_bottle = Drinkable("Water Bottle", "Individual water bottle", 5, 4)
Orange_Juice = Drinkable("Orange Juice", "Orange juice can", 5, 4)
Health_Potion = Consumable("Health Potion", "Tiny bottle, the description reads 'Health Potion'", 20, 2)
Change_characters_potion = Consumable("Change Characters", "The label reads: 'If u want to change characters drink this"
                                      "potion", 20, 2)
coat = CoatOfInvisibility("Coat", "Brown Coat", 10, 5)
Lens = Lens()
book = Book()
Pen = Pen()
Rope = Rope()
FlyingShoes = FlyingShoes()
player = Character("Player", "You", 100, False, 20)
enemy = Character("Enemy", "It's a bad guy", 100, False, 10)

living = Room("Living Room", None, None, None, None, 'kitchen', None, None, None, None, 'There are three couches and a'
              ' TV.')

kitchen = Room("Kitchen", "Old Room", None, None, "Living", "Garden", None, None, None, None, "Big wooden table,"
               " kitchen has old rusty drawers with a sink. To the west there is a big clear door leading to the"
               "garden")

Garden = Room("Garden", None, None, None, "Antique Art Room", None, None, None, None, None, "'Green grass all over,"
              " colorful flower are starting to bloom.")

Art_Room = Room("Art Room", None, None, None, "Garden", None, None, None, None, None, "To the east there is a brick"
                                                                                      " wall, which has no exist. In "
                                                                                      "the middle of the room there is"
                                                                                      " an art stand with some dry"
                                                                                      " paints by the side")

Southeast_of_Garden = Room("Front of House", 'Second_Floor', "Inside_House", "Dangerous Forest", None, None, None,
                           None, None, None, "Black two story house, with two white windows in front.")

Inside_House = Room("Inside House", None, "Inside Pool", None, "Living Room", None, None, None, "Bedroom", "Kitchen",
                    "You are inside a two story house; standing at the beginning of a corridor. Around you there are"
                    "different rooms and doors leading to the yet unknown. To the side a bit to the east there is a"
                    "fancy staircase leading to the second floor.")

Swimming_pool = Room("Inside Pool", None, None, None, "Big Bathroom", None, "Bedroom", None, None, None, "Big"
                     "rectangular pool with crystal water, the bottom can not be seen because of its deepness, inside"
                     " the pool there are infinite steps leading down to the bottom of the pool (if there is a bottom.")

Big_Bathroom = Room("Big Bathroom", None, None, "Bedroom", None, None, "Living Room", "Brick Wall", None, None, "You"
                    "are now east of the pool inside a gigantic bathroom, this bathroom is very antique, and it is also"
                    "very unique.")

Bedroom = Room("Bedroom", None, "Inside Pool", "Front Door", None, "Brick Wall", "Living Room", None, None, None,
               "Inside the bedroom there is a bed with two small drawers by the sides. In the south wall of the room"
               "there is a build in closet. At the northeast corner of the room there is a small bathroom. Inside the"
               " bathroom there is an open window leading to the outside east of the house.")

Second_Floor = Room("Up stairs", None, "Special Room", None, "Library", "Waiting Room", None, None, "Single Room",
                    "Waiting Room", "You are up stairs in the second floor, This floor looks very similar to the"
                    "first floor just with different room that you are about to discover (Only if you are willing to).")

Library = Room("Library", None, "Hallway", None, None, "Staircase", None, None, "(FIRST) Single bedroom",
               "Second Floor Bedroom", "The Library room is filled with row and rows of books of all kinds. Books that"
               "you have never imagined; they are a bit dusty as if no one has touched them in years.")

Special_Room = Room("Second Floor Bedroom", None, None, "Staircase", None, "Waiting Room", "Library",
                    "Waiting Room", "Hallway", None, "You are standing in a very typical room,"
                    "there is a bed, some lamps by the sides, books on the floor. To the north wall there is an open"
                    "window. But then you notice one of the weirdest things; part of the floor is glass allowing you to"
                    " see down and take a look at the pool. You are not sure if the glass is very stable.")

Gym = Room("Gym", None, "Back Gym wall", "Office", "Second Floor Bedroom", "Waiting Room", "Library", "Waiting Room",
           None, "Gym", "The gym is weird shaped. It is found at the northwest corner of the house. Instead of being a"
                 " regular rectangular shape building it is half circle.")

Office = Room("Office", None, "Gym", None, "Staircase", "Waiting Room", None, None, "Library", "Waiting Room", "You are"
              "in a room that looks like an office. This room has a desk, an old computer, and some bookshelf.")

Waiting_Room = Room("Waiting Room", None, "Gym", "Office", "Library", None, "Office", None, "Second Floor Bedroom",
                    None, "You find yourself in a small lobby next to an office. The Waiting room or lobby")


current_node = Southeast_of_Garden
directions = ['north', 'south', 'east', 'west', 'southeast', 'southwest', 'northeast', 'northwest']
short_directions = ['n', 's', 'e', 'w', 'se', 'sw', 'ne', 'nw']

while True:
    # Room Information
    print(current_node.name)   # change
    print(current_node.description)   # change

    # Asks for input
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)

    # Changes an "n" to "north"
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    # Moves rooms
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
