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
        'DESCRIPTION': 'Black two story house, with two white windows in front.',

    'PATHS': {
        'NORTH': 'Inside of House',
        'SOUTH': 'Dangerous Forest',
        }
    },
    'INSIDE HOUSE':{
        'NAME': 'INSIDE THE HOUSE',
        'DESCRIPTION': 'You are inside a two story house; standing at the beginning of a corridor. Around you there'
                       ' are different rooms and doors leading to the yet unknown. To the side a bit to the east there'
                       ' is a fancy staircase leading to the second floor.',
        'PATHS': {
            'UP': 'Second floor',
            'NORTH': 'Inside Pool',
            'NORTHWEST': 'Kitchen',
            'EAST': 'Living room',
            'NORTHEAST': 'Bedroom'
        }
    },
    'SWIMMING POOL':{
        'NAME': 'Inside Pool',
        'DESCRIPTION': 'Big rectangular pool with crystal water, the bottom can not be seen because of its deepness, '
                       'inside the pool there are infinite steps leading down to the bottom of the pool (if there is a'
                       'bottom).'

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
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognize")
