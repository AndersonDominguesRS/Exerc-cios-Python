lista=[10,8, -1,5, 1,4,9 ,3, -7 ,6, -2,-9,1000]

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
               



boubbleSort(lista)