'''
write a program to update the value of a key in the given dictionary.
Input is a single line containing key value pair seperated by space
'''

students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

key,updated_value=input().split()

students_dict[key]=updated_value 

print(students_dict)