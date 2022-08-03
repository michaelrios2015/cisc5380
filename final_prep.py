'''
8/2/22

Final Prep 

'''


l = [12, 6, 8, 2, 10, 11, 1, 7, 19]

p = 8

def partion_matrix(l,p):

    first = 0
    last = len(l)-1

    while last > first:

        if l[first] < p:
            first += 1
        else:
            temp = l[first]
            l[first] = l[last]
            l[last] = temp
            last -= 1
    
    return l

# print(partion_matrix(l,p))

# not working integers are inmoutable 
# def swap(i, j):
#     [i, j] = [j, i]
#     # temp = i
#     # i = j
#     # j = temp

def partion(l, p):

    first = 0
    last = len(l) - 1

    # neat a bit different than what I am doing but not a huge amount  
    while first < last:

        while l[first] < p:
            first += 1
        
        while l[last] >= p:
            last -= 1

        # this is to make sure we don't swap after meeting in the middle 
        if first < last:
            # print(l[last], l[first])    
            # swap(l[last], l[first])
            [l[last], l[first]] = [l[first], l[last]]
            # print(l[last], l[first])  
            # since we just swapped them we don't nee dto worry about them 
            first += 1
            last -= 1
# so we don't need to return it it will partion it for use 
    # return l

print(l)
partion(l, p)

print(l)
