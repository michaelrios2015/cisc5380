'''
8/1/22

1 d list ie [1, 13, 5, 7, 2, 9, 6, 4]

p = 8 (ranmodn number)


divide the list in such a way the that you have half smaller then p to the left and elements greater 
then or equal to p are to the right

most not use any other list but l

list does not need to be sorted just divided into the two halves

[1, 5, 7, 2, 6, 4, 9, 13]

so you could go through it if you see something greater than 8 move it to the end 

then subtract one from end and keep going till you meet in the middle

def partion_list(l, p)

no sorting built in alagorithm 

just psuedo code is fine 

you can only loop once

we will talk about it tomorrow

remeber think first then code, you will be stuck without this  
'''

# l = [1, 5, 7, 2, 6, 4, 9, 13]

# p = 8

# start = 0

# end = len(l) -1

# while end > start:
#     if l[start] < p:
#         start += 1
#     else:
#         temp = l[start]
#         l[start] = l[end]
#         l[end] = temp
#         end -= 1

# print(l)

'''

l = [2, -3, 1, 3, 5 , -1, -2]

how do we remove all the negative values

loop through 

'''
# # for loop does not work as we change teh length of the list

# def remove_negatives(l):

#     start = 0
#     end = len(l)

#     while end > start:
#         # print(l[start])
#         if l[start] >= 0:
#             start += 1
#         else:
#             # print(l[start])
#             l.remove(l[start])
#             end -= 1
#             # print(l[start])

#     return l

# l = [2, -3, 1, 3, 7, -6, 5 , -1, -2, 8, 6, 8, -99, -7, 19, -6, -6]

# print()
# print(remove_negatives(l))
# print()

'''
DICTIONARIES -- what I think of hash maps and such 

mutatable, associative data of varible length

daily_temps = { 'sun':62.8, 'sat': 78.9 }

key : value

associative data structure, you need the key to access value  


'''


from multiprocessing.sharedctypes import Value
from random import randint
daily_temps = {'sun': 62.8, 'sat': 78.9 }

# print(daily_temps)

# print(daily_temps[0]) does not work


# this works!!
# you get the value
# print(daily_temps['sun'])

# any immutable data strucre can be used as a key strings, integers, tuples

# interesting
temps = {('Apr', 2, 2001): 43, ('Apr', 7, 2001): 33}

# works fine
print(temps[('Apr', 2, 2001)])

# key error log
# print(temps[('Apr', 2, 2002)])

# creates an empty dictionary
dict()


# so if s is a 2 d list
s = [['apples', 2.24], ['pears', 6]]
# neat!! it takes it in and turns it into a dictionary
d = dict(s)
print(d)

'''

# get the value
d[key] = Value

# delet the value
del d[key]

# get all the keys
d.keys()

# get all the values 
d.values()

# you can change the value 
d[key] = new value 

'''

'''
SET data type

set is mutatble data type with nonduplicet unorderd values providing the usual mathematical set operations

set() - creates an empty set

memebership true or false, is it in the set

add A.add(2)

remove A.remove(2)

union new set with A and B elements

intersection - new set with the common elemnets

difference - opposit intersection I would imagine
'''

# A = {1,2,3}

# B = {3, 4, 5, 6, 7}

# # print(A | B)

# # nifty!!
# print( A- B)

# print( B - A)

# # symetric difference


# # (A -B ) | (B - A)
# # cool!!
# print(A.symmetric_difference(B))

# # just like normal
# len(A)

# # very useful for math problems

'''

fronset ---- hmm

same as set but you cannot change the elements 

everything else is the same interesting 

list is the most import data structure - everything else is made from that 

we are not getting into object oriented programming -- don't have time 

but everything else has been covered 

so for tomorrow we will go over a bunch of list problems, this should be what the final is like

we try and then go over it as a group :) 

final exam - one program 2 hours should be relatively simple 


create a 2d matrix  and see if it is symytric 

0 7 1 6
7 0 2 5
1 3 2 4
6 2 1 5

flip row and column and they should be the same so [1, 0] = [0, 1]
[1,1 ] and such do not matter 


we will use a while loop so we can break if it is not symmetric
'''


def create_matrix():

    n = randint(2, 5)

    l = []

    # slightly better at least for this class
    for i in range(n):
        # l.append([])
        row = []
        # so build the entire row
        for j in range(n):
            row.append(randint(0, 5))
        # then attach them
        l.append(row)

    return l


l = create_matrix()

print(l)

#


def symetric_matrix(l):

    # we just assume it's true
    symetric = True

# start at row 0
    row = 0

    # so I woul have just done two for loops with 2 return statements
    # but that is not how it is supposed to be done at least in this class

    # we assume it is symteric
    # while it has not priven to be asymetric and we have
    while symetric and row < len(l):
        # that's clever!! we just need to check half
        col = row + 1
        while symetric and col < len(l[0]):
            # we don't need to check [0][0], [1][1], they are on the dignol with no corresopneding checky things
            if row != col:
                # otherwise we check and if they don't equal each other
                if l[row][col] != l[col][row]:
                    # it's not symateric
                    symetric = False
            # iterate col
            col += 1
        # iterate row
        row += 1

    # so if we made it through symetric is still tru if not it's fasle
    return symetric


#
l = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
print(symetric_matrix(l))

if symetric_matrix(l):
    print
