import time


def bubblesort(lista:list[int]) -> list[int]:

    
    for i in range(len(lista)):


        for j in range(i+1, len(lista)):

          if lista[i]>lista[j]:


            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp


    return lista

class Timer:


    def __enter__(self):

        self.start_time = time.time()
        
    
    def __exit__(self, exc_type, exc_value, traceback):

        self.finish_time = time.time() - self.start_time
        print(f"time elapsed:{self.finish_time}")


    
with Timer():
    print(bubblesort( [7,5,12,1] ))







