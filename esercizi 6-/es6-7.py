'''6-7. People: Start with the program you wrote for Exercise 6-1.
Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people. As you loop through the list, print everything you know about each person.
'''

dict1:dict[str:str]  = {'first_name':'arthur', 'last_name':'wilson', 'age':'1000', 'city':'roma'}

dict2:dict[str:str]  = {'first_name':'arthur', 'last_name':'wilson 1', 'age':'1000', 'city':'roma'}

dict3:dict[str:str]  = {'first_name':'arthur', 'last_name':'wilson 2', 'age':'1000', 'city':'roma'}


new_list:list[dict] = []

new_list.append(dict1)
new_list.append(dict2)
new_list.append(dict3)


for d in new_list:
    print(d)


