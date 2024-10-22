print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

direction = input("You standing at the crossroads... Where do you want to go?\nType left or right ").lower()

if direction == "left":
    patience = input("\nYou've came across big lake... Do you want to swim or wait for a boat?\nType swim or wait ").lower()
    if patience == "wait":
        door = input("\nYou've came to an island with 3 doors which one you choose?\nType red, yellow or blue ").lower()
        if door == "yellow":
            print("\nCongratulations You Won... but princess is in another castle...")
        elif door == "red":
            print("\nBurned by fire. GAME OVER")
        elif door == "blue":
            print("\nEaten by beasts. GAME OVER")
        else:
            print("\nGame Over looser")
    else:
        print("You've been attacked by sharknado!!!\nGAME OVER")
else:
    print("You fall into a hole.\nGAME OVER")