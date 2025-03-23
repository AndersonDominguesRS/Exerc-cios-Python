import heapq

def prim(grafo, origem):

    mst = []
    visitados = set()
    fila_prioridade = []
    
    visitados.add(origem)
    for vizinho, custo in grafo[origem].items( ):
        heapq.heappush(fila_prioridade, (custo, origem, vizinho))
    
    while fila_prioridade:
        custo, vertice_origem, vertice_destino = heapq.heappop(fila_prioridade)
        
        if vertice_destino not in visitados :
            visitados.add(vertice_destino)
            mst.append((vertice_origem, vertice_destino, custo))
            for vizinho, custo in grafo[vertice_destino].items():
                if vizinho not in  visitados:
                    heapq.heappush(fila_prioridade, (custo, vertice_destino, vizinho))
    
    return mst
