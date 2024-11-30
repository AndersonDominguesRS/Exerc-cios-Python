def proc(lista, val, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        if val < lista[meio]:
            return proc(lista, val, inicio, meio)
        else:
            return proc(lista, val, meio + 1, fim)
    else:
        return inicio

def order(lista):
    for i in range(1, len(lista)):
        val = lista[i]
        j = proc(lista, val, 0, i)
        lista = lista[:j] + [val] + lista[j:i] + lista[i+1:]
    return lista

lista_teste=[12,20,10,3,6,5,9,78,99]

print (order(lista_teste))