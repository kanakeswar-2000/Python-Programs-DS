'''
Given a prefilled code of fruits dictionary , write a program to rename the 
fruit name(first line input) with other fruit name (second line input)
'''
fruits={
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50

}

fruit_name=input()
new_fruit_name=input()

fruit_items=fruits.items()

new_fruit_items=[]

for item in fruit_items:
    if (item[0]==fruit_name):
        list_item=list(item)
        list_item[0]=new_fruit_name
        new_item=tuple(list_item)
        new_fruit_items.append(new_item)
    else:
        new_fruit_items.append(item)

print(new_fruit_items)
