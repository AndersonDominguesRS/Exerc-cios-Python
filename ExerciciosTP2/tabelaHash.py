lista={}

def inserir(chave, valor):
    lista[chave]= valor

    print (lista)

def buscar_chave(chave):
    print (lista[chave])

def remove(chave):
    del lista[chave]

inserir('teste', 1)
buscar_chave('teste')
