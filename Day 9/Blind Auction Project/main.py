from art import logo
new_bidder = True
auction = {}
# TODO-1: Ask the user for input
print(logo)
print("Welcome to the blind auction!")

while new_bidder:
    name = input("What is your name:\n")
    bid = int(input("What is your bid:\n$:"))
    auction[name] = bid
    another_one = input("Is there a next bidder? Type 'yes' or 'no'.\n").lower()
    if another_one != 'yes':
        new_bidder = False
        print('\n' * 100)
    else:
        print('\n' * 100)
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
highest_bid = 0
winner = ""
for bid in auction:
    if auction[bid] > highest_bid:
        highest_bid = auction[bid]
        winner = bid


print(f"Winner is {winner}, with bid of ${highest_bid}")