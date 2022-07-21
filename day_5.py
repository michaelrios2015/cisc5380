# 7/20/22

# quizes!!

# Test(quiz) 1 - 07/25 - loops!!
# step one which type of loop
# ------------------------------------
# use for loops for know counting
# use while for only condition 

# step two
# make sure you understand what teh program is supposed to do
# ask questions - we will have time before teh quiz
# take a moment to think about what you need to do and how to do it 

# Test(quiz) 2: 7/27 - Functions, loops will probably still be there

# review:

# assignment statements

# expressions - Boolean and otherwise
# hiearchy and such 
    # operations
    # basic built in functions
    # precidents (heiarchy)

# Boolean expressions

# above should be fin for the first part

# below and above should be the second one
# the final will be like these 

# modules - importing 
# import all the module, import just a function

# review all the problems and homeworks
# write lots of code :)

# you can use notes, textbooks, internet 

# always format the output!!

# and choose the proper loop 

# n = 15

# how do we check for n is o or positive

# # this is what it ideally look like
# '''
#       Name: 
#       Date: 
# Assignment: 
# '''

# n = int(input("please enter a natural number: "))
# while n < 0:
#     n = int(input("please enter a natural number: "))

# total_sum = 0

# for i in range(1,n+1):
#     total_sum += i*i*i

# print()
# # print("the sumation of %d^3 = %d \n" %(n,total_sum))


# generate a random number in range [0,1)
# for as long as the generated number is less then 0.69

# from random import random

# upper_limit = float(input('please ener an upper limit [0,1): '))
# while upper_limit >= 1 or upper_limit < 0:
#     upper_limit = float(input('please ener an upper limit [0,1): '))

# r = 0
# counter = 0

# while r < upper_limit:
#     r = random()
#     if r < upper_limit:
#         print(r)
#         counter += 1
#     else:
#         print("%f, broke the loop" %r)
#         print('we had %d random number(s) before reaching one above %f' %(counter, upper_limit))


# # this type opf formating is what is desired :)
# import random

# r = 0
# # always better to 
# limit = 0.69

# print()
# while r < limit:
#     r = random.random()
#     print('%12.5f' %r)

# print() 

# write a program that inputs sides a,b,c of a triangle 
# a + b  > c and a + c > b and b + c > a

# input a, b , and c

# while a + b < c or a + c < b or b + c < a
# input c
# # 
# print()
# a = float(input('Side one of the triangle: ')) 

# b = float(input('Side two of the triangle: ')) 

# c = float(input('Side three of the triangle: '))

# # negation of the a + b > c
# while a + b <= c or a + c <= b or b + c <= a:
#     c = float(input('you Side three of the triangle: '))

# print()
# print('a = %12.7f' %a)
# print('a = %12.7f' %b) 
# print('a = %12.7f' %c)   

# write a progarm thar outputs a number 

# in the middle between Sqrt(2) and Sqrt(3)

# with the accaruy of .0001

# using a random 

# from random import random

# target = (2**.5 + 3**.5)/2

# # print(target)
# # 1.5731321849709863
# r = random() * 10

# # so this keeps us going unti r 
# while r > target + .001 or r < target - .001 :
#     r = random() * 10
#     # print(r)
# print()    
# print(r)
# print()

# the official 
from math import sqrt
from random import random

accuracy = .00001

guess = 0

while abs( guess - (sqrt(2) + sqrt(3))/2) > accuracy:
    guess = 2*random()

print()
print('Guess = %2.7f' %guess)    
print()

# practice problems for test 1
# write a program that enters a radius R of a big circle and uses a loop to find
# radius r of a circle with the area half of the cirle of radius R

# so user eners 

# given a sequence of squares in which the first square has side two and each consequatib=ve 
# square in the sequence has teh side which is half of the side of the previous square in 
# the sequence. how mant square  are needed for the sum of the areas of all squaressequence to be 
# at most 6