# number guessing game

import random

# function for darwing a number between 0 and 100

def guessing_game():
    x = random.randint(0,100)
    return x

number = guessing_game()

# first user try to guess the number

while True:
    print("Guess the number between 0 and 100:")
    user_guess = input()
    try:
        user_guess = int(user_guess)
        break
    except:
        print("Please type an integer!")

count = 1

min = 0
max = 100

# check if the user's guess is too low/high or just right

while True:
    if user_guess > number:
        if user_guess < max:
            max = user_guess
        print(f'Too high! Guess the number between {min} and {max}:')
    if user_guess < number:
        if user_guess > min:
            min = user_guess
        print(f'Too low! Guess the number between {min} and {max}:')
    if user_guess == number:
        if count == 1:
            print("Just right! You guessed in " + str(count) + " try! Thanks for playing!")
            break
        else:
            print("Just right! You guessed in " + str(count) + " tries! Thanks for playing!")
            break
    while True:
        user_guess = input()
        try:
            user_guess = int(user_guess)
            count += 1
            break
        except:
            print("Please type an integer!")
