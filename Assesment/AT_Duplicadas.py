def duplicados(lista):
    list_duplicadas = []

    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n ):
            if lista[i] == lista[j]:
                list_duplicadas.append(lista[i])

    print(list_duplicadas )

def duplicados_rash(lista):

    encontrados = set()
    list_duplicadas = []

    for n in lista:
        if n in encontrados:
            list_duplicadas.append(n)
        else:
            encontrados.add(n)
    
    return list_duplicadas

lista = [1, 2, 3, 4, 5, 2, 6, 7, 3, 8, 9, 11, 9, 10, 45, 2]
duplicados(lista)