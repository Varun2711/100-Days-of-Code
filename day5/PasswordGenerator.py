# 100 days of code: day 5
# password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    res = ''

    while nr_letters > 0 or nr_numbers > 0 or nr_symbols > 0:
        char_choice = random.randint(0,2) # 0: enter letter, 1 enter number, 2 enter symbol

        match char_choice:
            case 0:
                if nr_letters > 0:
                    res = res + random.choice(letters)
                    nr_letters -= 1
            
            case 1:
                if nr_numbers > 0:
                    res = res + random.choice(numbers)
                    nr_numbers -= 1

            case 2: 
                if nr_symbols > 0:
                    res = res + random.choice(symbols)
                    nr_symbols -= 1

    print(f'Your password is {res}')

        
        

