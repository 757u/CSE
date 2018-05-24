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
        print()


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

    def drink(self):
        print(" That %s was good!" % self.name)
    

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

    def see_through_lens(self):
        print()


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

    def open_chest(self, character):
        print("%s has opened by %s" % (self.name, character.name))

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
    def __init__(self, name, description, health, death, damage, location=None):
        self.name = name
        self.description = description
        self.health = health
        self.death = death
        self.damage = damage
        self.inventory = []
        self.lens = False
        self.location = location
        
    def use_lens(self):
        if Lens in self.inventory:
            self.lens = True
            print("You look through the lens.")
        else:
            print("You don't have a lens.")
            
    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]
        if self.lens:
            print("You put the lens away.")
            self.lens = False

    def eat(self):
        if self.eat:
            print("That was good!")

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
            print("You have killed %s", self.name)


player = Character("Player", "You", 100, False, 20)
goblin = Character("Goblin", "Bad ugly creature", 100, False, 10)
troll = Character("Troll", "", 100, False, 15)
type3 = Character("...", "", 100, False, 20)


class Room(object):
    def __init__(self, name, up, down, north, south, east, west, southeast, southwest, northeast, northwest,
                 description, characters, items=None):

        self.name = name
        self.up = up
        self.down = down
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
        self.characters = characters


sword = Weapon("Sword", "Big shiny sword", 20, 9, 20)
knife = Weapon("knife", "small kitchen knife", 15, 3, 13)
Shovel = Weapon("Shovel", "dirty old shovel", 10, 8, 7)
Tomato_sauce = Weapon("Tomato sauce", "Cleaning spray bottles containing tomato sauce. HINT: Goblins can be defeated"
                      " using the weirdest things."
                      "could help you defeat the troll", 65, 5, 79)
Backpack = Wearable("Backpack", "Black backpack", 2, 2)
Armor = Wearable("Protective Armor", "Armor", 15, 30)
clothing = Wearable("Cloths", "T-shirt and some jeans", 1, 3)
Apple = Consumable("Apple", "Red normal size apple", 5, 2)
Sandwich = Consumable("Sandwich", "Yummy! Ham sandwich", 5, 3)
Water_bottle = Drinkable("Water Bottle", "This is a normal 500ml water bottle. Remember that all types of consumables "
                                         "will give you health.", 5, 4)
Orange_Juice = Drinkable("Orange Juice", "Orange juice can", 5, 4)
Health_Potion = Consumable("Health Potion", "Tiny bottle, the description reads 'Health Potion'", 20, 2)
Change_characters_potion = Consumable("Change Characters", "The label reads: 'If u want to change characters drink this"
                                      "potion", 20, 2)
coat = CoatOfInvisibility("Coat", "Brown Coat", 10, 5)
Lens = Lens("Lens", "This lens looks worthless, but it will be of great use in this adventure. It is one of the most "
                    "powerful items you will find. This lens will help you not get killed, because it makes enemies "
                    "visible.", 100, 1)
book = Book("Magical Book", "This book looks very old, on the top of it there is a note. "
            "The note reads: 'Warning don't read this book, if you do you will be in danger.", 100, 10)
Pen = Pen("Dip Pen", "Wood Dip pen", 5, 1)
Rope = Rope("Rope", "White long rope", 10, 10)
key = Key("Key", "Very small gold key", 80, 1)
chest = Chest("Chest", "its a big chest", 3, 20)
FlyingShoes = FlyingShoes


living = Room("Living Room", None, None, "Bedroom", None, None, "Staircase_fir", None, None, None, None, "The walls"
              " of the room are covered by yellow wall paper. In the east wall there is a big white window, through the"
              " window you can observe the green grass. In  the room there are four leather couches. In the south wall "
              "there is a gigantic television", [Character("Goblin", "It's a bad guy", 100, False, 10),
                                                 Character("Goblin", "It's a bad guy", 100, False, 10),
                                                 Character("Goblin", "It's a bad guy", 100, False, 10),
                                                 Character("Goblin", "It's a bad guy", 100, False, 10)],
                                                 [Water_bottle])


