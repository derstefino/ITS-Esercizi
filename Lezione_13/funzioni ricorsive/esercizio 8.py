'''Esercizio 8.

Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva,
si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.
'''

def vowelsCounter(s:str):

    v = ["a","e","i","o","u","A","E","I","O","U"]
    
    if s[0:]=="":
        return 0
    elif s[0] in v:
        return 1 + vowelsCounter(s[1:])
    else:
        return vowelsCounter(s[1:])
    



print(vowelsCounter("steefano"))