'''
Given N numbers and an T indexes , write a program to form a List with N numbers and 
and print numbers at given indexes.
'''
N=int(input())
T=int(input())

L=[]

for i in range(N):
    num=int(input())
    L+=[num]
for i in range(T):
    k=int(input())
    print("index "+str(i)+" "+str(L[k]))