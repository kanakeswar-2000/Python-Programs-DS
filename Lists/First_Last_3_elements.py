'''
    write program to read N inputs and print the list containing first and last 3 inputs
'''
N=int(input())

L=[]

for i in range(N):
    S=input()
    if (i>=2):
        L+=[S]
    elif (i>=N-3):
        L+=[S]
print(L)