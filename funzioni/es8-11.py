'''8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
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



send_messages(), sent_messages

print(sent_messages, sent_messages)
