'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in your dictionary.
Print each person’s name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program.'''

peoples_fav_num:dict[str:int] = {'stefano':8, 'bob':5, 'bo':7, 'robert':9, 'bobby':4}


for key in peoples_fav_num:
    print(key)

print("here's their favourite numbers:\n")

for key in peoples_fav_num:
    print(peoples_fav_num[key])


poll_name:str = str(input("what's your name? "))

poll_number:str = str(input("what's your fav number? "))

peoples_fav_num[poll_name] = poll_number

print(peoples_fav_num)





