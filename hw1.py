# CISC 5380
# Michael Rios
# HW 1
# Due 7/11/22

# so we ask for the number

# a helper function so we know if we got a number
def isanum(x):
    try:
        # if it can be made into a float
        float(x)
        # it's true
        return True
        # if not it's not a number
    except:
        return False


title = ' PROGRAM MULTIPLE '
subtitle = ' for multiplying 3 numers '

# print('*************PROGRAM MULTIPLE***************')
print(title.center(40, '*'))
print(subtitle.center(40, '*'))


k = input("Please eneter your first number: ")

# we start a while loop
while not isanum(k):

    print('Sorry ', k, ' is not a number')

    k = input("please enter your first number: ")

k = float(k)


n = input("please eneter your second number: ")

while not isanum(n):

    print('Sorry ', n, ' is not a number')

    n = input("please enter your second number: ")

n = float(n)


p = input("please eneter your third number: ")

while not isanum(p):

    print(f'Sorry {p} is not a number')

    p = input("please enter your third number: ")


p = float(p)

# print(f'{k} * {n} * {p} = {k*n*p}')

print(f'{k:10}')
print(f'{n:10}')
print(f'X{p:9}')
print('-----------------')
print(f'{k*n*p:10}')
