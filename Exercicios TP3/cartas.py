from random import shuffle

espadas = ['A' , 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J' , 'Q'  , 'K' ]

def embaralhar (cartas):
    shuffle(cartas)
    return cartas

def ordenar (cartas):
    contador=1
    ordenada=[]
    letra=0

    while len(ordenada) <13:
        for n in cartas:
            if n=='A':
                letra=1                
            if n=='J':
                letra=11
            if n=='Q':
                letra=12
            if n=='K':
                letra=13
            if n == contador or letra ==contador:
                contador= contador+1
                ordenada.append(n)
                letra=0
                print (ordenada)        

print (embaralhar(espadas))
ordenar(espadas)