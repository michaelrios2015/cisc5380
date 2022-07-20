# quizes monday - 7/25 wednesday -7/28

# sumation series

# take in n as a keyboard from keyboard
#
# take in x from keyboard
#
# 1 + x + x^/2! + + x^3/3! +.... x^n/n!

n = 1000

x = 3

new_x = x

fact = 1

total = 1

for i in range(2, n+1):

    # fact = fact * i
    # print('fact ', fact)

    total += new_x/fact
    # print('new_x ', new_x)

    # print('fact ', fact)

    fact = fact * (i)
    # print(new_x/fact)
    new_x = new_x * x
    # print('new_x ', new_x)

print('total ---  %f' % total)
