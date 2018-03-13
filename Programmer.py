class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def walk(self):
        print("You are walking to your job station")

class Programmer(Employee):
    def __init__(self, name, age, job, degree_of_knowledge):
        super(Programmer, self).__init__(name, age,job)
        self.deggree_of_knowlege = degree_of_knowledge

    def start_Programming(self):
        print("You are at your job, and you are beginning to program")
