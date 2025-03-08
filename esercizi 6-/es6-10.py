'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number.
Then print each person’s name along with their favorite numbers.'''

peoples_fav_num:dict[str:list[int]] = {'stefano':[8, 9, 7], 'bob':[5, 11], 'bo':[7], 'robert':[9, 10, 9], 'bobby':[4, 2]}

for key in peoples_fav_num:
    print(f"{key}, {peoples_fav_num[key]}")


