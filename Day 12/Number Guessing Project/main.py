import random
from art import logo

HARD = 5
EASY = 10

def generate_number():
    return random.randint(1,100)

def check_if_correct(number,users_guess):
    if number == users_guess:
        return True

def choose_difficulty(choice):
    if choice == 'easy':
        return EASY
    elif choice == 'hard':
        return HARD

def game():
    random_number = generate_number()
    users_guess = -1
    attempts = 0

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = choose_difficulty(difficulty)

    for i in range(attempts):
        print(f"You have {attempts} attempts to guess the correct number.")
        users_guess = int(input("Make a guess: "))
        if check_if_correct(random_number,users_guess):
            print(f"Congratulations! You've found correct number {random_number}")
            return
        else:
            if users_guess > random_number:
                print("Too high.")
                attempts -= 1
            else:
                print("Too low.")
                attempts -= 1

    print(f"You lost. Correct answer was {random_number}")

game()