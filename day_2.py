# # import imp


# # print('Compute N = k*p*n')

# # # input
# # k = float(input('Enter value of k: '))
# # p = float(input('Enter value of p: '))
# # n = float(input('Enter value of n: '))

# # N = k*p*n

# # # One number per line output with labels
# # # out put
# # print('k = ', k)
# # print('p = ', p)
# # print('n = ', n)
# # print('N = ', N)

# # now we learn formating

# # seems like a little description is not bad

# # formating
# import math

# it = 41

# y = 112.333

# print('xhsjxhs %4.3f' % math.pi)


# print('djfkjfh %d sjdsajdkl %f' %(it, y))
# # %(it, y) this is needs to the same order as you have in your print statement

# # %d for int %f or float

# # %5d for 5 spaces %5d for right justififed %-5d for left justifed, decimal character counts as columns

# # %+5d includes plus or negative sign

# # %020.2f the first zeo pads your number with leading zeros

# # %10.2f (the . is for numbers after decimal point)

# # %10

# # formating is important for this class.. so practice :)

# a = 3
# b = 6
# c = 8

# print('a = %3d b = %-3d c = %d' %(a,b,c))

# # so for us all out put shoudl be one variable per line and lined up by decimak point

# a = 12.3
# b = 0.009
# # note how we added teh number of digits to get the maxium amount
# print('a = %6.3f' %a)
# print('b = %6.3f' %b)

# so for us we will

# quad.py

# enter a, b, c from keyboard

# output 2 roots of the quadratic equation

# ax^2 +bx + c =0

# -b

# 5 outputs all alligned by = and .

# class exercise 1 - 7/11/22
# solves a simple quadratice equation
# start with simple script

# print()
# a = float(input('Enter coefficient a: '))
# b = float(input('Enter coefficient b: '))
# c = float(input('Enter coefficient c: '))
# print()

# a = 1
# b = -3
# c = 2

# temp = (b**2 - 4 * a * c)**.5

# # so this is just a trick of order of operations calculat the top first divid it by 2 then divide that by a
# # I find it hard to read but it will run slightly faster
# r1 = (-b - temp) / 2/a


# r2 = (-b + temp) / (2 * a)

# # print('a  = %+5.3f' %a)
# # print('b  = %+5.3f' %b)
# # print('c  = %+5.3f' %c)

# # print('r1 = %+5.3f' %r1)
# # print('r2 = %+5.3f' %r2)

# # that looks better so you want to give enough spaces to reasonably accomodate
# print(' a = %8.2f' %a)
# print(' b = %8.2f' %b)
# print(' c = %8.2f' %c)

# print('r1 = %8.2f' %r1)
# print('r2 = %8.2f' %r2)
# # professor likes these empty lines
# print()

# print(r1)
# print(r2)


# control flow

# boolean expressions
# don't use predefinied variables such as float you can see with (__builtins__) help() q for quite

# relational operators
# ==
# !=

# logical (boolean) operators
# this is the hieracy
# not,
# and,
# or

# (2+3) > (7+6)
# is the same as
# 2+3 > 7+6
# profesor is into the heirachy of operations

# 1 < num < 10 is OK IN PYTHON???
# every other langauge needs a and statement
# Still better to use the and statement

# short circuit (lazy) Evaluation
# if n != 0 and 1/n < tolerance
# so we can get away with this becasue the in n = 0 we don't go on to the second part neat

# to be safe you would
# if n !=0:
#   if 1/n < tolerance:

# selection control

# if statement

# if <condition>: -- header
#   statemet -- suite
# else:
#   statement

# header + suit is clause

# if else only one will be done

# you can have just an if statement no else

# identation - big in pythin yes yes they are

# take in a, b, and c is it a triangle
# sum of any two side are bigger than the third

# out all the inputs and the area answer should be to 7.3 format

# get inputs
# empty line
# output
# empty line

# pretty

# print()
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))
# print()


import math
a = 3
b = 4
c = 5

print('is ', end=' ')
if a + b > c and b + c > a and c + a > b:
    # print(a)
    # print(b)
    # print(c)
    print("", end=' ')
else:
    # print(a)
    # print(b)
    # print(c)
    print("not ", end=' ')
print('a triabgkle')
print('the end')

# so even message redunandecs should be take care of... sure

# hw2 - 07/13
# write a program that accepts Values

# a, b, c from the keyboard

# and outputs the area triangle if it is a traingle
# and not a trianle if not

# p = (a+b+c)/2

# A = sqrt(p(p-a)(p-b)(p-c))
# '''
# dsjlkfjlasdkjf block comment??
# did not work for me...
# '''

# printing_codes_2.py
# Experiments with print command
# it =  input('Enter integer: ')    dziala
# y =  input('Enter float: ')       dziala
# from __future__ import print_function

# from __future__ import print_function
# It looks like this statement must be the first
# of the import statements (beginning of the file )


it = 41
y = 123.456789

# from the class notes
"""
print( '0. The value of PI is approximately %5.3f.' % math.pi ) 
# the above statement without () is now an error )
print( "1. After iteration.", it, "the solution was.", y )
print( '2. After iteration. %d, the solution was. %f.' %(it,y) )
print( '3. After iteration. %5d, the solution was. %3.1f.' %(it,y) )
print( '4. After iteration. %-5d, the solution was. %10.2f.' %(it,y) )
print( '5. After iteration. %+5d, the solution was. %-10.2f.' %(it,y) )
print( '6. After iteration. %+-5d, the solution was. %+10.2f.' %(it,y) )
print( '7. After iteration. %05d, the solution was. %020.2f.' %(it,y) )
print( '8. After iteration. %05d, the solution was. %10.2e.' %(it,y) )
"""

# hiearc
Prof. Strzemecki

()
** exponentiation            right-to-left
- negation                   left-to-right
*, /, //, %                  left-to-right
+, -                         left-to-right
    <, > , <= , >= , != , ==         left-to-right
    not left-to-right
    and left-to-right
    or left-to-right
