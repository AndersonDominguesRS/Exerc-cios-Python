import time

N = 8


movimentos_cavalo = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def eh_valido(x, y, tabuleiro):
    return 0 <= x < N and 0 <= y < N and tabuleiro[x][y] == -1

def resolver_forca_bruta(x, y, movimento, tabuleiro):

    if movimento == N * N:  # Todas as casas foram visitadas
        return True

    for dx, dy in movimentos_cavalo :
	
        nx, ny = x + dx, y + dy
		
        if eh_valido(nx, ny, tabuleiro): 
            tabuleiro[nx][ny] = movimento
			
            if resolver_forca_bruta(nx, ny, movimento + 1, tabuleiro):
                return True
            tabuleiro[nx][ny] = -1 

    return False

def iniciar_forca_bruta():
    tabuleiro = [[-1 for _ in range(N)] for _ in range(N)]
    tabuleiro[0][0] = 0
	
    if resolver_forca_bruta(0, 0, 1, tabuleiro):
        return tabuleiro
		
    else:
        return None


inicio = time.time()
solucao_forca_bruta = iniciar_forca_bruta()
fim = time.time()

print("Solução (Força Bruta):")
if solucao_forca_bruta:
    for linha in solucao_forca_bruta:
        print(linha)
else:
    print("Nenhuma solução encontrada.")
print(f"Tenpo de execução (força bruta): {fim - inicio:.4f} segundos")