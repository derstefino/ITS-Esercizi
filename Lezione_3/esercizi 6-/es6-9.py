'''6-9. Favorite Places: Make a dictionary called favorite_places.
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places.
Loop through the dictionary, and print each person’s name and their favorite places.
'''

dict_fav_place:dict[str:str] = {'Phineas':'L.A.', 'Utonium':'Townsville', 'Johnny':'Pops Moon Palace'}

for key in dict_fav_place:
    print(f"{key} is a person and his favourite place is {dict_fav_place[key]}")


