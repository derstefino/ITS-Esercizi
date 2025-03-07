'''3-7. Shrinking Guest List:
You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list.
Print your list to make sure you actually have an empty list at the end of your program.'''

guests:list = ["Adolf", "Cleese", "Hilter"]

for word in guests:
    print(f"It would be an honour to have you over for dinner at Vulcano, sir {word}")

print(guests[1])

guests.remove("Cleese")

new_person = "Neil"

guests.append(new_person)

for word in guests:
    print(f"It would be an honour to have you over for dinner at Vulcano, sir {word}")

print("A bigger table is now available")

guests.insert(0, "Cole")

guests.insert((len(guests)//2), "Chino")

guests.append("Jowgen")

for word in guests:
    print(f"It would be an honour to have you over for dinner at Vulcano, sir {word}")

print("You can only invite two people")

guests.pop()

print("Sorry Jowgen, you're no longer invited to dinner")

guests.pop()

print("Sorry Neil, you're no longer invited to dinner")

guests.pop()

print("Sorry Hilter, you're no longer invited to dinner")

guests.pop()

print("Sorry Chino, you're no longer invited to dinner")

for word in guests:
    print(f"You're still invited to dinner, sir {word}")

del guests[::-1] 

print(guests)

