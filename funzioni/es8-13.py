'''8-13. User Profile:  Build a profile of yourself by calling build_profile(),
using your first and last names and three other key-value pairs that describe you.
All the values must be passed to the function as parameters.
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
'''

def build_profile(first_name:str, last_name:str, age:int, height:float, gender:str) -> str:


    return f"{first_name} {last_name}, age {age}, height {height:.2f}, gender {gender}"


print(build_profile("Albert", "Wesker", 27, 1.90, "Uomo"))

