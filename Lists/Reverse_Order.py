'''
Given a number N , print N inputs in reverse order
'''

N=int(input())

L=[]

for i in range(N):
    S=input()
    L=[S]+L
print(L)