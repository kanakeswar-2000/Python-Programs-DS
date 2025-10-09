'''
Remove duplicates in the given sequence of numbers by forming a list and arrange the 
elements in ascending order
'''

num_list=input().split()

set_a=set()

for each_num in num_list:
    set_a.add(each_num)

new_list=list(set_a)

r_list=[]

for num in new_list:
    r_list+=int(num)
    
r_list.sort()

print(r_list)