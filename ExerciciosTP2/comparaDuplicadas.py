def busca_duplicadas(lista):
    lista_teste=[]
    for i in lista:
        if i not in lista_teste:
            lista_teste.append(i)


    print (lista_teste)

teste=[2,2,3,6,45,2,8,9,9,15,15,20,2,16,14,45,9]

busca_duplicadas(teste)
