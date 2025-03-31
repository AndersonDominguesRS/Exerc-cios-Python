import time

N = 8

movimentos_cavalo = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def eh_valido(x, y, tabuleiro):
    return 0 <= x < N and 0 <= y < N and tabuleiro[x][y] == -1

def resolver_forca_bruta(x, y, movimento, tabuleiro):

    if movimento == N * N:
        return True



def movimento_com_menor_grau(x, y, tabuleiro) :

    menor_grau = float('inf')
    proximo_movimento = None

    for dx, dy in movimentos_cavalo:
	
        nx, ny = x + dx, y + dy
		
        if eh_valido(nx, ny, tabuleiro):
            grau = sum(1 for mx, my in movimentos_cavalo if eh_valido(nx + mx, ny + my, tabuleiro))
            if grau < menor_grau:
                menor_grau = grau
                proximo_movimento = (nx, ny)

    return proximo_movimento

def resolver_com_heuristica(x, y, tabuleiro):

    for movimento in range(1, N * N):
        proximo = movimento_com_menor_grau(x, y, tabuleiro)
        if not proximo:
            return False
        x, y = proximo
        tabuleiro[x][y] = movimento
    return True

def iniciar_com_heuristica():
    tabuleiro = [[-1 for _ in range(N)] for _ in range(N)]
    tabuleiro[0][0] = 0 
	
    if resolver_com_heuristica(0, 0, tabuleiro):
        return tabuleiro
    else:
        return None


inicio = time.time()
solucao_heuristica = iniciar_com_heuristica()
fim = time.time()

print("\nSolução (Heurística do Menor Grau):")

if solucao_heuristica:
    for linha in solucao_heuristica:
        print(linha)
else:
    print("Nenhuma solução encontrada.")
print(f"Tempo de execução (heurística): {fim - inicio:.4f} segundos" )