'''8-10. Sending Messages:
Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message
and moves each message to a new list called sent_messages as it’s printed. After calling the function,
print both of your lists to make sure the messages were moved correctly.
'''

list_messages:list[str] = ["Allontanarsi dalla linea gialla", "Oggi è Martedì", "Basta il pensiero"]

def show_messages() -> None:
    
    for m in list_messages:
        print(m)


sent_messages:list[str] = []

def send_messages() -> None:

      

    for m in list_messages:
        print(m)
        sent_messages.append(m)

    for m in list_messages:
        list_messages.remove(m)
    list_messages.pop(0)


send_messages()

print(list_messages, sent_messages)

