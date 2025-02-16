class NoTrie:

    def __init__(self):
        self.filhos = {}
        self.eh_fim_da_palavra = False

class Trie:

    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra):
	
        no = self.raiz
		
        for char in palavra:
            if char not in no.filhos:
                no.filhos[char] = NoTrie()
            no = no.filhos[char]
        no.eh_fim_da_palavra = True

    def buscar(self, palavra):
	
        no = self.raiz
		
        for char in palavra:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return no.eh_fim_da_palavra

    def comeca_com(self, prefixo):
	
        no = self.raiz
		
        for char in prefixo:
            if char not in no.filhos: 
                return []
            no = no.filhos[char]
        
        return self._encontrar_palavras_com_prefixo(no, prefixo)

    def _encontrar_palavras_com_prefixo(self, no, prefixo): 
	
        palavras = []
        if no.eh_fim_da_palavra:
            palavras.append(prefixo)
        for char, no_filho in no.filhos.items():
            palavras.extend(self._encontrar_palavras_com_prefixo(no_filho, prefixo + char))
        return palavras 


