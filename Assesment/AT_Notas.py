class Node:
    def __init__(self , chave ):

        print(f"Chave informada: { chave}")
        self.chave = chave
        self.esquerda = None
        self.direita = None

class BUSCANOTA:
    def __init__(self ) :
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
                self._inserir (no_atual.esquerda, chave)

        else:
            if no_atual.direita is None:
                no_atual.direita = Node(chave)

            else:
                self._inserir(no_atual.direita, chave)

    def buscar_minimo(self ):
        return self._buscar_minimo(self.raiz)

    def _buscar_minimo(self, no_atual):
        while no_atual.esquerda is not None :
            no_atual = no_atual.esquerda
        return no_atual.chave

    def buscar_maxximo(self):
        return self._buscar_maxximo(self.raiz)

    def _buscar_maxximo(self, no_atual):

        while no_atual.direita  is not None:
            no_atual = no_atual.direita
        return no_atual.chave 
		
busca_nota = BUSCANOTA()
lista_notas = [85, 70, 95, 60, 75, 90, 100]

for nota in lista_notas:
    busca_nota.inserir(nota)

nota_minima = busca_nota.buscar_minimo()
nota_maxima = busca_nota.buscar_maxximo()
print(f"Nota mínima localizada: { nota_minima }")
print(f"Nota máxima localizada: { nota_maxima }")

