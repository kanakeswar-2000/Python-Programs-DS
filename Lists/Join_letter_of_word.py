'''
Given a sentence S containing space seperated words 
write a program to print string by joining third letter of each word in sentence.
'''

S=input()

words=S.split()

list_a=[]

for word in words:
    if (len(word)>2):
        letter=word[2]
        list_a.append(letter)

result=",".join(list_a)

print(result)
    

