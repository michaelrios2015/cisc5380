'''
CISC 5380
Michael Rios
HW 4 - Sum of Digits
Due 7/22/22

This program accepts a positive integer greter or equal to 10 
and returns the sum of it's digits

If a floating point number has been entered it will be convereted to an integer

If a non number is entered the program will crash 
'''


def digit_sum(n):

    res = 0

    while n > 0:
        res += n % 10
        n = n // 10

    return res


cont = 'y'

while cont == 'y' or cont == 'Y':

    # input
    n = float(input(
        'Please enter an intger with a value of 10 or higher : '))

    while n < 10:
        n = float(input(
            'Please enter an intger with a value of 10 or higher : '))

    print(digit_sum(int(n)))

    cont = input('Enter y or Y to continue, any other key to quite: ')
