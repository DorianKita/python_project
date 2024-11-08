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
            "coffee": 120,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.00

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
                    print("")
                else:
                    print(f"Sorry there is not enough {key}")
                    return False


    else:
        print("Sorry, we don't have this drink.")

def coffee():
    is_off = False
    # prompt user and ask what they want to order

    user_choice = input('What would you like to order? (espresso/latte/cappuccino): ').lower()

    # turn off coffe machine by entering off
    if user_choice == 'off':
        is_off = True

    # print report
    if user_choice == 'report':
        print_report(resources,money)

    # check resources sufficent?

    if not check_resources(user_choice,resources,MENU):
        return

    # process coins

    # check transaction successful?

    # make coffee

coffee()
