# 100 days of code: day 9
# Secret Auction program


def get_bidders():
    bidders = {}

    choice = ''
    while choice != 'no':
        name = input('What is your name: ')
        
        n = 0
        while n == 0:
            try:
                n = int(input('Enter the amount you wish to bid $'))
                bidders[name] = n
            except TypeError:
                print('Please enter an amount >= $1')

        choice = input('Are there any other bidders? (enter yes or no) ')


def main():
    bidders =  get_bidders()

    winner = ''
    winning_bid = -1

    for bid in bidders.items():
        name, amount = bid
        if amount > winning_bid:
            winner = name
            winning_bid = amount

    print(f'{winner} has won the auction with a bid amounting to ${winning_bid}')



if __name__ == '__main__':
    main()