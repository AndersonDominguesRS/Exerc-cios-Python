class HeapMinima:
    def __init__(self):
	
        self.heap = [] 

    def inserir_pacote(self, id_pacote, prioridade, tempo_transmissao) :
        self.heap.append((prioridade, id_pacote, tempo_transmissao))
        self._subir(len(self.heap) - 1)

    def remover_pacote_mais_prioritario(self) :
        if not self.heap:
            print("Heap está vazia.")
            return None
        pacote_prioritario = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._descer(0)
		
        return pacote_prioritario

    def atualizar_prioridade(self, id_pacote, nova_prioridade):
	
        for i, (prioridade, id_, tempo) in enumerate(self.heap):
            if id_ == id_pacote:
                self.heap[i] = (nova_prioridade, id_pacote, tempo)
                self._subir(i)
                self._descer(i)
                break

    def _subir(self, indice):
        while indice > 0:
		
            pai = (indice - 1) // 2
            if self.heap[indice][0] < self.heap[pai][0]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def _descer(self, indice):
        tamanho = len(self.heap)
		
        while True:
		
            menor = indice
            esquerda = 2 * indice + 1
            direita = 2 * indice + 2

            if esquerda < tamanho and self.heap[esquerda][0] < self.heap[menor][0]:
                menor = esquerda
            if direita < tamanho and self.heap[direita][0] < self.heap[menor][0]:
                menor = direita

            if menor != indice:
                self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
                indice = menor
            else:
                break

    def listar_pacotes(self):
        print("Pacote na heap:" )
        for prioridade, id_pacote, tempo in self.heap:
            print(f"ID: {id_pacote}, Prioridade: {prioridade}, Tempo: {tempo}")

heap = HeapMinima()

# pacotes
heap.inserir_pacote(1, 3, 10)  # ID: 1, Prioridade: 3, Tempo: 10
heap.inserir_pacote(2, 1, 5)   # ID: 2, Prioridade: 1, Tempo: 5
heap.inserir_pacote(3, 2, 8)   # ID: 3, Prioridade: 2, Tempo: 8

# listar pacotes
heap.listar_pacotes()

# Remover pacote maior prioridade
print("Removendo o pacote de maior prioridade...")
pacote_removido = heap.remover_pacote_mais_prioritario()
print(f"Pacote removido: {pacote_removido}")

# Atualizar prioridade pacote
print("Atualizando a prioridade do pacote com ID 3...")
heap.atualizar_prioridade(3, 0)

# Listar pacotes novamente
heap.listar_pacotes()