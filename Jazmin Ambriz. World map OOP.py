class Room(object):
    def __init__(self, name, north, south, east, west, southeast, southwest, northeast, northwest, description):
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


living = Room("Living Room", None, None, None, 'kitchen', None, None, None, None, 'There are three couches and a TV.')

kitchen = Room("Kitchen", "Old Room", None, "Living", "Garden", None, None, None, None, "Big wooden table, kitchen has"
               "old rusty drawers with a sink. To the west there is a big clear door leading to the garden")

Garden = Room("Garden", None,None, "Antique Art Room", None, None, None, None, None, "'Green grass all over, colorful"
             " flower are starting to bloom")
Art_Room = Room("Art Room", None, None, None, "Garden", None, None, None, None, "To the east there is a brick wall,"
               " which has no exist. In the middle of the room there is an art stand with some dry paints by the side.")

Southeast_of_Garden = Room("Front of House", "Inside of House", "Dangerous Forest", None, None, None, None, None, None,
                           "Black two story house, with two white windows in front.")

Inside_House = Room("Inside House", "Inside Pool", None, "Living Room", None, None, None, "Bedroom", "Kitchen", "You"
                    "are inside a two story house; standing at the beginning of a corridor. Around you there are"
                    "different rooms and doors leading to the yet unknown. To the side a bit to the east there"
                    "is a fancy staircase leading to the second floor.")

Swimming_pool = Room("Inside Pool", None, None, "Big Bathroom", None, "Bedroom", None, None, None, "Big rectangular pool"
                    "with crystal water, the bottom can not be seen because of its deepness, inside the pool there are"
                    "infinite steps leading down to the bottom of the pool (if there is a bottom.")





current_node = hdum
directions = ['north', 'south', 'east', 'west']

while True:
    print(current_node['name'])   # change
    print(current_node['descriptions'])   # change

    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognize")




