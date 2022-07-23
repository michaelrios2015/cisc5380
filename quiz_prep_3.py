# '''
# Given is the sequence of squares in which the first square
# has the area of 4, and each consecutive square in the
# sequence has the area which is half of the area of the
# previous square in the sequence. The sum of areas of certain
# number of squares in such sequence equals 255/32. Write a
# Python program that determines the number of squares in such
# sequence.
# '''

# total_area = 0

# area = 4

# counter = 0


# while total_area != 255/32:

#     total_area += area

#     area = area/2

#     print(area)

#     counter += 1

# print(total_area)
# print(counter)


# the official version
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
# this is essentially exactly the same as I did
square_area = 4.0
number_of_squares = 1

total_area = square_area
while total_area != 255/32:
    square_area = 0.5*square_area
    total_area += square_area
    number_of_squares += 1

# another example of how to print the results
print()
print('Number of squares in the sequence is: %d ' % number_of_squares)
print()
