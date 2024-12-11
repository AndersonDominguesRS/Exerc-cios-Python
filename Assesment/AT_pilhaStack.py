class Teste:
    def __init__(self ):
        
        self.pilha_atual = []
        self.pilha_retornar = []
        self.pilha_avancar = []

    def nova_pagina(self, endereco ):
        if self.pilha_atual:

            self.pilha_retornar.append(self.pilha_atual.pop())
        self.pilha_atual.append(endereco)
        self.pilha_avancar.clear()

    def retornar(self):
        if not self.pilha_retornar:

            return
        self.pilha_avancar.append(self.pilha_atual.pop())
        self.pilha_atual.append( self.pilha_retornar.pop())

    def avancar(self):
        if not self.pilha_avancar:

            return
        self.pilha_retornar.append( self.pilha_atual.pop() )
        self.pilha_atual.append( self.pilha_avancar.pop())

