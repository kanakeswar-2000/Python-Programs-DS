'''
Given a number N , write a program that reads N inputs and
 prints the list by adding N inputs to the end of the list L
'''
N=int(input())

L=["apple","98.90",True]

for i in range(N):
    S=input()
    L+=[S]
print(L)