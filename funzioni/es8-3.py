'''8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.'''

def make_shirt(size:int, message:str):

    print(f"Size of T-shirt: {size}. Message printed on: {message}")

make_shirt(40, "feeble")

make_shirt(message="a mi manera", size=30)
