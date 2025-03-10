grafo = {
    'Centro': ['Bairro A', 'Bairro B'],
    'Bairro A': ['Centro', 'Bairro C'],
    'Bairro B': ['Centro', 'Bairro C'],
    'Bairro C': ['Bairro A', 'Bairro B', 'Bairro D'],
    'Bairro D': ['Bairro C']
}


def consultar_vizinhos(bairro):
    if bairro in grafo:
        return f"Bairros vizinhos de {bairro}: {', '.join(grafo[bairro])}"
    else:
        return f"Bairro {bairro} não encontrado no grafo."


bairro_consulta = 'Bairro C'
print(consultar_vizinhos(bairro_consulta))
