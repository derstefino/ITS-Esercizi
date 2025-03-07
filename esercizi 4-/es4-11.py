'''4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1.
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists.
Print the message My favorite pizzas are:, and then use a for loop to print the first list.
Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.'''

pizzas:list[str] = ["Margherita", "Diavola", "Noci e gorgonzola"]

friend_pizzas:list[str] = pizzas.copy() 

pizzas.append("Marinara")

friend_pizzas.append("4 Formaggi")

if pizzas != friend_pizzas:
    print("le due liste sono diverse")


for word in pizzas:

    print(f"My favorite pizzas are: {word}")


for word in friend_pizzas:

    print(f"My friend's favorite pizzas are: {word}")


print(f"My favorite pizzas are: ")

for word in pizzas:

    print(word)




