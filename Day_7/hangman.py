# Choose a random word
import random
from stages import stages
from words import word_list

chosen_word = random.choice(word_list)

# create an empty list display
display = ["_" for letter in chosen_word]

lives = 6
game_over = False
guessed_letters = []


while not game_over:
    print('Guessed letters: {}'.format(guessed_letters))
    print(''.join(display))
    # ask the user to guess a letter and assign their answer to a variable called guess
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed {}".format(guess))

    guessed_letters.append(guess)
    # check if the guessed letter is one of the letters in the chosen word
    word = []
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # generate blanks for each letter
        if letter == guess:
            display[position] = letter

    print(''.join(display))
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win.")
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(stages[0])
            print('You lose. The word was {}'.format(chosen_word))
