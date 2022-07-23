# # practice problems for test 1
# # write a program that enters a radius R of a big circle and uses a loop to find
# # radius r of a circle with the area half of the cirle of radius R

# # so we calculate the area of Big circle divid it by half

# # so then do we just look for a bunch of liitle r that area equal to (piR^2)/ 2

# # so we would need to do it like guessing the midpoint

# from math import pi
# # so we get big r
# big_r = 8

# big_r = float(input('enter the radius: '))
# while big_r <= 0:
#     float(input('enter the radius > 0: '))

# # calculate it's area
# area_big_r = 2 * pi * big_r * big_r

# # divid it by two to get our target area
# target = area_big_r/2

# # start at hald big_r, the actual formular is R/sqrt(2) = r so R/2 is always below that
# little_r = big_r/2

# # then just slowly add to little r until the area is equal or greater thn the target since we are dealing with the SQRT(2) it's never really going to be equal so we can be a little above or below this gets us a little above by whatever teh increment is
# while 2 * pi * little_r * little_r < target:
#     little_r += .0001

# print('The radius of the circle half the area of the original circle is aproximately %10.6f' % little_r)

# def digit_sum(n):

#     digits = [int(x) for x in str(n)]

# print(digit_sum)

# n = int(input( "Enter a positive number that is > 10: "))

# while n <= 10:

#     n = int(input("Reenter a positive number that is > 10: "))


# so this is the offical way of doing it which is quite clever and thankfully essentially how I did it :)

# nice comment block
'''Date: 07/22/2022
   Assignment: Write a script that accepts from the
               keyboard a radius R of a circle, and uses a
               loop to find the radius r of a circle with
               the area half of the circle with radius R

  Description: Variables used in the program - its meaning

                ---- cool this is pretty much what I did 
               big_radius   - value of radius entered from 
                              the keyboard.
               small_radius - radius of the circle with the
                              area half of the circle with
                              the big_radius.
               STEP = 1e-6  - increment used in the search
                              for the value final of a 
                              small_circle.

--- so we explain ourselves here 
Solution idea: We start with the value of the small_radius =
               0.  Then we continue increasing the
               small_radius with the STEP value, until
               twice the area of the small circle becomes
               greater than the are of the big circle.
               Since the area of a big circle is
               pi*big_radius^2, and the area of a small
               circle is pi*small_radius^2, and since the
               area of the big circle should be twice the
               area of the small circle, we should be
               comparing

                 2*pi*small_radius^2 < pi*big_radius^2

              But since the value of pi is the same on
              both sides, we could just compare
   
                 2*small_radius^2 < big_radius^2

'''
# nice!!
STEP = 0.00001   # or STEP = 1e-5

print()
# Make sure big_radius has a positive value
# I like this definitely better
big_radius = 0
while big_radius <= 0:
    big_radius = float(input('Enter a radius of the bigger circle: '))

# i thought of starting at zero but started at big_radius/2 because the actual answer is big_radius/SQRT(2)
small_radius = 0
# so this is essentially what I have though I wrote mine out more... which I prefer :)
while 2*small_radius*small_radius < big_radius*big_radius:
    small_radius += STEP

# so this is how he likes the output --- very good to know
print()
print('                       entered radius of the big circle is: %.4f ' % big_radius)
print('radius of a circle with half the area of the big circle is: %.4f ' % small_radius)
print()
