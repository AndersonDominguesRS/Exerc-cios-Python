def pedidos_pares(pilha): 
    total=0
    for i in pilha:
        if i % 2 == 0:
            total=total+1
    print(total)

pilha_teste=[10,8,5, 1,4,9 ,3 ,6]

pedidos_pares(pilha_teste)