import random
from utils import *

def play_game():
    print("Starting a new round...")
    # generate a random target, and remember this target
    TARGET = random.randint(1, 100) # 1 <= target <= 100
    print("A random integer between 1 and 100 (both inclusive) is generated")
    # let the user keep guessing until right (while)
    while True:
        # ask for the guess
        user_guess = input("Please take a guess: ").strip() # strip(): clean the white space at the beginning and end of a string
        # make sure the user input is a number
        if not user_guess.isdigit():
            print("Invalid guess: you should enter a number")
            continue
        user_guess = int(user_guess)
        # verify the guess
        # if guess is correct -> break out of the loop
        if check_guess(user_guess, TARGET):
            break
