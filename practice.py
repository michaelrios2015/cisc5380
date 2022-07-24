# quizes monday - 7/25 wednesday -7/28

# sumation series

# take in n as a keyboard from keyboard
#
# take in x from keyboard
#
# 1 + x + x^2/2! + + x^3/3! +.... x^n/n!


# so this is teh numbers of time we need to sum
n = 0
while n < 1:
    n = int(input(
        'please enter the number of times to sum, integers of 1 or greater please: '))

# this is the number to sum
x = 0
while x < 1:
    x = int(
        input('please enter the number to sum, real numbers of 1 or greater please: '))

# we need an x to the power of
x_thpo = x

# our first factorial
fact = 1

# our fist total
total = 1

# the number of times we will go through the summations
for i in range(2, n+1):

    # fact = fact * i
    # print('fact ', fact)

    # so we add to our total the current x^n/n!
    total += x_thpo/fact
    # print('new_x ', new_x)

    # print('fact ', fact)

    # now we update the factorial (this is why I wanted to start at 2)
    fact = fact * (i)
    # print(new_x/fact)

    # we update the x^n
    x_thpo = x_thpo * x
    # print('new_x ', new_x)

# we return the total
print('total ---  %7f' % total)
