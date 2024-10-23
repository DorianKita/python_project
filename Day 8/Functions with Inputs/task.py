def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")

def life_in_weeks(age):
    one_year = 52
    whole_life = 90 * one_year
    lived = age * one_year
    live_left = whole_life - lived
    print(f"You have {live_left} weeks left.")

life_in_weeks(34)