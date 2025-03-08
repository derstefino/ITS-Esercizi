'''6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. '''

dict1:dict[str:str] = {'pets_name':'Venus', 'kind':'dog', 'owners_name':'T'}

dict2:dict[str:str] = {'pets_name':'Alien', 'kind':'xenomorph', 'owners_name':'Weaver'}

dict3:dict[str:str] = {'pets_name':'Hamburger', 'kind':'crocodile', 'owners_name':'Booker'}

new_list:list = []

new_list.append(dict1)
new_list.append(dict2)
new_list.append(dict3)


print("These are the pets' names:\n")

for dict in new_list:
    print(dict['pets_name'])
print("\n")

print("These are their kinds:\n")

for dict in new_list:
    print(dict['kind'])
print("\n")

print("These are their owners:\n")

for dict in new_list:
    print(dict['owners_name'])


