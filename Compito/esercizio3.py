'''Scrivere un programma che acquisisca una stringa inserita dall'utente e
generi una nuova stringa che corrisponda alla versione invertita della stringa originale.
Il programma deve poi visualizzare la stringa ottenuta in output.
Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''

string1:str = str(input())

string1_inverted = ""

for i in range(len(string1)):
    string1_inverted = string1[i] + string1_inverted

print(string1_inverted)