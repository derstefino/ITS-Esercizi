'''8-9. Messages: Make a list containing a series of short text messages.
Pass the list to a function called show_messages(), which prints each text message.'''

list_messages:list[str] = ["Allontanarsi dalla linea gialla", "Oggi è Martedì", "Basta il pensiero"]

def show_messages() -> None:
    
    for m in list_messages:
        print(m)

show_messages()