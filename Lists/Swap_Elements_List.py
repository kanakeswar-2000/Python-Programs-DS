'''
Given a list L in prefilled code. write a program to read l1 and l2 indexes and 
replace l1 index with l2 index , l2 index with l1 index
'''

L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]
l1=int(input())
l2=int(input())
a=L[l1]
L[l1]=L[l2]
L[l2]=a

print(L)
