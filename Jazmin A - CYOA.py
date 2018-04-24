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

    def pick_up_item(self):
        print(" You have now picked up a %s " % self.name)

    def drop_item(self):
        print("%d has been dropped", self.name)


class Weapon(Item):
    def __init__(self, name, description, value, weight, damage):
        super(Weapon, self).__init__(name, description, value, weight)
        self.damage = damage

    def attack(self):
        print("Attacks for %d of damage", self.damage)


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
    def __init__(self, name, description, value, weight):
        super(Lens, self).__init__(name, description, value, weight)


class Key(Item):
    def __init__(self, name, description, value, weight):
        super(Key, self).__init__(name, description, value, weight)

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
        print("item is out of the %s" % self.name)


class Book(Item):
    def __init__(self, name, description, value, weight):
        super(Book, self).__init__(name, description, value, weight)

    def open_book(self):
        print("%s is now open" % self.name)

    def read_book(self):
        print("The %s reads:..." % self.name)


class Pen(Item):
    def __init__(self, name, description, value, weight):
        super(Pen, self).__init__(name, description, value, weight)

    def pick_up_item(self):
        print("%d has been picked up", self.name)


class Rope(Item):
    def __init__(self, name, description, value, weight):
        super(Rope, self).__init__(name, description, value, weight)


class Glasses(Item):
    def __init__(self):
        super(Glasses, self).__init__("Glasses", "clear black glasses", 2, 2)

    def see_through_glasses(self):
        print("%s are on your face" % self.name)


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
        self.inventory = []

    def eat(self):
        if self.eat:
            print("That was good!")
            self.health += 5

    def pick_up(self, item):
        self.inventory.append(item)
        item.pick_up_item()


    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.damage))
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.death = True
            print("You died")


class Chest(Item):
    def __init__(self):
        super(Chest, self).__init__("Chest", "Old big dirty chest", 30, 70,)

    def open_chest(self):
        print("%d has open", self.name)

    def take_item(self):
        print("item is out of the %s" % self.name)


class Room(object):
    def __init__(self, name, up, north, south, east, west, southeast, southwest, northeast, northwest, description,
                 items=None):

        self.name = name
        self.up = up
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.southwest = southwest
        self.northeast = northeast
        self.northwest = northwest
        self.description = description
        self.inventory = items

    def move(self, direction):
            global current_node
            current_node = globals()[getattr(self, direction)]


sword = Weapon("Sword", "Big shiny sword", 20, 9, 20)
knife = Weapon("knife", "small kitchen knife", 15, 3, 13)
Shovel = Weapon("Shovel", "dirty old shovel", 10, 8, 7)
Tomato_sauce = Weapon("Spray bottles with tomato sauce inside", "Cleaning spray bottles containing tomato sauce, this"
                      "could help you defeat the troll", 65, 5, 79)
Backpack = Wearable("Backpack", "Black backpack", 2, 2)
Armor = Wearable("Protective Armor", "Armor", 15, 30)
clothing = Wearable("Cloths", "T-shirt and some jeans", 1, 3)
Apple = Consumable("Apple", "Red normal size apple", 5, 2)
Sandwich = Consumable("Sandwich", "Yummy! Ham sandwich", 5, 3)
Water_bottle = Drinkable("Water Bottle", "Individual water bottle", 5, 4)
Orange_Juice = Drinkable("Orange Juice", "Orange juice can", 5, 4)
Health_Potion = Consumable("Health Potion", "Tiny bottle, the description reads 'Health Potion'", 20, 2)
Change_characters_potion = Consumable("Change Characters", "The label reads: 'If u want to change characters drink this"
                                      "potion", 20, 2)
coat = CoatOfInvisibility("Coat", "Brown Coat", 10, 5)
Lens = Lens("Lens", "This lens looks worthless, but it will be of great use in this adventure", 100, 1)
book = Book("Magical Book", "This book looks very old, on the top of it there is a note. "
            "The note reads: 'Warning don't read this book, if you do you will be in danger.", 100, 10)
