# 100 days of code: day 2
# Tip Calculator project

if __name__ == '__main__':
    # print out introduction
    print('Welcome to the tip calculator!')

    # ask for the bill
    bill = float(input('What is the total bill? $'))

    # get tip percentage; multiplying by 0.01 is the same as dividing by 100
    tip_percent = int(input('How much tip would you like to give? 10, 12 or 15? ')) * 0.01

    # get the number of people splitting the bill
    num_people = int(input('How many people splitting the bill? '))

    # calculate tip, total and cost per person
    tip = bill * tip_percent
    total = bill + tip
    cost_per_person = total/num_people

    # display results
    print(f'Each person should pay ${cost_per_person:.2f}')

