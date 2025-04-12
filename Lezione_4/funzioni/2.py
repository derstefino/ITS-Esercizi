'''Exercise 2
Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.'''

def check_length(a:str):
    if len(a) > 10:
        print(f"The length of {a} is bigger than than 10 characters")
    elif len(a) < 10:
        print(f"The length of {a} is smaller than than 10 characters")
    else:
        print(f"The length of {a} is equal to 10 characters")



check_length("hello")

# on github
