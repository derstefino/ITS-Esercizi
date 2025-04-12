'''3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''

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