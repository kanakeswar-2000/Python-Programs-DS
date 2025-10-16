'''
Given space seperated numbers, write a program to print a list containing the given numbers
'''

Numbers_List=input().split() 

resultant_list=[]

for num in Numbers_List:
    number=int(num)
    resultant_list+=[number]

print(resultant_list)