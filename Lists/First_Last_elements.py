'''
Given an integer N , write a program to read N inputs and form a list with first and last two elements
'''

N=int(input())

L=[]

for i in range(N):
    num=int(input())
    L+=[num]
print(L[:2]+L[N-2:])