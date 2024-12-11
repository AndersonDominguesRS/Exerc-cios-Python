class FilaQueue:
    def __init__(self):
        self.fila = []

    def novo_chamado(self, chamado):
        print(chamado)
        self.fila.append(chamado)
        print("Chamado criado")

    def remover_chamado(self):
        if not self.fila:

            print("Chamado não encontrado")
            return None
        chamado = self.fila.pop(0)

        print("Chamado removido")
        return chamado

    def exibir_fila(self):
        if not self.fila:
            print("Sem chamados na fila")

        else:
            print( "Fila de chamados existentes:" )
            for chamado in self.fila:
                print(f"- {chamado}"  )

fila = FilaQueue()
fila.novo_chamado(" Chamdo 031220242350")
fila.novo_chamado(" Chamado 041220242350")

fila.exibir_fila()
fila.remover_chamado()
fila.exibir_fila()
fila.remover_chamado()
fila.exibir_fila()


