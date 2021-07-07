from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1, 100)

if difficulty == "easy":
    total_guesses = 10
elif difficulty == "hard":
    total_guesses = 5


while total_guesses > 0:
    print("You have {} attempts remaining to guess the number.".format(total_guesses))
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
        total_guesses -= 1
    elif guess < number:
        print("Too low.")
        total_guesses -= 1
    else:
        print("That's right it is {}".format(guess))
        total_guesses = 0

if guess != number:
    print("You ran out of guesses. Better luck next time.")
else:
    print("You win!")
