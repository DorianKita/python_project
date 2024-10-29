from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)
def calculate():
    should_acc = True
    num1 = float(input("What is the first number: "))

    while should_acc:
        for symbol in operations:
            print(symbol)
        symbol = input("What mathematical operation do you want to perform: ")
        num2 = float(input("What is the second number: "))
        result = operations[symbol](num1,num2)
        print(f"{num1} {symbol} {num2} = {result}")

        choice = input("Type 'y' to perform next calculation with current value or type 'n' to start new calculation: ").lower()

        if choice == "y":
            num1 = result
        else:
            should_acc = False
            calculate()
calculate()