import random
# print("The total number when the dies are added is:")
# print(answer1+answer2)
# print("The initial amount of money is: $15")
# initial_money = 15
# if answer1+answer2 == 7:
#     print("You have win your bet back, plus an additional $4")


def lucky7s():
    money = 15
    rounds = 0
    highest_amout_money = money
    highest_round = 0

    while money > 0:
        if highest_amout_money < money:
            highest_amout_money = money
            highest_round = rounds
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        money -= 1    # money minus 1, and setting money as the answer (money = money - 1)
        rounds += 1    # round + 1 = round
        if roll1 + roll2 == 7:
            money += 5
            print("you have won the bet, plus an additional $4")
        else:
            print("You have lost the bet")
    print("you have lost the game! it took you %d rounds to lose. "
            "Your highest amount of money was $%d in round number %d." % (rounds, highest_amout_money, highest_round))
lucky7s()