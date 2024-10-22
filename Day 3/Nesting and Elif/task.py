print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age >18 :
        bill = 12
        photo = input("Do you want a photo?")
        if photo == "yes":
            bill+=3
        print(f"Please pay ${bill}")
    elif age >12 :
        bill = 7
        photo = input("Do you want a photo?")
        if photo == "yes":
            bill += 3
        print(f"Please pay ${bill}")
    else:
        bill = 5
        photo = input("Do you want a photo?")
        if photo == "yes":
            bill += 3
        print(f"Please pay ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
