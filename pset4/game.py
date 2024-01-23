import random
import sys

def main():
    while True:
        # ask to the user a positive number: n
        try:
            n = int(input("Level: "))
            # check if n is positive
            if n > 0:
                # generate a random number between 1 and n: guess
                s_guess = random.randint(1, n)
                guess(s_guess)
                break
            else:
                continue
        except ValueError:
            continue


def guess(s_guess):
    while True:
        try:
            # ask to the user what can be the guess number
            u_guess = int(input("Guess: "))
        except ValueError:
            continue
        else:
            # check if guess is positive
            if u_guess > 0:
                # check if n and guess are the same number or not
                if u_guess == s_guess:
                    print("Just right!")
                    sys.exit()
                elif u_guess > s_guess:
                    print("Too large!")
                    continue
                elif u_guess < s_guess:
                    print("Too small!")
                    continue


main()
