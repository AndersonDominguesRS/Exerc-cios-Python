fila=["carlos","Roberto"]

def adicionar_cliente(nome):
    fila.append(nome)

def atender_cliente():
    print (fila[0])
    fila.remove(fila[0])

def tamanho_fila(fila):
    print (len(fila))

print(fila)
atender_cliente()
print(fila)
tamanho_fila(fila)