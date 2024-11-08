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

player_a = pick_players(data)
player_b = pick_players(data)

if player_a == player_b:
    player_b = pick_players(data)




print(logo)
print(f"Compare A: {format_players(player_a)}")
print(vs)
print(f"Against B: {format_players(player_b)}")