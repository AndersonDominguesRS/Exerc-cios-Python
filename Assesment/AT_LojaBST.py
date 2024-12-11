class Node:
    def __init__(self , chave ):

        print(f"Chave informada: { chave}")
        self.chave = chave
        self.esquerda = None
        self.direita = None

class LOJA_BST:
    def __init__(self) :
        self.raiz = None

    def inserir( self , chave):
        print( f"Chave informada inserir: {chave}")
        if self.raiz is None:
            self.raiz = Node(chave)

        else:
            self._inserir(self.raiz, chave )

    def _inserir(self, no_atual, chave) :
        print(f" Chave informada _inserir: {chave}")
        if chave < no_atual.chave:
            if no_atual.esquerda is None :
                no_atual.esquerda =  Node( chave)
            else:
                self._inserir(no_atual.esquerda, chave)
        else:

            if no_atual.direita is None:
                no_atual.direita = Node(chave)

            else:
                self._inserir(no_atual.direita, chave )

    def pesquisar(self, chave):
        print(f"Chave informada para pesquisa: {chave}")
        return self._pesquisar(self.raiz, chave)

    def _pesquisar(self, no_atual, chave):
        print(f"Chave informada para _pesquisa: {chave}")
        if no_atual is None:
            return False
        if chave == no_atual.chave:
            return True
        elif chave < no_atual.chave:
            return self._pesquisar(no_atual.esquerda, chave)
        else:
            return self._pesquisar(no_atual.direita, chave)
			
			
loja_bst = LOJA_BST()
listas_de_precos = [
    [100, 50, 150, 30, 70, 130, 170],
    [100, 50, 150, 30, 70, 130, 170],
    [100, 50, 150, 30, 70, 130, 170]
]

for precos in listas_de_precos:
    for preco in precos:
        loja_bst.inserir(preco)

preco_procurado = 70
disponivel = loja_bst.pesquisar(preco_procurado)
if disponivel:
    print(f"o valor {preco_procurado} esta disponível")
else:
    print(f"o valor {preco_procurado} não esta disponível")