def floyd_warshall(grafo):
    vertices = list(grafo.keys())
    n = len(vertices)
	
    distancias = {v: {u: float('infinity') for u in vertices} for v in vertices}

    for v in vertices:
        distancias[v][v] = 0

    for v in grafo:
        for u, peso in grafo[v].items():
            distancias[v][u] = peso

    for k in vertices : 
        for i in vertices: 
            for j in vertices: 
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
				
                    distancias[i][j] = distancias[i][k] + distancias[k][j]

    return distancias

# testes de uso:
grafo = {
    'Bairro1': {'Bairro2': 5, 'Bairro3': 10},
    'Bairro2': {'Bairro3': 3, 'Bairro4': 2},
    'Bairro3': {'Bairro4': 1},
    'Bairro4': {}
}

distancias_minimas = floyd_warshall(grafo)

print("Menores distâncias entre todos os pares de bairros:")
for origem, destinos in distancias_minimas.items():
    for destino, distancia in destinos.items():
        print(f"{origem} -> {destino}: {distancia}")