''''
    write a program to read a string S and check S present in the given list L 
    if it presents , then print true else print false.
'''

S=input()

L= ["5", "eat", "9.80", "Water", "python", "-678", "7685.26"] 

is_S_in_L=False 

for word in L:
    if(word==S):
        is_S_in_L=True 
        break

print(is_S_in_L)