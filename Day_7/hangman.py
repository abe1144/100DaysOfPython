# Choose a random word
import random

word_list = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

# ask the user to guess a letter and assign their answer to a variable called guess

guess = input("Guess a letter: ").lower()

# check if the guessed letter is one of the letters in the chosen word
blanks_list = ["_" for letter in chosen_word]
print(''.join(blank_list))
for letter in chosen_word:
    # generate blanks for each letter
    if letter == guess:
        print("right")
    else:
        print("wrong")

#
