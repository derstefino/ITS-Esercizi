'''
2. Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.

'''

import random

def random_number() -> None:

    start = int(input("from: "))

    end = int(input("to: "))

    extract = random.randint(start, end)

    attempts = 0

    while attempts < 5:

        guess = int(input("try guessing what number came out: "))

        if guess < extract:
            print("too low!")
            attempts +=1
        elif guess > extract:
            print("too high!")
            attempts +=1
        else:
            print("correct!")
            break

        if attempts==5:
                print("ran out of attempts!")



random_number()
