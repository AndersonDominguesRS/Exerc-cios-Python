def invert_fila(pilha):
    fila_inversa=[]
    for i in pilha:
        fila_inversa.insert(0,i)
    print (fila_inversa)



pilha_teste=[10,9,8,7,6,5,4,3,2,1]

invert_fila(pilha_teste)