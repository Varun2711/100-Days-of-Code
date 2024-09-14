# 100 days of code: day 3
# Treasure Island text rpg using basic control flow (no loops)

if __name__ == '__main__':
    

    # print welcome
    print('Welcome to treasure island!\nYour mission is to find the treasure.')

    # start the game and ask for direction from cross road.
    direction = input('You\'re at a cross road. Where do you want to go?\n\t\t Type "left" or "right"\n')

    if direction == 'left':
        # next choice
        decision = input('You\'ve come across a lake. There is an island in the middle of the lake\n\tType "wait" to wait for a boat. Type "swim" to swim across\n')

        if decision == 'wait':
            # final choice
            door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')

            if door == 'yellow':
                print('You found the treasure! You win!')
            elif door == 'red':
                print('It\'s full of fire. Game over.')
            elif door == 'blue':
                print('You got eaten by beasts. Game over.')
            else:
                print('The entity sensed your presence and attacked you. Game over.')
        else:
            print('You were attack by a trout. Game over.')
    else:
        print('You fell into a hole. Game over.')