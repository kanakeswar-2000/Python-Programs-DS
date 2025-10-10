'''
   Convert the given sequence of numbers into list.
'''

nums_list=input().split(",")

i=0 

for num in nums_list:
    nums_list[i]=int(num)
    i+=1 

tuple_a=tuple(nums_list)

print(tuple_a)