import heapq

def dijkstra(grafo, origem):
    distancias = {vertice: float('infinity') for vertice in grafo }
    distancias[origem] = 0

    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] =  distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return distancias 

# teste:
grafo = {
    'Centro': {'A': 4, 'B': 2 },
    'A': {'C': 3, 'D': 2},
    'B': {'A': 1, 'D': 4},
    'C': {'D': 1},
    'D': {}
}

centro_distribuicao = 'Centro'
distancias_minimas = dijkstra(grafo, centro_distribuicao)

print("Distâncis mínimas do centro de distribuição para cada bairro:")
for bairro, distancia in distancias_minimas.items():
    print(f"{bairro}: {distancia}")