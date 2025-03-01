'''Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n,
entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:

a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e,
quindi, visualizzare in output le liste a, b, c.'''

a:list = [1,2,3]

b:list = [4,5,8]

c:list =[a[1] + b[2-1], a[2] + b[2-2], a[0] + b[2]]

print(a,b,c)