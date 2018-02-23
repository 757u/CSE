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
        self.air_conditioning = True

    def turn_on(self):
        if self.running:
            print("Nothing happens.")
        self.running = True
        print("The car starts.")

    def move_forward(self):
        if self.running:
            print("You move forward")
        else:
            print("Nothing Happends")

    def turn_off(self):
        if self.running:
            self.running = False
            print("You turn the car off")
        else:
            print("The car is already off")

    def go_for_drive(self, passenger):
        print("%d passengers get in." % passenger)
        self.passengers = passenger
        self.turn_on()
        self.move_forward()
        self.move_forward()
        self.move_forward()
        self.turn_off()
        print("%d passengers get out." % passenger)
        self.passengers = 0


my_car = car("Lexus Mobile", "White", 4, 9001)
my_car.go_for_drive(4)
