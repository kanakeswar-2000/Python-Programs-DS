'''
Given a space seperated integers , write a program to print smallest number among the given numbers.
'''

numbers=input()

numbers_list=numbers.split()

smallest_num=numbers_list[0]

for num in numbers_list:
    if (num<smallest_num):
        smallest_num=num 

print(smallest_num)