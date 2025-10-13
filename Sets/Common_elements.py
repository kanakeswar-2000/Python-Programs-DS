'''
    Given two lines comma seperated integers ,
    write a program to print a list containing common elements in both the lines
'''

list_a=input().split(",")
list_b=input().split(",")

list_a=list(map(int,list_a))
list_b=list(map(int,list_b))

set_a=set(list_a)

common_elements=set_a.intersection(list_b)

result_list=list(common_elements)

print(result_list)
