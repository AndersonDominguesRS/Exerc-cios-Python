import heapq

def dijkstra(grafo, origem, destino) :
    # Inicialisando as distâncias com infinito
    custos = {cidade: float('infinity') for cidade in grafo}
    custos[origem] = 0
    
    predecessores =  {cidade: None for cidade in grafo}
    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        custo_atual, cidade_atual = heapq.heappop(fila_prioridade)
        if cidade_atual == destino :
            break

        for vizinha, custo in grafo[cidade_atual].items():
            novo_custo = custo_atual +  custo

            if novo_custo < custos[vizinha]:
                custos[vizinha] = novo_custo
                predecessores[vizinha] = cidade_atual
                heapq.heappush(fila_prioridade, (novo_custo, vizinha))
    caminho = [ ]
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()

    return custos[destino], caminho

# teste:
grafo = {
    'Cidade1': {'Cidade2': 150, 'Cidade3': 300},
    'Cidade2': {'Cidade3': 100, 'Cidade4': 200},
    'Cidade3': {'Cidade4': 250},
    'Cidade4': {}
}

origem = 'Cidade1'
destino = 'Cidade4'
custo_total, caminho = dijkstra(grafo, origem, destino)

print(f"O custo total da viagem de {origem} para {destino} é: R$ {custo_total}")
print("O trajeto mais econômico é:", " -> ".join(caminho))