def binary_search(n:int, num_list:list[int]) -> bool:
    
    inizio = 0
    fine = len(num_list) - 1
    

    while inizio <= fine:

        incontro = (inizio + fine)//2
        valore = num_list[incontro]


        if n == valore:
            return True
        elif n < valore:
            fine = incontro -1
        elif n > valore:
            inizio = incontro + 1
    

    return False



print(binary_search(1,[0,1,4,25,45]))