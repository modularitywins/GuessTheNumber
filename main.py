from game import *

def main():
    print("Welcome to Guess the Number")
    play_game()
    while True:
        user_input = input("Do you want to play another round [y/n]: ")
        if user_input.lower() == "n":
            break;
        play_game()
    print("We are done with this game. Exiting...")

main()
