'''
CISC 5380
Michael Rios
HW 3 - Bouncing Balls - Version 2.0
Due 7/22/22

This program accepts a intail height from which a ball is dropped 
and the bouncing ratio of the ball.  

It then calculates the total distance traveled by the ball.

If a user enters a negative height or a bouncing ratio not between 0 and 1 they will be prompted to renter the data until it is entered correctly

If the users enters a non number the program will crash 

'''
import sys

def total_height(h, br):
  total_height = h

  while h > sys.float_info.min:
    
      h = h*br
  
      total_height = total_height + 2 * h

  return total_height

print('\n-----Distanced traveled by a bouncing ball-----\n')
h = float(input(
    'Please enter the height from which you will drop the ball, a postive real number please: '))

while h <= 0:
  h = float(input(
    'Please enter the height from which you will drop the ball, a postive real number please: '))

br = float(input(
  'Please enter the bounce ratio of your ball, between one and zero please: '))
while br <= 0 or br >= 1: 
    br = float(input(
    'Please enter the bounce ratio of your ball, between one and zero please: '))


print("\nYou dropped a ball from a height of--:   %6.2f" % h)
print("With a bounce ratio of --------------:   %6.2f" % br)

# total_height = h

# while h > sys.float_info.min:
  
#     h = h*br

#     total_height = total_height + 2 * h

print('------------------------------------------------')
print("The ball traveled a total distance of:   %6.2f" % total_height(h, br))
print()


