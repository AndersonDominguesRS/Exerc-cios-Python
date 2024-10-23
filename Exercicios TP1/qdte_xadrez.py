graos=0

def verquadrado(graos):
    quadrado=1
    while graos !=1:
        graos= graos/2
        quadrado=quadrado+1
    print ("Quantidade de quadrados:", quadrado)


graos=16
verquadrado(graos)