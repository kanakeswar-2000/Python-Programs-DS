'''
Given a sentence , write a program to print the same sentence by reversing the letters in the each word.
'''

sentence=input()

words_list=sentence.split()

result_list=[]

for word in words_list:
    reversed_word=word[::-1]
    result_list+=[reversed_word]

result=" ".join(result_list)

print(result)


