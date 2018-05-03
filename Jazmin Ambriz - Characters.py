# Take damage
# Status Effect (paralyze, poison, burn, etc.)
# Description
# Perform Action
# Dialogue
# Death
# Attack
# Move?
# Pick up items
# Health

# has


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


player = Character("Player", "You", 100, False)
enemy = Character("Enemy", "It's a bad guy", 100, False, 10)

player.attack(enemy)
enemy.attack(player)
print(player.health)
enemy.attack(player)
print(player.health)
player.attack(enemy)
print(enemy.health)
enemy.attack(player)
player.eat()
print(player.health)
player.attack(enemy)
print(enemy.health)
enemy.eat()
print(enemy.health)
enemy.attack(player)
print(player.health)
enemy.attack(player)
enemy.attack(player)
enemy.attack(player)
print(player.health)
enemy.attack(player)
enemy.attack(player)
enemy.attack(player)
enemy.attack(player)
player.eat()
player.eat()
player.eat()
print(player.health)
print(player.death)
