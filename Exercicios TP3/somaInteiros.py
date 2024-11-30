def soma_inteiros(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_inteiros(lista[1:])