'''8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
'''

def ingredients(*args:str) -> None:


    print("The sandwich cointains the following ingredients:\n")
    for x in args:
        print(x)
    print("\n")

ingredients("Pollo", "Insalata")
ingredients("Avocado")
ingredients("Banana", "Peanut Butter")