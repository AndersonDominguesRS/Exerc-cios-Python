def q_select(lista, k):

    print(lista)
    if len(lista) == 1:
        return lista[0]
    
    ref = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < ref]
    centro = [x for x in lista if x == ref]
    direita = [x for x in lista if x > ref]

    if k < len(esquerda):
        return q_select(esquerda, k)
    
    elif k < len(esquerda) + len(centro):
        return ref
    
    else:
        return q_select(direita, k - len(esquerda) - len(centro))