grafo = {
    'Moinhos de Vento': ['Centro Histórico', 'Cidade Baixa'],
    'Centro Histórico': ['Moinhos de Vento', 'Menino Deus'],
    'Cidade Baixa': ['Moinhos de Vento', 'Menino Deus', 'Cristal'],
    'Menino Deus': ['Centro Histórico', 'Cidade Baixa'],
    'Cristal': ['Cidade Baixa', 'Tristeza'],
    'Tristeza': ['Cristal']
}


for bairro, conexoes in grafo.items():
    print(f"Bairro {bairro} está conectado com: {', '.join(conexoes)}")
