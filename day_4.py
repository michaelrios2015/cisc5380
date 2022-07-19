# 7/18/22

# going over the homework

# add documentation to the program at the beginning, starting with name, date and such 

# Input statements, we can now use while statemets

# import sys

# h = float(input("enter intial height: "))

# # check the input valuses
# while h <= 0:
#     h = float(input("pleaase reenter intial height, needs to be positive: "))
# r = float(input("enter the ratio: "))
# while r <= 0 or r >=1:
#     r = float(input("reenter ratio (0<r<1): "))

# # so to test just print the values and make sure it is ok
# # print(r)

# distance_traveled = h

# new_height = h

# # I did not know about sys.float_info.min.. very interesting 
# while new_height > sys.float_info.min:
#     new_height = new_height * r
#     distance_traveled += 2* new_height
#     print('%20.18e, %new_height')
#     # apperently this is a python 2 thing
#     # raw_input('Press <enter> to continue')

# print(distance_traveled)
# # 
# # apperently using power to is costly in terms of computer time.. interesting 

# import sys

# n = 1

# total = n

# new_n = n
# # doing this with brute force takes forever
# # while new_n > sys.float_info.min:
# while new_n > .0001:

#     n = n +1 
#     # print(n)
#     new_n = (1/n)

#     total += new_n
#     # print(new_n)
# print(total)

# import sys

# n = 1
# term = 1
# sum = term

# while term > sys.float_info.min and n < 10000:
#     term = 1/(n+1)
#     sum += term
#     n += 1

# print(sum)    

# quizes monday - 7/25 wednesday -7/28 

# sumation series

# take in n as a keyboard from keyboard
# 
# take in x from keyboard 
# 
# 1 + x + x^/2! + + x^3/3! +.... x^n/n!
# 

# for i in range(10):
#     print('%3d' %i) 

# for i in range(2, 10):
#     print('%3d' %i) 

# so it's this easy in python
# s = 'hello'

# for c in s:
#     print(c)

# import random 

# for i in range(10):
#     print('%6.4f' %random.random())

# now print random int 0 - 10
# import random 

# for i in range(10):
#     # randint range is inclusive 
#     print('%d' %random.randint(0,10))

# write a program that generaes and prints 10 random intgeres each in range 0-5
# and ouputs the number of integers gretare than two

# import random 

# counter = 0

# for i in range(10):
#     # randint range is inclusive
#     value =  random.randint(0,5)
#     print('%d' %value)
#     if value > 2:
#         counter += 1
# print("%d are great than 2" %counter)

# functions!!!

# def <function name>([<parameters>]): <- function header
# <statement> <- Suite (function body)
# 
# you don't need to have parameters
# 
# function first needs to be defined then it can be used
# 
# if your function returns a value use retur 

# we can use functions now

# def avg( n1, n2, n3 ):
#     return (n1 + n2 + n3)/3.0


# print('average is: %6.4f' %avg(3,4,7))

# def a function sum(n) that computes 1+ 2 + 3...+ n
# where n is a posit integer entered from the keyboard 

# so there might be a predfined function called sum but ours will take precident 
def sum(n):

    total = 0
# 
    for i in range(1,n+1):
        total += i

    return total
# we are not dealing with bad 
# a function should just do one thing so we want the input outside :)
n = int(input("please enter a poisive intger: "))
while n <= 0: 
    # n = int(input("please enter a poisive intger: "))
    n = int(input("please enter a poisive intger: "))

# print('sum = %d' %sum(n))

# so we could take the numbers in as float and then cast it as int them so if we 
# got 3.8 we then do sum(int(n)) so we send 3 or round 

# so we are starting to deal with bad data but have not jumped to what to do 
# if someone eneters a string instead of a digit 

# n = k * q + r

# 0<= r < q - remander 

# q = quient

# k = the max integer such that k * q <=n

# 7= 2*3 +1

7%2

7//2

15//3

15%3

# homework 4 due friday the 22 
# wite a function digitr sum of n where n is a positive integer > 10 entered from
# the keyboard and outputs the sum of the digits of n

# for example
# digit_sum(32) = 5
# digit_sum(1276) = 16

# vortex math?? -- where 9 * 9 always equals 9 