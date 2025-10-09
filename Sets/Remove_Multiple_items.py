'''
    A set is given in prefilled code , Provided the sequence of numbers 
    write a program to remove the list of numbers if they present in given set
'''
set_a={10,20,30,40,50,60,70,80,90}

nums_list=input().split()

for num in nums_list:
    num=int(num)
    set_a.discard(num)

new_list=list(set_a)
new_list.sort()

print(new_list)