import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ["rock", "paper", "scissors"]
choice_img = [rock, paper, scissors]

choose = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))

user_choice = choices[choose]

cpu_choice_int = random.randint(0, 2)
cpu_choice = choices[cpu_choice_int]

# check game outcome

if choose == cpu_choice_int:
    print(choice_img[choose])
    print("Computer Chooses:")
    print(choice_img[cpu_choice_int])
    print("It's a Draw!")
elif user_choice == "0" and cpu_choice_int == 2:
    print(choice_img[choose])
    print("Computer Chooses:")
    print(choice_img[cpu_choice_int])
    print("You Win!")
elif user_choice == "1" and cpu_choice_int == "0":
    print(choice_img[choose])
    print("Computer Chooses:")
    print(choice_img[cpu_choice_int])
    print("You Win!")
elif user_choice == "2" and cpu_choice_int == "1":
    print(choice_img[choose])
    print("Computer Chooses:")
    print(choice_img[cpu_choice_int])
    print("You Win!")
else:
    print(choice_img[choose])
    print("Computer Chooses:")
    print(choice_img[cpu_choice_int])
    print("You Lose")
