'''
Given student-names in the first line and corresponding student-ids second line comma seperated.
Write a program to print student-name and his/her student-id on each line in alphabetical order.
'''

def Convert_Key_Values_to_dict(studentNames,studentIds):

    dict_a={}

    for i in range(len(studentNames)):
        dict_a[studentNames[i]]=studentIds[i]

    return dict_a

names=input().split(",")
ids=input().split(",")

student_details_dict=Convert_Key_Values_to_dict(names,ids)

student_details_dict=sorted(student_details_dict.items())

for key,value in student_details_dict:
    print(key,value)