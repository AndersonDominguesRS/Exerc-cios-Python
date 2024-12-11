class Node:
    def __init__(self , chave ):

        print(f"Chave informada: { chave}")
        self.chave = chave
        self.esquerda = None
        self.direita = None

class INVENTARIOBST:

    def __init__( self):
       
       self.raiz = None

    def inserir(self, chave):

        if self.raiz is None:
            self.raiz = Node(chave)
        else:
            self._inserir(self.raiz, chave)

    def _inserir(self, no_atual, chave):

        if chave < no_atual.chave:
            if no_atual.esquerda is None:
                no_atual.esquerda = Node(chave)
            else:
                self._inserir(no_atual.esquerda, chave )

        else:
            if no_atual.direita is None:
                no_atual.direita = Node(chave)
            else:
                self._inserir(no_atual.direita, chave)

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no_atual, chave):
        if no_atual is None:
            return no_atual

        if chave < no_atual.chave:
            no_atual.esquerda = self._remover(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._remover(no_atual.direita, chave)
        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda

            no_atualizado = self._min_value_node(no_atual.direita)
            no_atual.chave = no_atualizado.chave
            no_atual.direita = self._remover(no_atual.direita, no_atualizado.chave)

        return no_atual

    def _min_value_node(self, no_atual):

        atual = no_atual
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def inorder(self, no_atual, resultado):

        if no_atual:
            self.inorder(no_atual.esquerda, resultado)
            resultado.append(no_atual.chave)
            self.inorder(no_atual.direita, resultado)

    def exibir_inorder(self ):

        resultado = []
        self.inorder(self.raiz, resultado)
        return resultado


inventario_bst = INVENTARIOBST()
lista_codigos = [45, 25, 65, 20, 30, 60, 70]

for codigo in lista_codigos:
    inventario_bst.inserir(codigo)

print("Ordem antes das remoções:", inventario_bst.exibir_inorder())
inventario_bst.remover(20)
print("Ordem crescente após remover 20:", inventario_bst.exibir_inorder())
inventario_bst.remover(25)
print(" Ordem crescente após remover 25:", inventario_bst.exibir_inorder())
inventario_bst.remover(45)
print("Ordem crescente após remover 45:", inventario_bst.exibir_inorder() )
