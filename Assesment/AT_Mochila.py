def mochila(W, pesos, valor, n):
    print(pesos)
    print(valor)
    print(n)
    K = [[0 for x in range(W + 1)] for x in range(n + 1) ]
    for i in range(n + 1) :

        for w in range(W + 1):
            if i == 0  or w == 0:
                K[i][w] = 0
            elif  pesos[i-1] <= w:
                K[i][w] = max(valor[i-1] + K[i-1][w-pesos[i-1]], K[i-1][w])


            else:

                K[i][w] = K[i-1][w]

    return K[n][W]