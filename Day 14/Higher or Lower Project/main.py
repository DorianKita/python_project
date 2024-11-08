import random

from art import logo,vs
from game_data import data

def pick_players(data):
    return random.choice(data)

def format_players(player):
    player_name = player['name']
    player_desc = player['description']
    player_country = player['country']
    return f"{player_name}, a {player_desc}, from {player_country}"

def pick_winner(player_a, player_b, guess):
    if player_a['follower_count'] > player_b['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'

player_a = pick_players(data)
player_b = pick_players(data)



if player_a == player_b:
    player_b = pick_players(data)



score = 0
game_over = False

print(logo)
while not game_over:
    print(f"Compare A: {format_players(player_a)}")
    print(vs)
    print(f"Against B: {format_players(player_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if pick_winner(player_a,player_b,guess):
        print("\n" * 20)
        print(logo)
        score +=1
        print(f"You're right! Current score: {score}")
        player_a = player_b
        player_b = pick_players(data)

    else:
        print("\n" * 20)
        print(logo)
        print(f"Sorry that wasn't good answer. Final score: {score}")
        game_over = True