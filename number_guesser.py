# created by: Wasim

import random

guess = 0

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger then 0 next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)

while True:

    guess += 1

    user_guess = input("Take a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess == random_number:
            print("You got it! :) ")
            break

        else:
            print("You got it wrong!")


    else:
        print("Please a number next time.")
        continue

print("You Got it in", guess, "guesses")







