'''
Write a program to create a dictionary , grouping of colored balls and corresponding total score
'''

key_value_pairs=input().split(",")
dict_a={}

for each_item in key_value_pairs:
    c_and_s=each_item.split(":")
    color,score=c_and_s[0],c_and_s[1]
    score=int(score)
    if color in dict_a:
        dict_a[color]=dict_a[color]+score
    else:
        dict_a[color]=score
dict_a_items=list(dict_a.items())
dict_a_items=sorted(dict_a_items)
print(dict_a_items)
