# 7-13-22

# nested if statement --- for this class use this professor thinks it is easier yo mess up 
# if condation:
#   statement
# else:
#   if condition:
        # statements
#   else:
#       if condition:
        # etc, etc


# elif else if
# if grade >= 90:
#     print("grade = A")
# elif grade >= 80:
#     print(grade b)
# # ect
# else:
#     print(grade f)


# write a script that takes in input three coeffecients of quadratic eqgaction 
# ax^2 + bx + c = 0

# output real roots of the equation

# test if a = 0, because it is not quadratic then 
# print not a quadratice equation and do nothing else 
# 
#  check if b^2 - 4 * a * c is zero or positive
# if it is less then zero print no real roots

# # otherwise compute and output roots :)
# a = float(input('Enter value of a: '))
# b = float(input('Enter value of b: '))
# c = float(input('Enter value of c: '))


# # a = 1
# # b = 0
# # c = 0

# if a == 0:
#     print("this is not a quadratic equation")
# else:
#     temp = b**2 - 4 * a * c
#     if temp < 0:
#         print('no real roots buddy')
#     else: 
#         r1 = (-b + temp ** .5)/2/a
#         r2 = (-b - temp ** .5)/2/a
#         print("root one is %f" %r1)
#         print("root two is %f" %r2)

# iterative control - loop de loop

# while statement

# while condition:
#   Suite-- interesting did not knwo it had a name
# 

# i = 0

# while i < 10:
#     print(i)
#     i += 1

# you want to avoid the infinite loop 
# like if we did not update i
#  i = 0
# this is an infinite loop
# while i < 10:
#     print(i)


# while loops are usually used when you don't know the number of repations

# sum = 0
# current = 1

# while current <= n:
#     print('%3d     %3d' %(sum, current))
#     sum = sum + current
#     current = current + 1



# for loop --- when you know the number of repitations

#  for variable in <sequence>

# for num in [2, 3, 4]:
#     # so we get it all on one line
#     print(' %3d ' %num, end = '')
# print()

# Boolean Flags and indefinite loops

# so done needs to be true or false 

# while not done
#   print(' please repeat')

# done = False

# while not done:
#     done = int(input('enter done: '))
#     print('done = %d' %done, end = ' ')

# range

# for num in range(10, 2, -2):
#     print(num)

# python always uses half open interval [10, 2)
#  so we want 10 not 2 [ yes ) no

# l = list(range(10,2,-2))

# print(l)

# range (start, end, step), end is never included 
# when start and step are left out they are assumed to be 0 and 1
# write a script that prints 10 random values one per line
# each randmo number in range of [0, 1)
# from random import random

# # i, j, k are used becaus ethey represent real numbers or possibly just
# # custom
# for i in range (10):
#     print('%3d     %10.6f' %(i, random()))

# from random import random

# total = 100000

# nc = 0

# for i in range (total):
#     x = random()
#     y = random()

#     if x**2 + y**2 < 1:
#         nc += 1
# pi = 4 * nc/total

# print()
# print('pi is apprimately %10.8f' %pi)
# print()

# write a program in unit square until the we get a point with length greater
# then 1.1
# the output number of points

# from random import random
# from math import sqrt 

# points_generated = 0

# limit_distance = 1.4
# stop = True

# x = random()
# y = random()


# while sqrt(x**2 + y**2) < limit_distance:
#     x = random()
#     y = random()
#     points_generated += 1
        

# print()
# print('for limit distance %f' %limit_distance)
# print('we generated %d points' %points_generated)
# print()

# homework 3 that accepts from the keyboard 
# the intail height h and the bouncing ratio r and outpouts the 
# total distance traveled by the ball untill it stops

# make sure height is positive

# h = float 

# bouning ratio is how h=high it bounces

# so we drop ball from height h and it bounces h * r

# h + 2(h*r) + 2* h*r*r..... so while h is not zero
# 
# out h and r 2 decimal points and so maybe a float with 6.2
# 
# bouncing ratio most be between 0 and less than 1
# 
# monday  