def f(lista:list[int]) -> dict:

    d1 = {}
    l1 = []
    l2 = [] 

    for num in lista:
        if num >= 0:
            l1.append(num)
            
        else:
            l2.append(num)
            


    d1['positivi'] = l1
    d1['negativi'] = l2

    return d1



lis:list[int] = [1,3,2,5,-6,646]

print(f(lista=lis))