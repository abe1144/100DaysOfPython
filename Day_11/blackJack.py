import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# function to deal cards


def deal_card():
    return random.choice(cards)

# function to calculate score given a list of cards


def calculate_score(loc):
    if len(loc) == 2 and sum(loc) == 21:
        return 0
    elif sum(loc) > 21:
        if 11 in loc:
            loc.remove(11)
            loc.append(1)
            calculate_score(loc)
        else:
            return sum(loc)
    else:
        return sum(loc)


def status(loc):
    print()


play_another = True
draw_another = True


while play_another:
    new_game = input(
        "Would you like to play a game of Black Jack? 'y' or 'n': \n")
    if new_game == 'n':
        play_another = False
        exit()
    else:
        print(logo)
        play_another = True
        draw_another = True
        computer_cards = []
        user_cards = []

    # deal initial cards:
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print("Your Cards: {}, Total Score: {}".format(
        user_cards, calculate_score(user_cards)))
    print("Computer's first card: {}".format(computer_cards[0]))
    while draw_another:
        new_card = input("Would you like another card? 'y' or 'n': \n")
        if new_card == 'n':
            draw_another = False
        else:
            user_cards.append(deal_card())

            if calculate_score(user_cards) > 21:
                print("Busted! You lose. Final Score: {}".format(sum(user_cards)))
                draw_another = False
            else:
                print("Your Cards: {}, Total Score: {}".format(
                    user_cards, calculate_score(user_cards)))

    # Computer's turn
    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    if calculate_score(user_cards) > calculate_score(computer_cards) and calculate_score(user_cards) < 21:
        print("You Win. Your Cards: {}, Total Score: {}. Computer Cards: {}, Total Score: {}".format(
            user_cards, sum(user_cards), computer_cards, sum(computer_cards)))
    elif calculate_score(user_cards) == 0 and calculate_score(computer_cards) != 0:
        print("You Win. Your Cards: {}, Total Score: {}. Computer Cards: {}, Total Score: {}".format(
            user_cards, sum(user_cards), computer_cards, sum(computer_cards)))
    elif calculate_score(user_cards) < calculate_score(computer_cards) and calculate_score(computer_cards) > 21:
        print("You Win. Your Cards: {}, Total Score: {}. Computer Cards: {}, Total Score: {}".format(
            user_cards, sum(user_cards), computer_cards, sum(computer_cards)))
    elif calculate_score(user_cards) == calculate_score(computer_cards):
        print("It's a draw. Your Cards: {}, Total Score: {}. Computer Cards: {}, Total Score: {}".format(
            user_cards, sum(user_cards), computer_cards, sum(computer_cards)))
    else:
        print("You Lose. Your Cards: {}, Total Score: {}. Computer Cards: {}, Total Score: {}".format(
            user_cards, sum(user_cards), computer_cards, sum(computer_cards)))
