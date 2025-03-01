'''Il valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e
determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate.

Quindi:

    progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
    modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
    modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
    modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.

Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''


pi_greco_approx:float = 4
den:int = 3
i:int = 0

while (((pi_greco_approx*100)//1)/100  != 3.14):
    if i % 2 == 0:
        pi_greco_approx -= 4/den
    if i % 2 !=0:
        pi_greco_approx += 4/den
    i += 1
    den += 2

print(f"per ottenere il valore approssimativo di 3.14 servono {i} termini")

while (((pi_greco_approx*1000)//1)/1000  != 3.141):
    if i % 2 == 0:
        pi_greco_approx -= 4/den
    if i % 2 !=0:
        pi_greco_approx += 4/den
    i += 1
    den += 2

print(f"per ottenere il valore approssimativo di 3.141 servono {i} termini")

while (((pi_greco_approx*10000)//1)/10000  != 3.1415):
    if i % 2 == 0:
        pi_greco_approx -= 4/den
    if i % 2 !=0:
        pi_greco_approx += 4/den
    i += 1
    den += 2

print(f"per ottenere il valore approssimativo di 3.14159 servono {i} termini")

while (((pi_greco_approx*100000)//1)/100000  != 3.14159):
    if i % 2 == 0:
        pi_greco_approx -= 4/den
    if i % 2 !=0:
        pi_greco_approx += 4/den
    i += 1
    den += 2

print(f"per ottenere il valore approssimativo di 3.14159 servono {i} termini")