# quizes monday - 7/25 wednesday -7/28

# sumation series

# take in n as a keyboard from keyboard
#
# take in x from keyboard
#
# 1 + x + x^2/2! + + x^3/3! +.... x^n/n!


# so in theory this is x^n/n1 from 0 to whatever number is entered
# but the program will run slight;y faster is we don't use ** and probably whatever math function in factorial

# since a the numbers of repitations is entered we definitly want to use a for loop

'''
so in theory it's 

for i range n+1
x^n/n!

but I will skip the for loop for the 0 entry and start at 1

so the prooblem is not explaided terribly well but I think it is safe to assume my interpreation is correct 

'''
# # n is probably supposed to be 1 or higher
# n = 0
# while n < 1:
#     n = int(input('please enter the number of times to sum n >= 1: '))

# x = 0
# while x <= 0:
#     # I assume it would need to above zero though that should be asked
#     x = float(input('please enter the number to sum  x > 0: '))


# # we will calculate this ourselves
# fact = 1

# x_thpo = x

# # since we never do n = 0 in the loop we start with sum at 1
# sum = 1

# for i in range(2, n+1):
#     # so here we add to the sum as indicated by the formula
#     sum += x_thpo/fact

#     # so here is the problem if we start at i = 1 we will get fact = 1 when it should equal 2
#     # so we will start with i = 2 and go to n + 1
#     fact = fact * i

#     x_thpo *= x

# print(sum)


#    Assignment: Write a script that accepts from the
#                keyboard a radius R of a circle, and uses a
#                loop to find the radius r of a circle with
#                the area half of the circle with radius R
'''
so if we fully write out the equation we get big_r/sqrt(2) == lil_r

but we are just going to start from zero and slowly increase lil_r till lil_r ^ 2 = big_r ^ 2/2

because we are testing the while loop, and it will be a while loop since we do not know how many times we need to do it


'''

# big_r = 0
# while big_r <= 0:
#     big_r = float(input('please enter the radius of the big cirlce R>0: '))


# lil_r = 0

# increment = .00001

# while lil_r * lil_r < big_r * big_r/2:
#     lil_r += increment

# print(lil_r)


'''
Sequence of Squares
-------------------

Given is the sequence of squares in which the first square
has the area of 4, and each consecutive square in the
sequence has the area which is half of the area of the
previous square in the sequence. The sum of areas of certain
number of squares in such sequence equals 255/32. Write a
Python program that determines the number of squares in such
sequence.

'''


area = 4

total_area = 4

counter = 1

# we don't know how many loops so we use a while loop
while total_area < 255/32:
    area /= 2
    total_area += area
    counter += 1

print(counter)
