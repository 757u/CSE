# ''''''
# import random
#  # print("Hello world")
# #
# # # Jazmin
# #
# # a = 4
# # b = 3
# # print(3 + 5)
# # print(5 - 3)
# # print(3 * 5)
# # print(6 / 2)
# # print(3 ** 2)
# #
# # print()
# # print("Try to figure out how this works")
# # print(14 % 5)
# #
# # # the "%" sign is a modulus. It finds the reminder.
# #
# # car_name = "Wibe Mobile"
# # car_type = "BW"
# # car_cylinder = 8
# # car_mpg = 5000.9
# #
# # print("I have a car called %s. It's pretty nice." % car_name)
# # print("I have a car called %s. It's a %s." % (car_name, car_type)) # watch the order
# #
# # # Here is where we get a little fancy
# # # print("What is your name?")
# # name = input("What is your name")
# # print("Hello %s." % name)
# #
# # age = input("How old are you?")
# # print("%s?! That's really old. You belong in a retirement home" % age)
# #
# # print("How are you doing today?")
#
# # Functions
#
#
# def print_hw() : # def=define
#     print("Hello World.")
#     print("Enjoy the day.") # 4 spaces
#
#
#     print_hw()
#
#
# def say_hi(name): # Name is a "parameter"
#         print("Hello %s" % name)
#         print("Coding is great!")
#
#
# say_hi("Jazmin")
#
#
# def print_age(name, age) :
#     print("%s is %d years old" % (name, age))
#     age = age + 1
#     print("Next year, %s will be %d years old" % (name, age))
#
#
# print_age("Jazmin", 15)
#
#
# def algebra_hw(x) :
#     return x**3 + 4*x**2 + 7 * x - 4
#
#
# print(algebra_hw(3))
# print(algebra_hw(4))
# print(algebra_hw(5))
# print(algebra_hw(6))
# print(algebra_hw(7))
#
#
# # if statements
#
#
# def grade_calc(percentage) :
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:  # elif
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#         return "F"
#
#
# print(grade_calc(25))
#
# '''Write a function called "happy-birthday"
# that "sings" (prints) Happy birthday
#
# It must take one parameter called "name"'''
#
#
# def happy_bday(name):
#     print("Happy Birthday")
#     print("Happy Birthday to you")
#     print("Happy Birthday dear computer")
#     print("Happy Birthday to you")
#
# happy_bday("computer")
#
#
# # Loops
#
# for num in  range(10):
#     print(num + 1)
#
# # While Loops (BEWARE!!!!!!)
#
# a = 1
# while a < 10: #This is the condition, it must be true to execute,
#               # it must be true to execute
#     print(a)
#     a += 1  #This iterates so that we can break the loop
#
# Random Numbers
# import random # This should be on line 1
# print(random.randint(0,1000))
#
# c = '1'
# print(c == 1) # we have a string and an inte
# print(int(c) == 1)
# print(c == str(1))
#
#
#
# # Complarisons
#
# print(1 == 1) # Use a double equal sign to compare
# print(1 != 2) # 1 is not equal to 2. used to show that something is false.
# print(not False) # "1" is the "not" operator
#
#
#
#
# Lists

the_count = [1, 2, 3, 4, 5]
cheesburger_ingredients = ['cheese', "beef", "sauce", "sesame seed bun", "avocado", "onion"]
print(cheesburger_ingredients[0])
print(cheesburger_ingredients[3])
print(len(cheesburger_ingredients))
print(len(the_count))

# # Going through lists
# for item in cheesburger_ingredients:      # for loops are used when you the exact number of time that something is going through
#     print(item)
#
# for number in the_count:
#     print(number * 2)                     # " * " is the times sign x
#
# length = len(cheesburger_ingredients)
# range(5)     # A list of the numbers 0 through 4
# range(len(cheesburger_ingredients))  # Generates a list of all indices
#
# for num in range(len(cheesburger_ingredients)):
#     item = cheesburger_ingredients[num]
#     print("The item at index %d is %s" % (num, item))
#
#
# cheesburger_ingredients.append("lettuce")
# print(cheesburger_ingredients)
#
# # Recasting into a list
# strOne = "Hello World!"
# listOne = list (strOne)
# print(listOne)
# listOne[11] = '.'
# print(listOne[-1])
#
# # Adding things to a list
# cheesburger_ingredients.append("Fries")
# print(cheesburger_ingredients)
#
# # Remove things from a list
# cheesburger_ingredients.pop(1)
# print(cheesburger_ingredients)
# cheesburger_ingredients.remove("cheese")
# print(cheesburger_ingredients)
#
# # Getting the alphabet
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)
#
#
# # Making things Lowercase
# strTwo = "ThIs Is A VeRy oDD sEnTENcE"
# lowercase = strTwo.lower()
# print(lowercase)
#
#
#
#
#
# #list of letters a person has guesses so far
#
# L1 = ["H", "e", "l", "l", "o"]
# "".join(L1)
# print(L1)


# Dictionaries - Made up of key: value pair

dictionary = {"name": 'Lance', 'age': 26, 'height': 6 * 12 + 2}

# Accessing things from a dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Add a pair to a dictionary
dictionary["proffesion"] = "telemarketer"

large_dictionary = {
    'CA': 'California',
    'AZ': 'Arizona',
    'NY': 'New York'
}
print(large_dictionary['NY'])
larger_dictionary = {
    'CA': 'California',
    'AZ': 'Arizona',
    'NY': 'New York'
}
print(large_dictionary['NY'])


larger_dictionary = {
    'CA': [
        'Fresno',
        "San Francisco",
        "San Jose"

    ],
    'Az':[
        "Phoenix",
        "TusCon"
    ],
    'NY': [
        "New York City",
        "Brooklyn",
    ]
}
print(larger_dictionary['NY'])
print(larger_dictionary['NY'][1])
print(larger_dictionary)
print(larger_dictionary ['Az'][0])

largest_dictionary = {
    'CA':{
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona',

        ]
    },
    'AZ':{
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico',
        ]
    },
    'NY':{
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts'
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    },

}

current_node = largest_dictionary['NY']
print(current_node['POPULATION'])




