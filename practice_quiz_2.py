'''

1. Write and test a function that computes:

   a) r(x) = 1/(1 + 25x^2)

   b) h(x) = 1/((x-0.3)^2+0.01) +  1./((x-0.9)^2+0.04) - 6

   c) s(n) = 1^3 + 2^3 + .... + n^3

'''

from random import random


def r(x):

    return 1/(1 + 25*x*x)


print('r(3) %f' % r(3))


def h(x):

    # return (x-.3)(x-.3) + .01
    return 1/((x-.3)*(x-.3) + .01) + 1/((x-.9)*(x-.9) + .04) - 6


# print(h(3))

print('h(3) %f' % h(3))


def s(n):

    sum = 0

    for i in range(1, n+1):

        sum += i*i*i

    return sum


print('s(3) %d' % s(3))


'''
2. Write and test function maxint( l ) that returns the
   maximum value in list l. For example, given list of
   integers l = [3, 7, 1, 8, 9, 2], maxint( l ) should
   return 9.

'''


def maxint(l):
    max = l[0]

    for i in range(1, len(l)):
        if l[i] > max:
            max = l[i]

    return max


l = [3, 7, 1, 8, 9, 2]

print('maxint %d' % maxint(l))


'''
3. Write and test function minint( l ) that returns the
   minium value in list l. For example, given list of
   integers l = [3, 7, 1, 8, 9, 2], minint( l ) should
   return 1.
'''


def minint(l):
    min = l[0]

    for i in range(1, len(l)):
        if l[i] < min:
            min = l[i]

    return min


l = [3, 7, 1, 8, 9, 2]

print('minint %d' % minint(l))


'''
4. Write and test function signum( n ) that returns the
   following

                 1    if  n is greater than or equal to 0
   signum(n) =
                 0    otherwise
'''


def signum(n):

    if n >= 0:
        return 1
    else:
        return 0


print('signum positive %d' % signum(7))
print('signum negative %d' % signum(-17))


'''

5. Write and test function named large_random that
   returns a random number greateer than 0.5

'''


def large_random():

    x = 0

    while x < .5:
        x = random()

    return x


print('large number %f' % large_random())
