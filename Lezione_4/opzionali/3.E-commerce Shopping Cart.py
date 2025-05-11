'''
3. E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
    Create functions that manage the shopping cart, allowing the user to add, remove, and view products in the cart.
    Create a function that calculates the cart total and apply any discounts or taxes.
    Create a funciton to print a detailed summary of the cart including products and totals.
    Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

'''
inventory:list = [] 
cart:list = []

def product(name:str, price:float, quantity:int) -> None:

    product = {name:(price, quantity)}

    inventory.append(product)


def add_product(name:str) -> None:

    for product in inventory:
        if name in product:
            cart.append(product)
        else:
            print("no item to be found")


def remove_product(name:str) -> None:

    for product in cart:
        if name in product:
            cart.remove(product)
        else:
            print("no item to be found")


def view_products() -> None:

    print(cart)


def cart_total() -> None:

    total=0
    for product in cart:
        if type(product)==dict:
            for key, value in product.items():
                total += value[0]*value[1]  

    print(total)


product("matita",3.00,10)

add_product("matita")

cart_total()


        
