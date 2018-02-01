import random

# '''
# # This is a guide of how to make hangman
#
# 1. Make a word bank - 10 items (checked)
# 2. Select a random item to guess (checked)
# 3. take in a letter and add it to a list of letters_guessed (checked)
# -up to ten incorrect guesses (checked)
# guesses_left = 10 (checked)
# list of letters that you have guesses (checked)
# you only reveal the letter if its on a list of letters_guessed
# letters_guessed = ('e', 'h', "o', 's', "p',

# 4. Reveal Letters based on input
# 5. Create win and lost conditions
#turn random word into a list
# '''
# you will use the "".join(l1) to make it look pretty


word_bank = ["Afghanistan", "Bosnia and Herzegovina", "Central African Republic", "Djibouti", "Equatorial Guinea",
             "Hungary", "Luxembourg", "Mozambique", "Switzerland", "Ukraine"]
word = random.choice(word_bank).lower()
print(word)
# guess = 10
guess_left = 10



list_of_letters_guessed_by_player = ['']

player_letter = ""
while guess_left > 1:
    output = []
    for letter in word:
        if letter in list_of_letters_guessed_by_player:
            output.append(letter)
        else:
            output.append("*")

    output = ''.join(output)
    print(output)



    if player_letter not in word:
        guess_left -= 1
    print("you have %s guesses left" % guess_left)
    if "*" not in output:
        print("You Win")
        exit(0)

    player_letter = input("What is your letter guess?").lower()
    list_of_letters_guessed_by_player.append(player_letter)
    print(list_of_letters_guessed_by_player)
print(" You Lost")