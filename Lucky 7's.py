import random
answer1 = random.randint(1,6)
answer2 = random.randint(1,6)
print(answer1)
print(answer2)
# print("The total number when the dies are added is:")
# print(answer1+answer2)
# print("The initial amount of money is: $15")
# initial_money = 15
# if answer1+answer2 == 7:
#     print("You have win your bet back, plus an additional $4")


def bet(roll1, roll2, money, rounds, highest_amout_money, highest_round):
    if money > 0:
        if highest_amout_money < money:
            highest_amout_money = money
            highest_round = rounds
        money -= 1    # money minus 1, and setting money as the answer (money = money - 1)
        rounds += 1    # round + 1 = round
        if roll1 + roll2 == 7:
            money += 5
            print("you have won the bet, plus an additional $4")
            bet(roll1, roll2, money, rounds, highest_amout_money, highest_round)
        elif roll1 + roll2 != 7:
            print("You have lost the bet")
            bet(roll1, roll2, money, rounds, highest_amout_money, highest_round)


bet(answer1, answer2, 5, 0, 0, 0)