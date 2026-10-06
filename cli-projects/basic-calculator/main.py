# basic calculator
import sys


def input_num():
    try:
        c = float(input("Enter first number: "))
        d = float(input("Enter second number: "))
        return c, d
    except ValueError or TypeError:
        print("Please enter a valid number next time!")
        sys.exit()


def division(a, b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b


def root(a):
    if a < 0:
        print("Cannot take root of a negative number")
    else:
        return a ** 0.5


def square(a): return a ** 2


database = {
    "add": "addition",
    "sub": "subtraction",
    "mul": "multiplication",
    "div": "division",
    "sq": "square",
    "rt": "root"
}
print("Basic calculator")
print("Code\t:\tOperation")
for key, value in database.items():
    print(f"{key}\t:\t{value}")
VALID_BASIC = {"add", "sub", "mul", "div"}
VALID_SPECIAL = {"sq", "rt"}

user_input = input("Enter a code from above:").strip().lower()

if user_input in VALID_BASIC:
    x, y = input_num()
    if user_input == "add":
        result = x + y
        print(f"Addition: {result}")
    elif user_input == "sub":
        result = x - y
        print(f"Subtraction: {result}")
    elif user_input == "mul":
        result = x * y
        print(f"Multiplication: {result}")
    else:
        result = division(x, y)
        print(f"Division: {result}")
elif user_input in VALID_SPECIAL:
    number = int(input(f"Enter the number to {user_input}: "))
    if user_input == "rt":
        result = root(number)
        print(f"The root of {number} is: {result}")
    else:
        result = square(number)
        print(f"The square of {number} is: {result}")
else:
    print("Invalid input!")
