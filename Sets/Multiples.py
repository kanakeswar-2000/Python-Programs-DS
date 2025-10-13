'''
    Given an integer N , write a program to create two sets with N multiples of 2 and 3 
    and print the following 
    1. All the multiples of 2 but not the multiples of 3 
    2.All the uncommon multiples of 2 and 3
'''

N=int(input())

set_a=set()
set_b=set()

for i in range(1,N+1):
    set_a.add(2*i)
    set_b.add(3*i)

Multiples_of_2_only=set_a-set_b 
Uncommon_multiples=set_a^set_b 

result_1=list(Multiples_of_2_only)
result_2=list(Uncommon_multiples)

result_1.sort()
result_2.sort()

print(result_1)
print(result_2)
