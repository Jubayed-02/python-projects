from random import randint
import sys

print("Welcome to the number guessing game!")
player = input("What's your name? \n:").title()

rules = f"""
Rules:
    1. You have to guess a number in the range of 1 to 10.
    2. You have 3 chances to guess the right answer.
    3. Invalid input (letters, symbols, numbers outside 1-10) 
       still counts as one of your chances.
Best of luck, {player}!
"""
print(rules)

def check_input(attempt):
    try:
        value = int(input(f"Guess #{attempt}: "))
    except ValueError:
        return None
    except KeyboardInterrupt:
        print(f"\nThanks for playing the game, {player}!")
        sys.exit()
    if 1 <= value <= 10:
        return value
    return None

secret_number = randint(1, 10)

for i in range(3):
    user_input = check_input(i+1)

    if user_input is None:
        print("Invalid input!\n")  
        continue

    if secret_number == user_input:
        print("Bingo, you guessed it!\n")
        break
    else:
        print("wrong guess!\n")
else:
    print(f"The number was: {secret_number}")

print(f"Thanks for playing the game, {player}!")
