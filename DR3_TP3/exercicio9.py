import heapq

def prim(grafo, origem):

    mst = [] 
    visitados = set()
    fila_prioridade = [ ]
    
    visitados.add(origem)
    for vizinho, custo in grafo[origem].items():
        heapq.heappush(fila_prioridade, (custo, origem, vizinho))
    
    while fila_prioridade:
        custo, cidade_origem, cidade_destino = heapq.heappop(fila_prioridade)
        
        if cidade_destino not in visitados:
            visitados.add(cidade_destino)
            mst.append((cidade_origem, cidade_destino, custo))
            
            for vizinho, custo_vizinho in grafo[cidade_destino].items():
                if vizinho not in visitados:
                    heapq.heappush(fila_prioridade, (custo_vizinho, cidade_destino, vizinho))
    
    return mst

# teste :
grafo = {
    'Cidade1': {'Cidade2': 5, 'Cidade3': 10},
    'Cidade2': {'Cidade1': 5, 'Cidade3': 3, 'Cidade4': 7},
    'Cidade3': {'Cidade1': 10, 'Cidade2': 3, 'Cidade4': 4},
    'Cidade4': {'Cidade2': 7, 'Cidade3': 4}
}

origem = 'Cidade1'
mst = prim(grafo, origem)

print("arvore Geradora Mínima (MST):")
for aresta in mst:
    print(f"Aresta {aresta[0]} -> {aresta[1]} com custo {aresta[2]}")