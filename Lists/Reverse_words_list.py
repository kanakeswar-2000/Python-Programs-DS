'''
Given a space seperated words , write a program to print the list by reversing the words.
'''

words=input()

words_list=words.split()

reversed_words_list=words_list[::-1]

print(reversed_words_list)