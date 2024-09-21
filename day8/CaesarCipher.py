# 100 days of code: day 8
# Caesar cipher program

def encrypt(message, x):
    '''
    Takes in two parameters: a string (message) and integer x
    returns a string with ceasar cipher encryption on message based on x
    '''
    encrypted_message = ''

    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message = encrypted_message + chr((ord(char)-97 + x)%26 + 97)
            else:
                encrypted_message = encrypted_message + chr((ord(char)-65 + x)%26 + 65)
        elif char.isdigit():
            encrypted_message =  encrypted_message + chr((ord(char)-48 + x)%10 + 48)
        else:
            encrypted_message = encrypted_message + ' '

    return encrypted_message

def decrypt(message, x):
    '''
    Takes in an encrypted string
    and returns its decrypted form based on x
    '''
    decrypted_message = ''

    for char in message:
        if char.isalpha():
            if char.islower():
                decrypted_message = decrypted_message + chr((ord(char)-97 - x)%26 + 97)
            else:
                decrypted_message = decrypted_message + chr((ord(char)-65 - x)%26 + 65)
        elif char.isdigit():
            decrypted_message =  decrypted_message + chr((ord(char)-48 - x)%10 + 48)
        else:
            decrypted_message = decrypted_message + ' '

    return decrypted_message




if __name__ == '__main__':

    running = True

    while running:
        user_choice = input('Enter e to encrypt a message and d  to decrypt and q to quit')

        if user_choice == 'e':
            message = input('Enter you message')
            offset = int(input('Enter a number'))
            em = encrypt(message, offset)
            print(f'encrypted message: {em}')
        elif user_choice == 'd':
            message = input('Enter you message')
            offset = int(input('Enter a number'))
            dm = encrypt(message, offset)
            print(f'decrypted message: {dm}')
        elif user_choice == 'q':
            print('Thank you! Goodbye!')
            running = False
        else:
            print('Please enter one for the following options')
    

        