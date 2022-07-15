# CISC 5380
# Michael Rios
# HW 3 - Bouncing Balls
# Due 7/13/22

print('\n-----Distanced traveled by a bouncing ball-----\n')
# input
h = float(input(
    'Please enter the height from which you will drop the ball, a postive real number please: '))
br = float(input(
    'Please enter the bounce ratio of your ball, between one and zero please: '))
# print()

# I know we did not have to include this... but we learned if statements and I hate not
# checking the input
if h >= 0 and br >= 0 and br < 1:

    print("\nYou dropped a ball from a height of--:   %6.2f" % h)
    print("With a bounce ratio of --------------:   %6.2f" % br)

    # we add the intial fall to our total height
    total_height = h

    # I was getting an error with just h > 0 and high bounce ratios
    # so i am using this to correct that, it's intial value could be anything but the height
    previous_height = 2 * h

    # so while we are still bouncing or it says our bounce is the same height as the last bounce,
    # that is impossible and should trigger a stop
    while h > 0 and previous_height != h:
        # we just set previous height to height
        previous_height = h

        # calculate the new height
        h = h*br

        # and twice the new height, up and down, to the old height
        total_height = total_height + 2 * h
        # print(total_height)
        # print(h)

    # once we exit the loop we are done
    print('------------------------------------------------')
    print("The ball traveled a total distance of:   %6.2f" % total_height)
    print()


else:
    print('\nEither you have a negative height and/or your bounce ratio is not between zero and 1, adios')
    print()
