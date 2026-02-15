'''
Write a program to remove a key in the given dictionary.
Input is a single line containing the word key
'''

students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

key=input() 

del students_dict[key]

print(students_dict)