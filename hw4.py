'''
CISC 5380
Michael Rios
HW 4 - Sum of Digits
Due 7/22/22

This program accepts a positive integer greter or equal to 10
and returns the sum of it's digits

If a floating point number has been entered it will be convereted to an integer

If a non number is entered the program will crash

The program will continue until the user enters a character other than y or Y to exit
'''

# our


def digit_sum(n):

    res = 0

    while n > 0:
        res += n % 10
        n = n // 10

    return res


cont = 'y'

# a while loop that lets the user run the program more than once
while cont == 'y' or cont == 'Y':

    # input
    print()
    n = float(input(
        'Please enter an intger with a value of 10 or higher : '))

    # this makes sure we get a number of 10 or above
    while n < 10:
        n = float(input(
            'Please enter an intger with a value of 10 or higher : '))

    # output
    print()
    print('the sum of the digits in: %6d' % n)
    # print('%3d' % n)
    print('                      is: %6d' % digit_sum(int(n)))

    print()
    cont = input('Enter y or Y to continue, any other key to quite: ')
