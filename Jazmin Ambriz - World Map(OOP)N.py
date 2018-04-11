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

Southeast_of_Garden = Room("Front of House", 'Second_Floor', "Inside_House", "Dangerous Forest", "Living Room", None,
                           None, None, None, None, "Black two story house, with two white windows in front.")

Inside_House = Room("Inside House", "Second_Floor", "Inside_Pool", None, "Living", "Kitchen", None, None,
                    "Bedroom", "Art_Room", "You are inside a two story house; standing at the beginning of a corridor."
                    " Around you there are different rooms and doors leading to the yet unknown. To the side a bit to"
                    " the east there is a fancy staircase leading to the second floor.")

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

Second_Floor = Room("Up stairs", None, "Special_Room", None, "Library", "Waiting_Room", None, None,
                    "Single_Room's Hallway", "Waiting Room", "You are up stairs in the second floor, This floor looks "
                    "very similar to the first floor just with different rooms that you are about to discover"
                    " (Only if you are willing to).")
Staircase = Room("Staircase", None, "Special_Room", None, "Library", "Office", None, None, "Bedroom", "Waiting_Room",
                 "You are back at where the fancy staircase start, you are still in the second floor.")

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
                            "writing on them.1")

SECOND_Single_bedroom = Room("SECOND_Single_bedroom", None, None, "FIRST_Single_bedroom", None, "Special_Room",
                             "Bedroom", "Waiting_Room", None, None, "You are in a tiny room, it looks"
                             " like you can only fit a small bed. The walls are pale green and they have some "
                             "writing on them.2")

Special_Room = Room("Second Floor Main Bedroom", None, None, "Second_Floor", "Hallway", "Waiting Room", "Library",
                    "Waiting Room", "Hallway", None, "You are standing in a very typical room, "
                    "there is a bed, some lamps by the sides, books on the floor. To the north wall there is an open"
                    "window. But then you notice one of the weirdest things; part of the floor is glass allowing you to"
                    " see down and take a look at the pool. You are not sure if the glass is very stable.")

Gym = Room("Gym", None, "Back Gym wall", "Waiting_Room", "Second Floor Bedroom", "Waiting Room", "Library",
           "Waiting Room", None, "Gym", "The gym is weird shaped. It is found at the northwest corner of the house. "
           "Instead of being a regular rectangular shape building it is half circle.")

Office = Room("Office", None, "Waiting_Room", None, "Staircase", "Waiting Room", None, None, "Library",
              "Waiting_Room", "You are in a room that looks like an office. This room has a desk, an old computer, "
              "and some bookshelf.")

Waiting_Room = Room("Waiting Room", None, "Gym", "Office", "Library", None, "Office", None, "Second Floor Bedroom",
                    None, "You find yourself in a small lobby next to an office. The Waiting room or lobby")

current_node = Southeast_of_Garden
directions = ['north', 'south', 'east', 'west', 'southeast', 'southwest', 'northeast', 'northwest', 'up']
short_directions = ['n', 's', 'e', 'w', 'se', 'sw', 'ne', 'nw', 'u']

while True:

    print(current_node.name)   
    print(current_node.description)

    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)

    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
