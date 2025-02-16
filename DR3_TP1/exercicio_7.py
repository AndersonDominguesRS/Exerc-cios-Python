class TrieNode:
    def __init__(self):
        self.filhos = {}
		
        self.e_fim = False

class Trie:

    def __init__(self):
        self.raiz = TrieNode()

    def inserir(self, palavra):
	
        no_atual = self.raiz
        for char in palavra:
		
            if char not in no_atual.filhos:
                no_atual.filhos[char] = TrieNode()
            no_atual = no_atual.filhos[char]
        no_atual.e_fim = True

    def buscar(self, palavra):
	
	
        no_atual = self.raiz
        for char in palavra:
		
            if char not in no_atual.filhos:
                return False
            no_atual = no_atual.filhos[char]
        return no_atual.e_fim 


