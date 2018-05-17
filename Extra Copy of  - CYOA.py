while True:
    # Room Information
    print(player.location.name)
    print(player.location.description)

    if player.location.inventory is not None and len(player.location.inventory) > 0:
        print()
        print("The following item(s) are in the room: ")
        for item in player.location.inventory:
            print(item.name)
            print(item.description)

    if len(player.location.characters) > 0:
        if player.lens is False:
            print("You sense a presence.")
        elif len(player.location.characters) == 1:
            print("You see a %s" % player.location.characters[0].name)
        else:
            print("You see %d goblins" % len(player.location.characters))

    if player.location == Road:
        print()
        if "SOUTHWEST" in input():
            print("Game Over!!!")
            quit(0)

    # Asks for input
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
