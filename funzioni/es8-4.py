'''8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''

def make_shirt(size:str="Large", message:str="I love Python"):

    print(f"Size of T-shirt: {size}. Message printed on: {message}")


make_shirt()

make_shirt("Medium")

make_shirt("Any size", "I like Python less now")