def quick_sort(lista):

    if len(lista) <= 1:
        print (lista)
        return lista
    
    else:
        pPartida = lista[len(lista) // 2]
        esquerda = [x for x in lista if x < pPartida]
        meio = [x for x in lista if x == pPartida]
        direita = [x for x in lista if x > pPartida]
        return quick_sort(esquerda) + meio + quick_sort(direita)