'''
write a program to replace the last element with the given number in each tuple of a list given below.
'''

list_a=[(1,2,3),(10,30),(11,32,45,89)]
N=int(input())
new_list=[]
for each_tuple in list_a:
    new_tuple=each_tuple[:-1] +(N,)
    new_list.append(new_tuple)

print(new_list)
