def criar_grafo() : 


    return {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B', 'E'],
        'E': ['B', 'D', 'F'],
        'F': ['C', 'E']
    }
	

grafo = criar_grafo() 

def dfs(grafo, inicio, visitados=None):

    if visitados is None:
	
        visitados = set()
    
    visitados.add(inicio)
    print(inicio, end=' ') #incluir altrd
    
    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)
			
from collections import deque

def bfs(grafo, inicio):

    visitados = set()
    fila = deque([inicio])
    
    visitados.add(inicio)
    
    while fila: #melhorar tempo while
	
        vertice = fila.popleft( )
        print(vertice, end=' ')
        
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
				
				
grafo = criar_grafo()

print("DFS (Busca em Profundidade) a partir da Estacao A:")
dfs(grafo, 'A')

print("\n\nBFS (Busca em Largura) a partir da Estacao A:")
bfs(grafo, 'A')