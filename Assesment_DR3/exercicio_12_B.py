import itertools

import random

def algoritmo_genetico_tsp(grafo, populacao_tamanho=100, geracoes=500, taxa_mutacao=0.1): 

    n = len(grafo)
    
    def gerar_populacao_inicial(): 
        return [random.sample(range(n), n) for _ in range(populacao_tamanho)]

    def calcular_custo(caminho):
	
        return sum(grafo[caminho[i]][caminho[i+1]] for i in range(n-1)) + grafo[caminho[-1]][caminho[0]]

    def selecao_roleta(populacao, custos):
	
        total_fitness = sum(1/c for c in custos)
        prob = [(1/c)/total_fitness for c in custos]
        acumulado = [sum(prob[:i+1]) for i in range(len(prob))]
        r = random.random()
		
        for i, p in enumerate(acumulado):
            if r <= p:
                return populacao[i]

    def cruzamento(pai1, pai2): 
        ponto = random.randint(0, n-1)
		
		
        filho = pai1[:ponto] + [cidade for cidade in pai2 if cidade not in pai1[:ponto]]
        return filho

    def mutacao(caminho):
	
        if random.random() < taxa_mutacao:
            i, j = random.sample(range(n), 2)
            caminho[i], caminho[j] = caminho[j], caminho[i]

    populacao = gerar_populacao_inicial()
	
    for _ in range(geracoes):
        custos = [calcular_custo(caminho) for caminho in populacao]
        nova_populacao = []

        for _ in range(populacao_tamanho):
            pai1 = selecao_roleta(populacao, custos)
            pai2 = selecao_roleta(populacao, custos)
            filho = cruzamento(pai1, pai2)
            mutacao(filho)
			
            nova_populacao.append(filho)
        
        populacao = nova_populacao
		

    melhor_caminho = min(populacao, key=calcular_custo)
    melhor_custo = calcular_custo(melhor_caminho)
    return melhor_custo, melhor_caminho

def held_karp_tsp(grafo):

    n = len(grafo)
    dp = {}

    for i in range(1, n): 
        dp[(1 << i, i)] = (grafo[0][i], 0)

    for tamanho in range(2, n):
	
        for subset in itertools.combinations(range(1, n), tamanho):
		
            mask = sum(1 << i for i in subset)
			
            for j in subset :
			
                dp[(mask, j)] = min(
                    (dp[(mask ^ (1 << j), k)][0] + grafo[k][j], k)
                    for k in subset if k != j 
                )

    mask = (1 << n) - 2 
    res = min(
        (dp[(mask, i)][0] + grafo[i][0], i) for i in range(1, n)
    )


    caminho = [0]
	
    last = res[1]
    mask = (1 << n) - 2
    while last:
	
        caminho.append(last)
        next_mask = mask ^ (1 << last)
        last = dp[(mask, last)][1]
        mask = next_mask

    caminho.append(0)
    return res[0], caminho

def vizinho_mais_proximo_tsp(grafo, inicio=0):

    n = len(grafo)
    visitados = {inicio}
    caminho = [inicio]
    custo_total = 0

    atual = inicio
    while len(visitados) < n:
	
        proximos = [(grafo[atual][vizinho], vizinho) for vizinho in range(n) if vizinho not in visitados]
		
        menor_distancia, proximo = min(proximos)
        caminho.append(proximo)
        visitados.add(proximo)
        custo_total += menor_distancia
        atual = proximo

    custo_total += grafo[atual][inicio]
	
    caminho.append(inicio)
    return custo_total, caminho


grafo = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Held-Karp
print("Held-Karp (Força Bruta):")
custo_exato, caminho_exato = held_karp_tsp(grafo)
print(f"Custo: {custo_exato}, Caminho: {caminho_exato}")

# Vizinho Mais Próximo
print("\nVizinho Mais Próximo:")
custo_guloso, caminho_guloso = vizinho_mais_proximo_tsp(grafo)
print(f"Custo: {custo_guloso}, Caminho: {caminho_guloso}")

# Algoritmo Genético
print("\nAlgoritmo Genético:")
custo_genetico, caminho_genetico = algoritmo_genetico_tsp(grafo)
print(f"Custo: {custo_genetico}, Caminho: {caminho_genetico}")