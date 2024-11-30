def order_lista(lista):
    lista_ordenada=[]

    while 0 != len(lista):   
        teste=0
        for n in lista:
            
            for t in lista:
                if t <=n:
                    n=t
                    teste=t  
        lista_ordenada.append(teste)
        lista.remove(teste)
    print(lista_ordenada)

lista_teste=[10,12,5,6,79,8,1,14]

order_lista(lista_teste)