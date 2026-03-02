'''
Write a program to combine two dictionaries updating values for  common keys
'''

def str_int(str_num_list):
    int_list=[]
    for i in str_num_list:
        i=int(i)
        int_list.append(i)
    return int_list 

def convert_to_key_value_pairs(keys_list,values_list):
    dic={}
    for i in range(len(keys_list)):
        key=keys_list[i]
        value=values_list[i]
        dic[key]=value 
    return dic 

names_list1=input().split()
num_list1=input().split()
num_list1=str_int(num_list1)

names_list2=input().split()
num_list2=input().split()
num_list2=str_int(num_list2)

dict_1=convert_to_key_value_pairs(names_list1,num_list1)
dict_2=convert_to_key_value_pairs(names_list2,num_list2)

dict_1.update(dict_2)
dict_1_items=list(dict_1.items())
dict_1=sorted(dict_1_items)

print(dict_1)
 

 
