import heapq

def prim(grafo, inicio):
    mst = []
    visitados = set()
    heap = [(0, inicio, None)]
    total_custo = 0

    while heap:
	
        peso, atual, anterior = heapq.heappop(heap)

        if atual in visitados:
            continue

        visitados.add(atual)

        if anterior is not None:
		
            mst.append((anterior, atual, peso))
            total_custo += peso

        for vizinho,  custo in grafo[atual]:
            if vizinho not in visitados:
                heapq.heappush(heap, (custo, vizinho, atual) )

    return mst, total_custo
	


grafo = {
    'A': [('B', 1), ('D', 3)],
    'B': [('A', 1), ('C', 2), ('D', 4)],
    'C': [('B', 2), ('D', 5)],
    'D': [('A', 3), ('B', 4), ('C', 5)]
}

mst, custo = prim(grafo, 'A')
print("Árvore Geradora Mínima:", mst)
print("Custo Total:", custo)