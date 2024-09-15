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
    return ''.join(curr) == secret

# welcome
print('Welcome to hangman! Guess the secret word before the man gets hanged!')
print('\n')

print(f'Word: {''.join(curr)}')
print(f'Lives remaining: {lives}')


while lives > 6 and not has_won():
    pass