import heapq

grafo = {
    'CD': [('A', 2), ('B', 5)],
    'A': [('CD', 2), ('C', 3)],
    'B': [('CD', 5), ('C', 2), ('D', 6)],
    'C': [('A', 3), ('B', 2), ('D', 1)],
    'D': [('B', 6), ('C', 1), ('E', 4)],
    'E': [('D', 4), ('F', 2)],
    'F': [('E', 2)]
}


def dijkstra(grafo, origem, destino):

    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origem] = 0 

    heap = [(0, origem)] 
    caminhos = {vertice: [] for vertice in grafo}
    caminhos[origem] = [origem]

    while heap:
        distancia_atual, vertice_atual = heapq.heappop(heap)

        for vizinho, peso in grafo[vertice_atual]:
		
            nova_distancia = distancia_atual + peso


            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                caminhos[vizinho] = caminhos[vertice_atual] + [vizinho]
				
                heapq.heappush(heap, (nova_distancia, vizinho))

    return distancias, caminhos
	
	
distancias, caminhos = dijkstra(grafo, 'CD', 'F')

destino = 'F'
rota = caminhos[destino]
custo_total = distancias[destino]

print(f"rota mais curta do CD ate {destino}: {' -> '.join(rota)}")
print(f"Custo total (distância mínima): {custo_total} km")

