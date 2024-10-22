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

possibilities = [rock,paper,scissors]
computer_chocie = random.choice(possibilities)

players_choice = int(input("Welcome to RPS Game. What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if players_choice == 0:
    print("You choose Rock ")
    print(rock)
elif players_choice == 1:
    print("You choose Paper ")
    print(paper)
elif players_choice == 2:
    print("You choose Scissors ")
    print(scissors)
else:
    print("Wrong number, you can choose 0,1 or 2")

if computer_chocie == rock:
    print("Computer choose Rock")
    print(rock)
elif computer_chocie == paper:
    print("Computer choose Paper")
    print(paper)
else:
    print("Computer choose Scissors")
    print(scissors)

if players_choice == 0 and computer_chocie == scissors:
    print("You WON!")
if players_choice == 0 and computer_chocie == paper:
    print("You LOOSE!")
if players_choice == 0 and computer_chocie == rock:
    print("It's a TIE!")

if players_choice == 1 and computer_chocie == rock:
    print("You WON!")
if players_choice == 1 and computer_chocie == scissors:
    print("You LOOSE!")
if players_choice == 1 and computer_chocie == paper:
    print("It's a TIE!")

if players_choice == 2 and computer_chocie == paper:
    print("You WON!")
if players_choice == 2 and computer_chocie == rock:
    print("You LOOSE!")
if players_choice == 2 and computer_chocie == scissors:
    print("It's a TIE!")