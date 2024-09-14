# 100 days of code: day 4
# single play rock paper scissors

import random

# ascii art array
art_array = ["    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)", "    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)", "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"]


if __name__ == '__main__':
    
    # start the game
    print('Let\'s play rock paper scissors!')

    # get inputs
    player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

    computer_choice = random.randint(0,2)

    # display choices
    print(art_array[player_choice])
    print('\nComputer chose: \n')
    print(art_array[computer_choice])

    # proccess the inputs and get winner
    # this method only works since rock is at index 0 paper is at index 1 and scissors at index 2. This way each counter is 1 index ahead and each win condition is 1 index behind.
    x = player_choice - computer_choice
    res = ''
    if x > 0:
        res = 'You win!'
    elif x == 0:
        res = 'It\'s a tie.'
    else:
        res = 'You lose'

    print(f'\n{res}')