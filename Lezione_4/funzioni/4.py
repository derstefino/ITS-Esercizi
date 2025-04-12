'''Exercise 4
Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.'''

def check_each(a:list):
    for num in a:
        if num < 5:
            print("smaller")
        elif num > 5:
            print("bigger")
        else:
            print("equal")



check_each([4,4,4,4,4,4,5,8]   )


# on github