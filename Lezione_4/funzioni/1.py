'''Exercise 1
Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.'''

def check_value(a:float):
    if a == 5:
        print(f"The number {a} is equal to 5")
    
    elif a < 5:
        print(f"The number {a} is smaller than 5")

    else:
        print(f"The number {a} is bigger than 5")



check_value(6)

# on github

