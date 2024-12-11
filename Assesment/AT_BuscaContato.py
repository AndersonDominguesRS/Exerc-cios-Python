def pesquisa_nome(contatos, nome_procurado):
    contato_encontrado=""
    telefone_encontrado=""
    for contato in contatos:
        if contato["nome"].lower() == nome_procurado.lower():
             contato_encontrado=nome_procurado
             telefone_encontrado=contato["telefone"]

    
    if contato_encontrado:
        print(f"Contato: {contato_encontrado} ---- Telefone: {telefone_encontrado}")

    else:
        print("Contato não localizado")


