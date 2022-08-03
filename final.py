'''

       Name: Michael Rios 
       Date: 8/3/22
 Assignment: Final 
      class: CISC 5380

1) Accepts from the keyboard a length of n of a list
    The list leng should be in a value in range [10,20]

    this program will accpet any real number between 10-20 if a non integer is entered the number will be truncted to make an integer

    if a non number is entered the program will crash

2) Defeines function create_list(n) that creates a list of length n of random integers each integer in a list in range [3,8]

3 - 7 what is on the assignmment sheet

this program will also allow the user to run it more than once, I like doing it and it makes it easier to test

I turned the comparsion script into a function, it can only compare two list of teh same length, if they are of differnt lengths it will crash

The functions are all at the top becuase I think that is considered easier to read but I may be wrong

'''

from random import randint

def create_list(n):

    l = []
    for i in range(n):
        l.append(randint(3,8))
    
    return l

def print_list(l):

    for i in range(len(l)):
        print('%3d' %l[i], end = '')
    print()

def compare_lists(l1, l2):
    common = []

    for i in range(len(l1)):
        if l1[i] == l2[i]:
            common.append(i)
    
    return common

cont = 'y'

while cont == 'y' or cont == 'Y':

    print()
    n = 0
    while n < 10 or n > 20:
        n = float(input('Please enter list length between 10 and 20: '))

    n = int(n)

    list_1 = create_list(n)
    list_2 = create_list(n)

    print()
    print('list_1: ', end = '')
    print_list(list_1)
    print('list_2: ', end = '')
    print_list(list_2)
    print()

    common = compare_lists(list_1, list_2)

    if not common:
        print('There are no positions having the same value')
    else:
        print('Common positions are:', end = '')
        print_list(common)
    print()

    cont = input('Enter Y or y to continue any other key to exit: ')
    
    if cont != 'y' and cont != 'Y':
        print()