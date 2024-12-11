lista = list(range(1, 100001))
def pesquisa_linear(lista, isbn):
    total = 0
    for n in lista:
        total += 1
        if n == isbn:
             print (f"O total de iteraçoes com a pesquisa linear foi de: {total}")
        
def pesquisa_binaria(lista, isbn):
    esquerda, direita = 0, len(lista) - 1
    total = 0
    while esquerda <= direita:
        total += 1

        meio = (esquerda + direita) // 2
        if lista[meio] == isbn:
            print (f"O total de iteraçoes com a pesquisa binária foi de: {total}")
            return total
        elif lista[meio] < isbn:
            esquerda = meio + 1
        else:
            direita = meio - 1    
        
        
pesquisa_linear(lista, 100)
pesquisa_binaria(lista, 100)

        