kitchen = Room("Kitchen", None, None, None, None, "Staircase_fir", "West_of_Garden", None, None, None, None,
               " In the middle of the kitchen there is a big wooden table. At the east of the kitchen there are many"
               " old rusty drawer; surprisingly most of the drawers are full with can tomato sauce, underneath the"
               " drawers there is a silver sink. To the west there is a  big clear door leading to the garden", None,
               [knife, Tomato_sauce])

West_of_Garden = Room("West of garden", None, None, None, "West_of_Garden", "kitchen", "Antique Art Room",
                      "Dangerous_Forest", "South_of_Garden", "Road", "North_Garden", " You are now west of "
                      "the House, there is green grass all over the place.", None, [Character("troll", "", 100, False,
                                                                                    20)])

Road = Room("The Road", None, None, "West_of_Garden", "Dangerous Forest", "Front of House", "Dangerous Forest",
            "Dangerous Forest", "Road", "Back of house", "Dangerous Forest", "The Road is the only way to get out of"
            " the house into a safe place. If you decide to take this path you will never be able to return back "
            "into the house. If you are ready to end this game pleas type SOUTHWEST!!! . If you don't follow directions"
            "game will not end.", None, None)

Dangerous_Forest = Room("Dangerous Forest", None, None, None, None, None, None, None, None, None, None, "It is"
                        " preferable that you exist the forest", [Character("Troll", "Bad ugly creature", 100, False,
                                                                            10,)], None)

# Old_Room = Room("Old Room", None )

South_of_Garden = Room("Front of House", 'Second_Floor', None, "Inside_House", "Dangerous Forest", "Front of House",
                       "Road", "Dangerous Forest", "Dangerous Forest", None, None, "You look up and down the house "
                       "face. It is dilapidated with curls of paint peeling off and falling to the ground. Ivy"
                       "clings to the walls and most of it is withered away. As you step around, there is the soft "
                       "crunching of dead leaves turning the floor into a mosaic of yellows, oranges, and reds. Around"
                       "the house The Heavy Forest dominates.", [])

# North_of_Garden = Room("Back of House", "You are now at the back of the House, the most notifiable thing there is an"
# " apple tree. Remember any type of food or bevarage can give you health.")


Art_Room = Room("Art Room", None, None, None, None, "Garden", None, None, None, None, None,
                "To the east there is a brick wall, which has no exist. In the middle of the room there is"
                " an art stand with some dry paints by the side", [sword, key], None)

Inside_House = Room("Inside House", None, None, "Swimming_pool", "South_of_Garden", "living", "kitchen",
                    "South_of_Garden", "South_of_Garden", "Bedroom", "Art_Room", "You are inside a two story house; "
                    "standing at the beginning of a corridor. Around you there are different rooms and doors leading"
                    " to the yet unknown. To the side a bit to the east there is a fancy staircase leading to the "
                    "second floor. This House is fancy, but at the same time it is very old.", [],
                    [Lens])

Swimming_pool = Room("Indoor Pool", None, None, None, None, "Inside_House", "Big Bathroom", None, "Bedroom", None,
                     None, "Big rectangular pool with crystal water, the bottom can not be seen because of its "
                     "deepness, inside the pool there are infinite steps leading down to the bottom of the pool "
                     "(if there is a bottom.)", [Character("Goblins", "Bad ugly creature", 100, False, 10)], None)

Big_Bathroom = Room("Big Bathroom", None, None, None, "Bedroom", None, None, "living", "Brick Wall", None, None, "You"
                    "are now east of the pool inside a gigantic bathroom, this bathroom is very antique, and it is also"
                    "very unique.", None, None)

Bedroom = Room("Bedroom", None, None, "Swimming_pool", "Front Door", None, "Brick Wall", "Living Room", None, None,
               None, "Inside the bedroom there is a bed with two small drawers by the sides. In the south wall of the "
               "room there is a build in closet. At the northeast corner of the room there is a small bathroom. Inside"
               " the bathroom there is an open window leading to the outside east of the house.", [], [clothing])

Second_Floor = Room("Up stairs", None, "Staircase_fir", "Special_Room", None, "Library", "Waiting_Room", None, None,
                    "Single_Room's Hallway", "Waiting Room", "You are up stairs in the second floor, This floor looks "
                    "very similar to the first floor just with different rooms that you are about to discover"
                    " (Only if you are willing to).", None, None)

