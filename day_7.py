'''
7/27/22

the final will be 2 hours 6-8pm wednesday

one programming assignment 

might have multiple functions and such 

open book open notes

submission is the same 

will include lists, and everything else we have done (loops, functions, etc) 

all the formating and such that we always do 

LISTS!!!! - usually an array I guess

list is a linear data structure 

list has zero based index -- so first eleemnt is 0

you can retrieve, update, insert, delet and append

list traverals - examing all the elements one by one of the list

list is mutable, it can be changed 

note the brackets
[1,2,3]

don't need to have same types - ussually cannot do this 
['a', 2, True]

empty list, it's fine often used for testing 
[]

that's it
lst = [1,2,3]

lst[0]
'''

# l = [1,2,3]
# # so each element of an array is like a varible 
# print(l[2])

# sum = l[0] + l[1] + l[2]

# l[1] = 7
# print(l[1])

# # delete 
# del l[1]

# print(l)

# # insert(position, value) --- nice 
# l.insert(1,3)
# print(l)

# # append adds to the end of the list
# l.append(17)
# print(l)

# # sort
# l.sort()
# print(l)

# # reverse
# l.reverse()
# print(l)

'''
tuples inmoutable - no change at all - interesting

almost like a list but with ()
nums = (10, 20, 30)

tuples can have mixed elements

even a sigle entry tuple needs a comma 
(1,)

this is a sequence 

string, tuple , list all sequences 


length len(s) -- numbers of eleemnets in sequence

select s[0] --- 

slice S[1:4] - select elementes 1-4, 1,2,3,4
        s[1:] - select 1 to end

count s.count('e') -- counts the numbers of occuernce of the argument hello we get 1 for the one e
        s.count(4) -- for hello we get an error so 

index s,index('e)  teh first occarnes of the elenet 

Membership 'h' in s  True in hello -- use this a lot very useful

min min(s) - min element

max max(s) - max element 

sum sum(s)-- sum of element, string will give you an eror 

join s+w combines to sequence ohh use this with strings a lot but you can do it with tuples and strings too
tuples makes a new one does not modify original ones

list of list are fine

[[1,2,3], [7,8,9]]

so l[0] = [1,2,3]
first element of teh first elemnet 
l[0][0] = 1

Used this 

Iteratrating the list 


create a nested list 

l = [[2,7,6],[5,3,1],[4,9,8]]

print this lit 

list by list 
'''
# matrix print
# l = [[2,7,6, 10],[5,3,1],[4,9,8]]

# print()

# for row in range(len(l)):
#     # so using row lets us print rows of different length so it is more versitile 
#     for column in range(len(l[row])): 
#         print('%5d' %l[row][column], end = '')
#     print()
# print()

# for ch in 'My name':
#     print(ch, end = '   ')
# print() 

# # while loops

# nums = [1,2,3,4]
# # we should noy use a while loop like this when we know the lenght, if we did not while is ok 
# k = 0 
# while k < len(nums):
#     print(nums[k], end = '--')
#     k += 1

# this will make a list
l = list(range(0,11,2))

print(l)

'''
hw 5 

due monday 8/1

write a script that creates a 2d list of random integers each in range [0,25]
with random length of each row 

number of row is also randon [1,6]

range of row length [5,8]

you can make this a function and such 
prints the list in the matrix form as we did in class

prints the maxium intger in the whole 2 d list 

example 

7 9 6 2
1 0 5 12 19
5 6 
4 9 3
13 7 9 5 

try to have a create list function, no arguments

a print list function, list is the argument

a find max function 

l= create_list()

print_list(l) 

print('max = " find_max(l))

'''