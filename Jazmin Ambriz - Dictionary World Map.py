world_map = {
    'LIVING': {
        'NAME': 'Living Room',
        'DESCRIPTION': 'There are three couches and a TV.',
        'PATHS': {
            'WEST': 'KITCHEN'
        }
    },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': 'Big wooden table, kitchen has old rusty drawers with a sink. To the west there is a big clear'
                       ' door leading to the garden ',
        'PATHS': {
            'EAST': 'LIVING',
            'WEST': 'GARDEN'
        }
    },
    'GARDEN': {
        'NAME': 'Garden',
        'DESCRIPTION': 'Green grass all over, colorful flower are starting to bloom',
        'PATHS': {
            'EAST': 'Antique art room'
        }
    },
    'ART ROOM': {
        'NAME': 'Art room',
        'DESCRIPTION': 'To the east there is a brick wall, which has no exist. In the middle of the room there is an'
                       ' art stand with some dry paints by the side.',
        'PATHS': {
            'WEST': 'Garden'
        }
    },
    'SOUTHEAST OF GARDEN': {
        'NAME': 'Front of House',
        'DESCRIPTION': 'Black two story house, '
    }

}
current_node = world_map['LIVING']
directions = ['WEST', 'NORTH', 'SOUTH', 'EAST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])

    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            print(name_of_node)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognize")
