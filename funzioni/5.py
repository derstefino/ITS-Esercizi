'''Exercise 5
Write a function add_one(). It takes an integer as argument. The function adds 1 to the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented
by 1.
Print new_list.
Example:
add_one_to_list([1, 2, 3])
>>> [2, 3, 4]'''

def add_one(a:int):
    result = a + 1
    return result

def add_one_to_list(b:list[int]):
    
    new_list:list = []
    
    for x in b:
        
        new_list.append(add_one(x))
        
    print(new_list)



add_one_to_list([1,3,5])


# on github
