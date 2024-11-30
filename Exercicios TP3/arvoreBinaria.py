def ordena_arvore(raiz):
    resultado = []
    def ordenado(no):
        if no is not teste:
            ordenado(no.esquerda)
            resultado.append(no.valor)
            ordenado(no.direita)
    ordenado(raiz)
    return resultado