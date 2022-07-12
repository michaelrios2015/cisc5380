# CISC 5380
# Michael Rios
# HW 2 - Triangles
# Due 7/13/22

print()
print(" TRIANGLE OR NOT ".center(70, '*'))
print(" You will be asked to enter three real numbers. ".center(70, '*'))
print(" Anything else will cause the program to crash. ".center(70, '*'))
print(" If they can form a triangle we will calculate the area for you ".center(70, '*'))
print()
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
print()

area = 0
output = ''

print('The sides:')
if a + b > c and b + c > a and c + a > b:
    s = (a + b + c)/2

# I assume is we fully cross multiplied this expression so that python did not have to use the () it would run
# a bit faster, but I am not sure
    area = (s*(s-a)*(s-b)*(s-c))**.5

    print('   a = %7.3f' % a)
    print('   b = %7.3f' % b)
    print('   c = %7.3f' % c)

    output = ('Area = %7.3f\n' % area)

else:

    print('a = %7.3f' % a)
    print('b = %7.3f' % b)
    print('c = %7.3f' % c)

    output = '\nCannot form a triangle\n'

print(output)
print('the end'.center(30, '-'))
print()
