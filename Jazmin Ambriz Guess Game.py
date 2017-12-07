import random
answer = random.randint(1,50)
print(answer)
turns_left = 5
guess = int(input("What is your guess?"))  # str
turns_left -= 1
correct_guess = False

while turns_left > 0 and correct_guess == False:
 if guess == answer:
    print("You win!")
    correct_guess = True
 elif guess > answer:
    print("Too high!")
    guess = int(input("Guess again"))
    turns_left -= 1
 elif guess < answer:
    print("Too low!")
    guess = int(input("Guess again"))
    turns_left -= 1












# Generate a number
# Ask the user for an input(Number)
# Does the guess match the number?
# Add "Higher and "Lower"
# Add 5 guesses