Staircase_sec = Room("Staircase", None, "Staircase_fir", None, "Special_Room", None, "Library", "Office", None,
                     "Bedroom", "Waiting_Room", "You are back at where the fancy staircase start, you are still in the"
                     " second floor.", None, None)

Staircase_fir = Room("Staircase", "Second_Floor", None, "Inside_Pool", "Southeast_of_Garden", "Living", "kitchen",
                     None, None, "Bedroom", "Art_Room", "You are in between the Front Door House and the fancy "
                     "staircase leading up to the second floor. ", None, None)


Library = Room("Library", None, None, "Hallway", None, None, "Staircase", None, None, "(FIRST) Single bedroom",
               "Second Floor Bedroom", "The Library room is filled with rows and rows of books of all kinds. Books that"
               " you have never imagined; they are a bit dusty as if no one has touched them in years.", [Character
               ("Goblin", "Bad creature", 100, False, 10)], None)

Hallway = Room("Hallway", None, None, None, "Hallway", "FIRST_Single_bedroom", "Special_Room", "Library",
               "Waiting_Room", "SECOND_Single_bedroom", None, "You are in a dark hallway. The only light you have is"
               " coming from some old flickering lamps attached to the wall. In the wall there are some painting of old"
               " and young people that you have never seen before, to the east there are two doors and to the west"
               " there is only one.", [troll], None)

FIRST_Single_bedroom = Room("FIRST_Single_bedroom", None, None, "SECOND_Single_bedroom", "Bedroom", None,
                            "Special_Room", "Library", "Waiting_Room", None, "SECOND_Single_bedroom", "You are in a"
                            " tiny room, it looks like you can only fit a small bed. The walls are pale green and they"
                            " have some writing on them.1", [Backpack])

SECOND_Single_bedroom = Room("SECOND_Single_bedroom", None, None, None, "FIRST_Single_bedroom", None, "Special_Room",
                             "Bedroom", "Waiting_Room", None, None, "You are in a tiny room, it looks"
                             " like you can only fit a small bed. The walls are pale green and they have some "
                             "writing on them.2", None, None)

Special_Room = Room("Second Floor's Main Bedroom", None, None, None, "Second_Floor", "Hallway", "Waiting Room",
                    "Library", "Waiting Room", "Hallway", None, "You are standing in a very typical room, "
                    "there is a bed, some lamps by the sides, books on the floor. To the north wall there is an open"
                    "window. But then you notice one of the weirdest things; part of the floor is glass allowing you to"
                    " see down and take a look at the pool. You are not sure if the glass is very stable.", None,
                    [Chest])

Gym = Room("Gym", None, "Back Gym wall", "Waiting_Room", "Special_Room", "Waiting Room", "Library",
           "Waiting Room", None, "Gym", "The gym is weird shaped. It is found at the northwest corner of the house. "
           "Instead of being a regular rectangular shape building it is half circle.", None, [Armor])

Office = Room("Office", None, "Waiting_Room", None, "Staircase", "Waiting Room", None, None, "Library",
              "Waiting_Room", "You are in a room that looks like an office. This room has a desk, an old computer, "
              "and some bookshelf.", None, [Pen])

Waiting_Room = Room("Waiting Room", None, "Gym", "Office", "Library", None, "Office", None, "Second Floor Bedroom",
                    None, "You find yourself in a small lobby next to an office.", None, [Sandwich])


def take(item_requested):
    found = False
    for item in player.location.inventory:
        if item.name.lower() == item_requested.lower():
            # print("taken")
            found = True
            player.location.inventory.remove(item)

            player.pick_up(item)

    if not found:
        print("I don't see that here")


player.location = South_of_Garden
directions = ['north', 'south', 'east', 'west', 'southeast', 'southwest', 'northeast', 'northwest', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'se', 'sw', 'ne', 'nw', 'u', 'd']


