'''Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

    acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
    calcolare e visualizzare la somma di tutti i numeri pari inseriti;
    calcolare e visualizzare la media di tutti i numeri dispari inseriti;
    determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
    se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
'''

sum_even:int = 0
sum_odd:int = 0
count_odd:int = 0
number_list:list = []
freq:dict = {} 




while True:

    number:int = int(input("Inserisci un numero (0 per terminare): "))

    if number == 0:
        break

    number_list.append(number)

    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number
        count_odd += 1

for number in number_list:
    if number in freq:
            freq[number] += 1
    else:
            freq[number] = 1

number_freq = freq.items()
    
max_freq = max(freq.values())
    
if sum_odd > 0:
    print(f"Somma dei numeri pari: {sum_even}")
    
if sum_even > 0:
    print(f"Media dei numeri dispari: {sum_odd/count_odd}")

for number, frequence in number_freq:
    if frequence == max_freq:
            print(f"Numero più frequente: {number} ({frequence} volte)")