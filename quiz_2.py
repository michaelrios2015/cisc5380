'''
       Name: Michael Rios 
       Date: 7/27/22
 Assignment: Quiz 2
      class: CISC 5380

write a script that defines and tests function named 
max_3 which requires three positive integer arguments,
say a, b, c and returns teh maxium of the three numbers without sorting then=m.
So for example if in your script the the values are 3, 1, 5, respectively, 
function max_3 should return 5 when tested. Your program must take into account all 
automatic requiremnets discussed in class. within the function you must
not use any structures to store the values other than the variables

the function first assumes i is the larget integer 

if j is larger than it j becomes max(the largest)

then k is tested against that, nice and straight forward 

if any value less then one is entered the user will be prompted to reneter the data

if a real positive number is entered it will be truncated to make a positive integer

if anything else is entered the program will crash

users can choose to run the program again by entering Y or y at the end, they will be 
promoted 


'''

def max_3(i, j, k):

    max = i 

    if max < j:
        max = j
    
    if max < k:
        max = k

    return max

cont = 'y'

while cont == 'y' or cont == 'Y':
# oh i should probably align these ...
    print()
    a = 0
    while a < 1: 
        a = float(input('Please enter your first positive integer : '))

    b = 0
    while b < 1: 
        b = float(input('Please enter your second positive integer: '))

    c = 0
    while c < 1: 
        c = float(input('Please enter your thrid positive integer : '))
    print()

    print('                  a = %6d' %a)
    print('                  b = %6d' %b)
    print('                  c = %6d' %c)
    print('----------------------------------------')
    print('The maxium interger = %6d' %max_3(int(a), int(b), int(c)))
    print()

    cont = input('Enter y or Y to continue any other key to exit: ')
    
    if cont != 'y' and cont != 'Y':
        print()


# 
# the official version 
# def max_3(a, b,c):
#     return max( a, max(b, c))