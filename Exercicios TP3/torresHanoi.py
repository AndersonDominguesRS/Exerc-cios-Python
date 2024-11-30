def torre_hanoi(i, origem, destino, auxiliar):
    if i ==1:
        print(f"Mova o disco 1 de {origem} para {destino}")
    else:
        torre_hanoi(i -1, origem, auxiliar, destino)
        print(f"Mova o disco {n} de {origem} para {destino}")
        torre_hanoi(n-1, auxiliar, destino, origem)