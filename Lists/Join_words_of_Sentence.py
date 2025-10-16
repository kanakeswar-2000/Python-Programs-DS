'''
Given a sentence S containing space seperated words , 
Write a program to print a string by joining the words in a sentence with dot (.)
'''

S=input()

words_list=S.split()

result=".".join(words_list)

print(result)
