class Item(object):
    def __init__(self, name, description, value, weight):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight


class Weapons(object):
    def __init__(self, sword, knife,shovel, spray_bottles_with_tomatosauce):
        self.sword = sword
        self.knife = knife
        self.shovel = shovel
        self.tomato_sauce = spray_bottles_with_tomatosauce


class Wearable(object):
    def __init__(self, backpack, armor, clothing):
        self.backpack = backpack
        self.armor = armor
        self.clothing = clothing


class Consumable(object):
    def __init__(self, food, water_bottle):
        self.food = food
        self.water_bottle = water_bottle

class Potions(object)












