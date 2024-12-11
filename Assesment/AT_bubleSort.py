import time
lista = list(range(1, 10001))
def boubbleSort(lista):
    novaLista=[]
    while 0 != len(lista):   
        teste=0
        for n in lista:            
            for t in lista:
                if t <=n:
                    n=t
                    teste=t  
        novaLista.append(teste)
        lista.remove(teste)
    print ("LISTA ORDENADA: ", novaLista)            


inicio= time.time()
boubbleSort(lista)
fim= time.time()
print (f"Total tempo de execussão: {fim - inicio}")