while True:
    # Room Information
    print("For help type: '?' or 'help'.")
    print()
    print(player.location.name)
    if player.location.characters is not None and len(player.location.characters) > 0:
        if player.lens is False:
            print("You sense a presence.")
        elif len(player.location.characters) == 1:
            print("You see a %s" % player.location.characters[0].name)
        else:
            print("You see %d goblins" % len(player.location.characters))
            print("___________________________________________________________________________________________________")

    print(player.location.description)

    if player.location.inventory is not None and len(player.location.inventory) > 0:
        print()
        print("The following item(s) are in the room: ")
        for item in player.location.inventory:
            print(item.name)
            print(item.description)

    if player.location == Road:
        print()
        if "SOUTHWEST" in input():
            print("Game Over!!!")
            quit(0)

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
            player.move(command)
        except KeyError:
            print("You cannot go this way")

    elif "take" in command:
        item_requested = command[5:]
        take(item_requested)
        for item in player.inventory:  # Go through every item
            if item.name.lower() == item_requested.lower():  # and see if it matches the name of the item u are looking
                if isinstance(item, Drinkable):
                    command2 = input("Would you like to drink it?")
                    if command2.lower() in ['y', 'yes']:
                        item.drink()
                        print("You have drunk the beverage")
                        print("You're health is:")
                        player.health += 5
                        print(player.health)
                        print("______________________________________________________________________________________")
                        print()

                elif isinstance(item, Consumable):  # If that item object is a consumable
                    command2 = input("Would you like to eat it?")
                    if command2.lower() in ['y', 'yes']:
                        player.eat()  # Eat it.
                        print("You have eaten ")
                        player.health += 5
                        print(player.health)

    elif "pick up" in command:
        item_requested = command[8:]
        take(item_requested)
        for item in player.inventory:  # Go through every item
            if item.name.lower() == item_requested.lower():  # and see if it matches the name of the item u are looking
                if isinstance(item, Drinkable):
                    command2 = input("Would you like to drink it?")
                    if command2.lower() in ['y', 'yes']:
                        item.drink()
                        print("You have drunk the beverage")
                        print("You're health is:")
                        player.health += 5
                        print(player.health)
                        print("______________________________________________________________________________________")
                        print()

                elif isinstance(item, Consumable):  # If that item object is a consumable
                    command2 = input("Would you like to eat it?")
                    if command2.lower() in ['y', 'yes']:
                        player.eat()  # Eat it.
                        print("You have eaten ")
                        player.health += 5
                        print(player.health)

    elif "drink" in command:
        item_requested = command[6:]
        for item in player.inventory:  # Go through every item
            if item.name.lower() == item_requested.lower():  # and see if it matches the name of the item u are looking
                if isinstance(item, Drinkable):
                    item.drink()
                    print("You have drunk the beverage")
                    print("You're health is:")
                    player.health += 5
                    print(player.health)
                    print("_________________________________________________________________________________________")
                    print()

                elif isinstance(item, Consumable):  # If that item object is a consumable
                    player.eat()  # Eat it.
                    print("You have eaten ")
                    player.health += 5
                    print(player.health)
    elif "drop" in command:
        item_wanted = command[5:]
        drop = False
        for item in player.inventory:
            if item.name.lower() == item_wanted.lower():
                drop = True
                player.inventory.remove(item)
                player.location.inventory.append(item)
        if not drop:
            print("You can't drop it")
        print()

    elif "help" or "?" in command:
        print("To mve type: south, east, north, west")

    elif command == 'inventory':
        print("You're inventory is:")
        item_number = 1
        for item in player.inventory:
            print('%s. ' % item_number + item.name)  # '/n'
            print()
            item_number += 1

    elif command == 'use lens':
        player.use_lens()

    elif "attack" in command:
        human = command[7:]
        character_to_remove = None
        for stuff in player.location.characters:
            if stuff.name.lower() in human.lower():
                if isinstance(stuff, Character):
                    player.attack(stuff)
                    print("KABOOM!!!!!!!!!")
                    if stuff.health <= 0:
                        character_to_remove = stuff
        if character_to_remove is not None:
            player.location.characters.remove(character_to_remove)

    elif 'open chest with key' in command:
        if player.inventory == key:
            for thing in player.inventory:
                if isinstance(thing, Key):
                    Chest.open_chest(chest, player)
                    player.pick_up(book)

        else:
            print("Key is not in your inventory.")

    else:
        print("Command not recognized")

     # TO DO LIST:
        # MAKE IT SO YOU CAN FIND THE KEY AND THEN BE ABLE TO OPEN CHEST
        # Make a friend that can talk and lead the player
        # IF yOU PUT FLYING SHOES YOU DIE BECAUSE YOU DONT KNOW HOW TO FLY
