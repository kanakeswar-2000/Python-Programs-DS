'''
Given a list of words , write a program to print half the list of words , considering one more when ood number of words
'''

words_list=input().split()

no_of_words=len(words_list)

half_words_length=no_of_words//2

if (no_of_words%2==1):
    half_words_length=half_words_length+1 

new_list=words_list[:half_words_length]

print(new_list)






