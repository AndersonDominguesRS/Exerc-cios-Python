def selection_sort(jogadores):
    n = len(jogadores)  # Determinando o tamanho da lista
    for i in range(n):  #Iniciando o for para procurar um item na lista
        indice_menor = i
        for j in range(i + 1, n): # Neste for é percorrido a parte não ordenada da lista infomada
            if jogadores[j]['pontuacao'] < jogadores[indice_menor]['pontuacao']:
                indice_menor = j
        jogadores[i], jogadores[indice_menor] = jogadores[indice_menor], jogadores[i] #Neste ponto do código é realizada 
        #a troca entre o maior e o mennor número encontrado
    return jogadores

