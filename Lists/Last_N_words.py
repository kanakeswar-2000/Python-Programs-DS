'''
Given a space seperated words and a number N, write a program to print last N words in reverse order
'''

sentence=input()

N=int(input())

words_list=sentence.split()

new_list_of_words=words_list[-N:]

reversed_words=new_list_of_words[::-1]

print(reversed_words)