Pen = Pen("Dip Pen", "Wood Dip pen", 5, 1)
Rope = Rope("Rope", "White long rope", 10, 10)
key = Key("Key", "Very small gold key", 80, 1)
FlyingShoes = FlyingShoes()
player = Character("Player", "You", 100, False, 20)
enemy = Character("Enemy", "It's a bad guy", 100, False, 10)


living = Room("Living Room", None, "Bedroom", None, "living", "Staircase", "kitchen", None, None, None, "The walls of "
              "the room are covered by yellow wall paper. In the east wall there is a big white window, through the "
              "window you can observe the green grass. In  the room there are four leather couches. In the south wall "
              "there is a gigantic television", [Water_bottle])

kitchen = Room("Kitchen", "Old Room", None, None, "Living", "Garden", None, None, None, None, " In the middle of the"
               " kitchen there is a big wooden table. At the east of the kitchen there are many old rusty drawer; "
               "surprisingly most of the drawers are full with can tomato sauce, underneath the drawers there is"
               " a silver sink. To the west there is a  big clear door leading to the garden", [knife, Tomato_sauce])

West_of_Garden = Room("Garden", None, "West_of_Garden", "West_of_Garden", "Antique Art Room", "Dangerous_Forest",
                      "South_of_Garden", "Road", "North_Garden", "Forest", " You are west of the House, there is green"
                      " grass all over, colorful flowers are starting to bloom.")

# Road = Room("Road", None, "")
# Dangerous_Forest = Room("Dangerous Forest", None, "")
# Old_Room = Room("Old Room", None )

South_of_Garden = Room("Front of House", 'Second_Floor', "Inside_House", "Dangerous Forest", "Living Room", None,
                       None, None, None, None, "Black two story house, with two white windows in front.")

Art_Room = Room("Art Room", None, None, None, "Garden", None, None, None, None, None,
                "To the east there is a brick wall, which has no exist. In the middle of the room there is"
                " an art stand with some dry paints by the side", [sword])

Inside_House = Room("Inside House", None, "Swimming_pool", "South_of_Garden", "living", "Kitchen", "South_of_Garden",
                    "South_of_Garden", "Bedroom", "Art_Room", "You are inside a two story house; standing at the "
                    "beginning of a corridor, to the side of you there is a small table. In the table there is"
                    " something that looks like a lens. Around you there are different rooms and doors leading to the"
                    " yet unknown. To the side a bit to the east there is a fancy staircase leading to the second"
                    " floor.",
                    [Lens])

Swimming_pool = Room("Indoor Pool", None, None, "Staircase", "Big Bathroom", None, "Bedroom", None, None, None, "Big"
                     "rectangular pool with crystal water, the bottom can not be seen because of its deepness, inside"
                     " the pool there are infinite steps leading down to the bottom of the pool (if there is a bottom.")

Big_Bathroom = Room("Big Bathroom", None, None, "Bedroom", None, None, "living", "Brick Wall", None, None, "You"
                    "are now east of the pool inside a gigantic bathroom, this bathroom is very antique, and it is also"
                    "very unique.")

Bedroom = Room("Bedroom", None, "Swimming_pool", "Front Door", None, "Brick Wall", "Living Room", None, None, None,
               "Inside the bedroom there is a bed with two small drawers by the sides. In the south wall of the room"
               "there is a build in closet. At the northeast corner of the room there is a small bathroom. Inside the"
               " bathroom there is an open window leading to the outside east of the house.", [clothing])

Second_Floor = Room("Up stairs", None, "Special_Room", None, "Library", "Waiting_Room", None, None,
                    "Single_Room's Hallway", "Waiting Room", "You are up stairs in the second floor, This floor looks "
                    "very similar to the first floor just with different rooms that you are about to discover"
                    " (Only if you are willing to).")
Staircase_sec = Room("Staircase", None, "Special_Room", None, "Library", "Office", None, None, "Bedroom",
                     "Waiting_Room", "You are back at where the fancy staircase start, you are still in the second"
                     " floor.")

