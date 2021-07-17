from gameData import data
from art import logo, vs
import random
import os


def clear():
    return os.system('cls')


current_score = 0
choice_a = random.choice(data)
choice_b = random.choice(data)

end = False


def calculate_score(a, b):
    if a['follower_count'] > b['follower_count']:
        return a
    else:
        return b


while not end:

    print(logo)
    if current_score > 0:
        print("You're right! Current score: {}".format(current_score))

    print("Compare A: {}, {}, from {}".format(
        choice_a["name"], choice_a['description'], choice_a['country']))
    print(vs)
    print("Compare B: {}, {}, from {}".format(
        choice_b["name"], choice_b["description"], choice_b["country"]))
    choice = input("Who has more followers? Type 'A' or 'B': ")

    result = calculate_score(choice_a, choice_b)

    if choice == "a":
        user_choice = choice_a
    else:
        user_choice = choice_b

    if result == user_choice:
        current_score += 1
        choice_a = choice_b
        choice_b = random.choice(data)
        clear()
    else:
        end = True
        clear()
        print(logo)
        print("Sorry, that's wrong. Final score: {}".format(current_score))
