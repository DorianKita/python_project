import random
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



#######################################################
def blackjack():
    user_hand = []
    computer_hand = []
    play = input("Do you want to play a jackpot? Type 'y' or 'n'")

    while play == "y":


        #pick a cart function
        for i in range(2):
            user_hand.append(pick_card(cards))
            computer_hand.append(pick_card(cards))
        print(user_hand,computer_hand)

        #count score function
        user_score = count_score(user_hand)
        computer_score = count_score(computer_hand)

        #if user or computer have jackpot
        if computer_score == 21:
            print("Computer won with Blackjack")
            return
        elif user_score == 21:
            print("You won with Blackjack!")
            return

        #if user points > 21
        if user_score > 21:
            #if user have ace
            if 11 in user_hand:
                switch_11_to_1(user_hand)
                # if after switching 11 to 1 still >21 (function?)


        #if user wants another card? input
            #pick a card function
                #go back to counting score

        # add card until computer have >17

        #if computer have > 21 points user wins

        # if not than we compare results



        user_hand = []
        computer_hand = []
        play = input("Do you want to play a jackpot? Type 'y' or 'n'")
    print("Goodbye")
blackjack()