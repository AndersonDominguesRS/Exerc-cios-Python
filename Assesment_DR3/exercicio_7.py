import numpy as np

def criar_matriz_adjacencia():
    INF = float('inf')  #teste ausencia
    matriz = [
        [0, 2, 4, INF, INF, INF],  # A
        [2, 0, 1, 7, INF, INF],    # B
        [4, 1, 0, INF, 3, INF],    # C
        [INF, 7, INF, 0, INF, 1],  # D
        [INF, INF, 3, 2, 0, 5],    # E
        [INF, INF, INF, 1, 5, 0],  # F
    ]
    return np.array(matriz)

matriz = criar_matriz_adjacencia()

def floyd_warshall(matriz):
    n = len(matriz)
    dist = matriz.copy() 

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
	
	

matriz_distancias = floyd_warshall(matriz)


print("Matriz de menores tempos de viagem:")
print(matriz_distancias)

bairros = ['A', 'B', 'C', 'D', 'E', 'F']
indice_A = bairros.index('A')
indice_F = bairros.index('F')
tempo_minimo_A_F = matriz_distancias[indice_A][indice_F]
print(f"\nTempo mínimo para viajar do Bairro A ate o Bairro F: {tempo_minimo_A_F} minutos")