import heapq



def dijkstra(grafo, origem, destino) :
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[origem] = 0
    
    predecessores = {vertice: None for vertice in grafo}

    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
        
        if vertice_atual == destino:#alterar perfomance
            break
        for vizinho, peso in grafo[vertice_atual].items() :
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                predecessores[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))


    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()

    return distancias[destino], caminho

# teste:
grafo = {
    'Bairro1': {'Bairro2': 10, 'Bairro3': 20},
    'Bairro2': {'Bairro3': 5, 'Bairro4': 15},
    'Bairro3': {'Bairro4': 10},
    'Bairro4': {}
}

origem = 'Bairro1'
destino = 'Bairro4'
distancia, caminho = dijkstra(grafo, origem, destino)

print(f" A distância mais curta de {origem} para {destino} é: {distancia}")
print("O trajeto mais curto é:", " -> ".join(caminho))