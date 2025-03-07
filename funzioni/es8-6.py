'''8-6. City Names: Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this: "Santiago, Chile".
Call your function with at least three city-country pairs, and print the values that are returned.'''

def city_country(city:str, country:str)->str:
    city= city + ","
    return city


print((city_country("Aranciopoli", "Kanto")))

print(city_country(("Whiterun", "Skyrim")))

print(city_country(country="Romania", city="Bucarest"))


