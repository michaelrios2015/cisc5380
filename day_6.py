# 7/25/22

# quiz 2 functions
'''
1) define at least one function 

should only need one finction, if you want to use more that is fine 

function should only do one task 

2) you will be expected to write a python script which defines and test the function

3) functions should be defined first --- all the way at the top

ex define a funcation even(n) that returns true if n is even and fals otherwise 

test the function by inputting n interger n from the keyboard and printing an output either 
either n is odd or n is even 


'''

# def even(n):
#     # long version
#     # if n % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     # short version
#     return n % 2 == 0

# n = int(input('please enter an intger: '))

# # keep your printing effecient
# print()
# print('%d is ' %n, end = '')

# if even(n):
#     print('even')
# else:
#     print('odd')
# print()

'''
write a function first_last(string)

That returns the first and last letter of the string
'''
# I guess str is not a reserved word
def first_last(str):
    
    # res = word[0] + word[-1]

    # return res
    return str[0] + str[-1]

word = input('please enter a string: ')


print("the fust and last letters of " + word + ' are ' + first_last(word))


# professor says test test test 
# function then some script to run it 
