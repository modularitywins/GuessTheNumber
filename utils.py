def check_guess(guess, target):
    if guess < target:
        print("Your guess is too small")
        return False
    elif guess > target:
        print("Your guess is too large")
        return False
    else:
        print("Your guess is correct")
        return True
