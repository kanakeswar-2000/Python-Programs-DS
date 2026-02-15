'''
Write a program to add a key-value pair to the given dictionay.
Input will be a single line containing space seperated strings representing key-value pair.
'''

students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}
 
key,value=input().split()

students_dict[key]=value 

print(students_dict)