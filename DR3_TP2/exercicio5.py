# Representação do grafo como lista de adjacência
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}


# Função para exibir os vizinhos de um centro
def exibir_vizinhos(grafo, centro):
    if centro in grafo:
        return f"Vizinhos de {centro}: {', '.join(grafo[centro])}"
    else:
        return f"Centro {centro} não encontrado no grafo."

# Exemplo de uso
for centro in grafo.keys():
    print(exibir_vizinhos(grafo, centro))


# Lista de adjacência com pesos
grafo_com_pesos = {
    'A': [('B', 10), ('C', 15)],
    'B': [('A', 10), ('D', 20)],
    'C': [('A', 15), ('E', 25)],
    'D': [('B', 20), ('E', 30)],
    'E': [('C', 25), ('D', 30)]
}

from collections import deque

# Função de BFS
def bfs_rota_mais_curta(grafo, inicio, destino):
    visitados = set()
    fila = deque([(inicio, [inicio])])  # A fila armazena pares (nó atual, caminho percorrido)

    while fila:
        atual, caminho = fila.popleft()

        if atual == destino:
            return caminho  # Retorna o caminho mais curto encontrado

        if atual not in visitados:
            visitados.add(atual)
            for vizinho in grafo[atual]:
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))

    return f"Não há caminho entre {inicio} e {destino}."

