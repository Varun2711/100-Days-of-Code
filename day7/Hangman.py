# 100 days of code: day 7
# hangman

import json
import random

# words dictionary is from the following github repo: https://github.com/dwyl/english-words

# game variables
words = {}
lives = 6
secret = ''
guesses = [] # letters guessed


# get  words
with open('./words_dictionary.json') as f:
    words = json.load(f)

# initialize the secret word
secret = random.choice(list(words.keys()))
curr = ['_']*len(secret) # current state; initialized all positions to blank

# check for winner
def has_won():
    '''
    Return true if the word has been guessed correctly
    else return false
    '''
    return ''.join(curr) == secret

# display game state:
def display_state():
    '''
    display the current game state: print out how much of the
    word has been guessed and the remaining number of lives and letters used
    '''
    print(f'Word: {''.join(curr)}\n')
    print(f'Lives remaining: {lives}')
    print(f'Letters used: {guesses}')


# get letter guess:
def get_guess():
    '''
    get a letter guess from the user; and return that character
    '''

    guess = ''

    # only return after validating input
    while not guess:
        try:
            guess = input('Enter your guess: ')

            if not guess.isalpha():
                raise TypeError
            elif len(guess) > 1 or guess in curr:
                raise ValueError
            
        except TypeError:
            print('Please enter a letter from the alphabet')
        
        except ValueError:
            guess = ''
            print('Please enter a single letter from the alphabet that has not been used')

    return guess
    


# welcome
print('Welcome to hangman! Guess the secret word before the man gets hanged!')
print('\n')

while lives > 0 and not has_won():
    display_state()

    guess = get_guess()

    if guess in secret:
        
        for i, char in enumerate(secret):
            if guess == char:
                curr[i] = guess
    else:
        lives -= 1

    guesses.append(guess)


if has_won():
    print('You win!')
else:
    print(f'Game over. The correct word was: {secret}')
