lista= [17, 2, 99, 15, 3, 60, 4, 5, 20, 6, 7, 8, 9, 10, 40]

def greatestNumber(lista):
    teste=0
    for n in lista:
        if teste <n:
            teste=n

    print(teste)

greatestNumber(lista)