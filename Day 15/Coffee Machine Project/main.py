MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(resources,money):
    for name in resources:
        if name == 'water':
            print(f"{name.capitalize()}: {resources[name]}ml")
        elif name == 'milk':
            print(f"{name.capitalize()}: {resources[name]}ml")
        else:
            print(f"{name.capitalize()}: {resources[name]}g")
    print(f"Money: ${money}")

def check_resources(choice,resources,drinks):
    if choice in drinks:
        for key in resources.keys():
            if key in drinks[choice]['ingredients'].keys():
                if resources[key] >= drinks[choice]['ingredients'][key]:
                    print()
                else:
                    print(f"Sorry there is not enough {key}")
                    return False
        return True
    elif choice != "report":
        print("Sorry, we don't have this drink.")

def process_coins():
    quarters_inserted = int(input("How many quarters? : "))
    dimes_inserted = int(input("How many dimes? : "))
    nickles_inserted = int(input("How many nickles? : "))
    pennies_inserted = int(input("How many pennies? : "))

    inserted_coins = 0.25 * quarters_inserted + 0.10 * dimes_inserted + 0.05 * nickles_inserted + 0.01 * pennies_inserted
    return inserted_coins


def check_transaction_successful(money,drinks,choice):
    if money < drinks[choice]['cost']:
        return print("Sorry that's not enough money. Money refunded.")
    elif money > drinks[choice]['cost']:
        change = round(money - drinks[choice]['cost'],2)
        money = drinks[choice]['cost']
        print(f"Here is ${change} dollars in change.")
        return money
    elif money == drinks[choice]['cost']:
        money = drinks[choice]['cost']
        return money

def make_coffe(resources, drinks, choice):
    for key in resources.keys():
        if key in drinks[choice]['ingredients'].keys():
            resources[key] -= MENU[choice]['ingredients'][key]
            resources[key] = resources[key]
    return(resources)


def coffee(resources,):
    money = 0.00
    earned_money = 0.00
    new_resources = resources
    is_off = False
    # prompt user and ask what they want to order
    while not is_off:
        user_choice = input('What would you like to order? (espresso/latte/cappuccino): ').lower()

        # turn off coffe machine by entering off
        if user_choice == 'off':
            print("Good bye.")
            return

        # print report
        if user_choice == 'report':
            print_report(new_resources,earned_money)
            continue
        # check resources sufficent?

        if not check_resources(user_choice,new_resources,MENU):
            return

        # process coins
        print("Please insert coins.")
        money = process_coins()

        # check transaction successful?
        earned_money += check_transaction_successful(money,MENU,user_choice)

        # make coffee
        new_resources = make_coffe(new_resources,MENU,user_choice)
        print(new_resources)
        print(f"Here is your {user_choice}. Enjoy!")

coffee(resources)
