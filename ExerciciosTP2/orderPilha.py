def order_pilha(pilha):
    pilha_ordenada=[]

    while 0 != len(pilha):   
        teste=0
        for n in pilha:
            
            for t in pilha:
                if t <=n:
                    n=t
                    teste=t  
        pilha_ordenada.append(teste)
        pilha.remove(teste)
    print(pilha_ordenada)

pilha_teste=[10,8, -1,5, 1,4,9 ,3, -7 ,6, -2,-9,1000]

order_pilha(pilha_teste)
