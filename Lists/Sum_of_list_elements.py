'''
Given a space seperated numbers , write program to print the sum of all numbers.
'''

numbers=input()

numbers_list=numbers.split()

sum=0 

for each_num in numbers_list:
    num=int(each_num)
    sum+=num 

print(sum)



