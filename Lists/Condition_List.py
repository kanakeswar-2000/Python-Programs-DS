'''
    A list is given in the prefilled code ,
    Given a number N , write a program to return a list containing numbers greater than N
'''

N=int(input())
List=[2,15,60,21,34,70,45,97]
new_List=[]

for num in List:
    if (num > N):
        new_List+=[num]

print(new_List)
