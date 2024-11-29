def livros_impares(lista): 
    total=0
    for i in lista:
        if i % 2 != 0:
            total=total+1
    print(total)

lista_teste=[10,8,5, 1,4,9 ,3 ,6]

livros_impares(lista_teste)