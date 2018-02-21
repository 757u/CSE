# Defining a class
class Cheeseburger(object):
    def __init__(self, patty, cheese):  # TWO underscores before and after
        self.patty = patty
        self.cheese = cheese
        self.eaten = False

    def give(self, name):
        print(name + "is thankful")

    def cut(self):
        print("You cut the cheeseburger")

    def eat(self):
        print("You eat the cheeseburger")
        self.eaten = True


#  Instantiating (The creation of) two cheeseburgers
burger1 = Cheeseburger("Beef", "Havarti")
burger2 = Cheeseburger("Beacon", "Swiss")

print(burger1.eaten)
print(burger2.cheese)

burger1.eat()
print(burger1.eaten)
print(burger2.eaten)

class car(object):
    def __init__(self, name, color, num_of_doors, hp,):
        self.color = color
        self.doors = num_of_doors
        self.running = False
        self.HP = hp
        self.passengers = 0
        self.name = name