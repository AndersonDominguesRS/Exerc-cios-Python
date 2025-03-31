import itertools

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