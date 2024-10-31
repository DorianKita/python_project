import random
from art import logo
# from itertools import count
#
#
# def blackjack():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     def pick_starting_cards(cards):
#         random_card = random.choice(cards)
#         return random_card
#
#     user_hand = []
#     computer_hand = []
#
#     for i in range(2):
#         user_hand.append(pick_starting_cards(cards))
#         computer_hand.append(pick_starting_cards(cards))
#
#     def count_hand(hand):
#         result = sum(hand)
#         return result
#
#     user_score = count_hand(user_hand)
#     computer_score = count_hand(computer_hand)
#     print(user_hand)
#     print(computer_hand)
#
#
#     if user_score == 21:
#         print("Wygrana blackjack!")
#         return
#     if computer_score == 21:
#         print("Przegrana komputer blackjack")
#         return
#
#     def check_if_ace():
#         if user_score > 21 and 11 in user_hand:
#             print(user_hand)
#             user_hand.remove(11)
#             user_hand.append(1)
#             print(user_hand)
#
#     def check_is_over_21(user):
#         points = count_hand(user_hand)
#         if user > 21:
#             check_if_ace()
#             if points > 21:
#                 print("Przegrana ponad 21")
#                 return True
#
#     if check_is_over_21(user_score):
#         return
#     another = False
#     if user_score <= 21:
#         another = True
#
#     while another:
#         another_card = input("Czy chcesz kolejna karte? y or n")
#         if another_card == "y":
#             user_hand.append(pick_starting_cards(cards))
#             user_score = count_hand(user_hand)
#             print(user_hand)
#             if check_is_over_21(user_score):
#                 return
#
#         else:
#             another = False
#
#     while computer_score < 17:
#         computer_hand.append(pick_starting_cards(cards))
#         computer_score = count_hand(computer_hand)
#         print(computer_score)
#         print(computer_hand)
#
#
#     if computer_score > 21:
#         print("Wygrałeś, komp ma ponad 21")
#     else:
#         if user_score > computer_score:
#             print("Wygrałes bo miales wiecej pkt niz komputer")
#         elif user_score == computer_score:
#             print("Remis")
#         else:
#             print("komp wygral bo mial wiecej pkt")
#
#
# blackjack()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def pick_card(cards):
        random_card = random.choice(cards)
        return random_card

def count_score(hand):
    return sum(hand)

def switch_11_to_1(hand):
    new_hand = hand.remove(11)
    new_hand = hand.append(1)
    return hand

def check_is_over_21(user_score, user_hand, computer_hand, computer_score):
    if user_score > 21:
        # if user have ace
        if 11 in user_hand:
            switch_11_to_1(user_hand)
            # if after switching 11 to 1 still >21 (function?)
            user_score = count_score(user_hand)
            if user_score > 21:
                print(f"Your final hand: {user_hand}, final score: {user_score}")
                print(f"Computer final hand: {computer_hand}, final score: {computer_score}")
                return "lose"
        else:
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(f"Computer final hand: {computer_hand}, final score: {computer_score}")
            return "lose"

def choose_winner(user_score,computer_score, user_hand, computer_hand):
    if computer_score > user_score:
        print(f"Your final hand: {user_hand}, final score: {user_score}")
        print(f"Computer final hand: {computer_hand}, final score: {computer_score}")
        print(f"Computer won!")
    elif computer_score == user_score:
        print(f"Your final hand: {user_hand}, final score: {user_score}")
        print(f"Computer final hand: {computer_hand}, final score: {computer_score}")
        print(f"Draw!")
    else:
        print(f"Your final hand: {user_hand}, final score: {user_score}")
        print(f"Computer final hand: {computer_hand}, final score: {computer_score}")
        print(f"You won!")

#######################################################
def blackjack():
    user_hand = []
    computer_hand = []
    play = input("Do you want to play a Blackjack game? Type 'y' or 'n'")

    while play == "y":
        print(logo)

        #pick a cart function
        for i in range(2):
            user_hand.append(pick_card(cards))

        computer_hand.append(pick_card(cards))
        #count score function
        user_score = count_score(user_hand)
        computer_score = count_score(computer_hand)

        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer first card: {computer_hand[0]}")

        #if user or computer have jackpot
        if computer_score == 21:
            print("Computer won with Blackjack")
            return
        elif user_score == 21:
            print("You won with Blackjack!")
            return

        if check_is_over_21(user_score, user_hand, computer_hand, computer_score) == "lose":
            print("Over 21, you lose.")
            return

        another_card = input("Do you want another card? Type 'y' or 'n': ")
        while another_card == "y":
            user_hand.append(pick_card(cards))
            user_score = count_score(user_hand)
            print(f"Your cards: {user_hand}. Your score is: {user_score}.")
            print(f"Computer first card: {computer_hand[0]}")
            if check_is_over_21(user_score, user_hand, computer_hand, computer_score) == "lose":
                print("Over 21, you lose.")
                return
            another_card = input("Do you want another card? Type 'y' or 'n': ")
                #if user wants another card? input

            #pick a card function
                #go back to counting score

        # add card until computer have >17
        while computer_score < 17:
            computer_hand.append(pick_card(cards))
            computer_score = count_score(computer_hand)
            print(f"Your cards: {user_hand}. Your score is: {user_score}.")
            print(f"Computer cards: {computer_hand}. Computer score is: {computer_score}.")

        #if computer have > 21 points user wins
        if computer_score > 21:
            print(f"You won! Computer score is over 21. Computer score was: {computer_score}")
            return
        # if not than we compare results

        choose_winner(user_score,computer_score, user_hand, computer_hand)
        play = input("Do you want to play a Blackjack game? Type 'y' or 'n'")
        if play == "y":
            blackjack()
        else:
            print("Goodbye")
blackjack()