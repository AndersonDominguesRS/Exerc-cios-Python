import numpy as np

def criar_matriz_adjacencia(bairros, conexoes):

    n = len(bairros)
    matriz = np.full((n, n), float('inf'))
    np.fill_diagonal(matriz, 0)

    for bairro, conexoes_bairro in conexoes.items():
        for destino, distancia in conexoes_bairro:
            i, j = bairros.index(bairro), bairros.index(destino)
            matriz[i][j] = distancia
    
    return matriz

bairros = ['A', 'B', 'C', 'D', 'E', 'F']

conexoes = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 5)],
    'C': [('A', 2), ('D', 8), ('E', 3)],
    'D': [('B', 5), ('C', 8), ('F', 6)],
    'E': [('C', 3), ('F', 1)],
    'F': [('D', 6), ('E', 1)],
}

matriz = criar_matriz_adjacencia(bairros, conexoes)

print("Matriz de Adjacencia:")
print(matriz)


def criar_lista_adjacencia(conexoes):
    lista_adjacencia = {}
    for bairro, conexoes_bairro in conexoes.items():
        lista_adjacencia[bairro] = conexoes_bairro
    return lista_adjacencia

lista = criar_lista_adjacencia(conexoes)
print("\nLista de Adjacencia:")
for bairro, conexoes_bairro in lista.items():
    print(f"{bairro}: {conexoes_bairro}")