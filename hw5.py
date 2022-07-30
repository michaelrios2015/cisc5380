'''
       Name: Michael Rios 
       Date: 8/1/22
 Assignment: Homework 5 
      class: CISC 5380


write a function that creates a 2d list of random integers each in range [0,25]
with random number of rows from [1,6] and a random number of columns from [5,8]

a function that prints the list in the matrix form as we did in class
and a seperate function that prints the maxium intger in the whole 2 d list 
example 

7 9 6 2
1 0 5 12 19
5 6 
4 9 3
13 7 9 5 

The max  = 19

'''

from random import randint


def create_list():

    l = []

    rows = randint(1, 6)

    for i in range(rows):
        l.append([])
        columns = randint(5, 8)
        for j in range(columns):
            number = randint(0, 25)
            l[i].append(number)

    return l


def print_list(l):

    for row in range(len(l)):
        for column in range(len(l[row])):
            print('%5d' % l[row][column], end='')
        print()


def find_max(l):

    max = l[0][0]

    for row in range(len(l)):
        for column in range(len(l[row])):
            if l[row][column] > max:
                max = l[row][column]

    return max


l = create_list()


print()
print_list(l)
print()

print('The max is: %d' % find_max(l))
print()