Staircase_fir = Room("Staircase", "Second_Floor", "Inside_Pool", "Southeast_of_Garden", "Living", "Kitchen", None, None,
                     "Bedroom", "Art_Room", "You are in between the Front Door House and the fancy staircase leading up"
                     " to the second floor. ")


Library = Room("Library", None, "Hallway", None, None, "Staircase", None, None, "(FIRST) Single bedroom",
               "Second Floor Bedroom", "The Library room is filled with rows and rows of books of all kinds. Books that"
               " you have never imagined; they are a bit dusty as if no one has touched them in years.")

Hallway = Room("Hallway", None, None, "Hallway", "FIRST_Single_bedroom", "Special_Room", "Library", "Waiting_Room",
               "SECOND_Single_bedroom", None, "You are in a dark hallway. The only light you have is coming from some"
               " old flickering lamps attached to the wall. In the wall there are some painting of old"
               " and young people that you have never seen before, to the east there are two doors and to the west"
               " there is only one.")

FIRST_Single_bedroom = Room("FIRST_Single_bedroom", None, "SECOND_Single_bedroom", "Bedroom", None, "Special_Room",
                            "Library", "Waiting_Room", None, "SECOND_Single_bedroom", "You are in a tiny room, it looks"
                            " like you can only fit a small bed. The walls are pale green and they have some "
                            "writing on them.1", [Backpack])

SECOND_Single_bedroom = Room("SECOND_Single_bedroom", None, None, "FIRST_Single_bedroom", None, "Special_Room",
                             "Bedroom", "Waiting_Room", None, None, "You are in a tiny room, it looks"
                             " like you can only fit a small bed. The walls are pale green and they have some "
                             "writing on them.2")

Special_Room = Room("Second Floor's Main Bedroom", None, None, "Second_Floor", "Hallway", "Waiting Room", "Library",
                    "Waiting Room", "Hallway", None, "You are standing in a very typical room, "
                    "there is a bed, some lamps by the sides, books on the floor. To the north wall there is an open"
                    "window. But then you notice one of the weirdest things; part of the floor is glass allowing you to"
                    " see down and take a look at the pool. You are not sure if the glass is very stable.", [Chest])

Gym = Room("Gym", None, "Back Gym wall", "Waiting_Room", "Special_Room", "Waiting Room", "Library",
           "Waiting Room", None, "Gym", "The gym is weird shaped. It is found at the northwest corner of the house. "
           "Instead of being a regular rectangular shape building it is half circle.", [Armor])

Office = Room("Office", None, "Waiting_Room", None, "Staircase", "Waiting Room", None, None, "Library",
              "Waiting_Room", "You are in a room that looks like an office. This room has a desk, an old computer, "
              "and some bookshelf.", [Pen])

Waiting_Room = Room("Waiting Room", None, "Gym", "Office", "Library", None, "Office", None, "Second Floor Bedroom",
                    None, "You find yourself in a small lobby next to an office. The Waiting room or lobby", [Sandwich])


def take(item_requested):
    print("You attempt to pick up a %s" % item_requested)
    found = False
    for item in current_node.inventory:
        if item.name.lower() == item_requested.lower():
            # print("taken")
            found = True
            Room.inventory.remove(item_requested)
            Character.iventory.append(item_requested)
            player.pick_up(item)

    if not found:
        print("I don't see that here")


current_node = South_of_Garden
directions = ['north', 'south', 'east', 'west', 'southeast', 'southwest', 'northeast', 'northwest', 'up']
short_directions = ['n', 's', 'e', 'w', 'se', 'sw', 'ne', 'nw', 'u']

while True:
    # Room Information
    print(current_node.name)
    print(current_node.description)

    if current_node.inventory is not None:
        print()
        print("The following item(s) are in the room: ")
        for item in current_node.inventory:
            print(item.name)

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

    elif "take" in command:
        item_requested = command[5:]
        take(item_requested)
    elif "pick up" in command:
        item_requested = command[8:]
        take(item_requested)
    else:
        print("Command not recognized")


# .remove item