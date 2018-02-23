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




