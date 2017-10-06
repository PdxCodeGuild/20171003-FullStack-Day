"""
Lab 13: Guess the Number
1) the computer will pick a random number between 1 and 10
2) the user will try to guess that number
3) if the guess is correct, tell the user "that's correct!"
4) otherwise, tell the user "that's incorrect!"

step 2
compare the target and guess
if the target is greater than the guess, print 'higher'
otherwise, print 'lower'
"""

import random

target = random.randint(1, 10)

last_guess = None

n_guesses = 0


def calc_distance(target, guess):
    return abs(target - guess)

while True:
    guess = int(input('guess the number! '))
    if guess == target:
        print('that\'s correct!')
        break
    else:
        print('that\'s incorrect!')

    #if target > guess:
    #    print('guess higher!')
    #else:
    #    print('guess lower!')

    if last_guess is not None:
        d_guess = calc_distance(target, guess)
        d_last_guess = calc_distance(target, last_guess)
        if d_guess < d_last_guess:
            print('closer')
        elif d_guess == d_last_guess:
            print('you\'re the same distance away')
        else:
            print('further')

    print('guess: ' + str(guess))
    print('last guess: ' + str(last_guess))

    last_guess = guess

    n_guesses += 1

print(f'You guessed {n_guesses} times!')
