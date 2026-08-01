#Fri Jul 31, 2026

import random
x = int(input("What is the range of the number? 1 - __"))
# Generates an integer from 1 to 10 (can include 1 and 10)
secret = random.randint(1, x)
first_guess = True

while(True):
    if first_guess:
        guess = int(input (f"Guess my number, 1 - {x}. "))
        first_guess = False
    else:
        guess = int(input("Guess my number. "))

    if guess == secret:
        print("Congrats! You Win!")
        break
    elif guess > secret:
        print("The secret number is less than your guess.")
    else:
        print("The secret number is greater than your guess.")
