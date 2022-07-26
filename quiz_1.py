'''
       Name: Michael Rios 
       Date: 7/25/22
 Assignment: Quiz 1
      class: CISC 5380

Write the program that computes the summation of 1/k^2
starting from k = 1 until the value of 1/k^2 is less than 1e-15. 
Your program should output the value of the computed sum as well 
as the number of time it is necessary to increment k.

so we set a target = to 1e-15

we set k = 1

counter and total_sum to 0

we start with our summation equal to one so we can enter the while loop

we recaluate summation 

interate total sum and k

and then output our results 

the formating for the output should probably measure how long k is and then use that length
to create the spaces in front of the total sum but since no user input is involved and 
nothing will change I just set it manually

'''

target = 1e-15

summation  = 1

k = 1 

counter = 0

total_sum = 0

while summation > target:
    summation = 1/(k*k) 
    total_sum += summation
    k +=1


print()
print('           k = %d' %k)
print('computed sum =        %14.12f' %total_sum)
print()


# 
# 1/k/k is the same as 1/(k*k), interesting yes i guess it is  
# official version

k = 1
sum = 1
while 1/k/k > target:
    k += 1
    sum += 1/k/k

print()
print('sum = %16.7f ' %sum)
print('  k = %8d ' %k)
print()

# for testing start with a small number and make sure it's working 