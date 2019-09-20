# https://realpython.com/python-random/

import random

secret = random.randint(0, 100)
win = False

for i in range(0, 5):
    guess = int(input("Guess a number: "))
    if guess == secret:
        win = True
        break
    elif guess > secret:
        print("Too hugh")
    else:
        print("Too low")

if win:
    print("You win!")
else:
    print("You lose!")
