class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None

class Trie :
    def __init__(self):
        self.root = TrieNode( )

    def inserir(self, palavra):
        node = self.root
        for char in palavra:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = palavra

    def autocompletar(self, prefixo):
        node = self.root
        for char in prefixo:
		
            if char not in node.children:
                return [] 
            node = node.children[char]
        return self._buscar_palavras(node)

    def _buscar_palavras(self, node):
	
        palavras = []
        if node.is_end_of_word:
            palavras.append(node.word)
        for char, filho in node.children.items():
            palavras.extend(self._buscar_palavras(filho))
        return palavras

    def correcao_automatica(self, palavra, limite_distancia=2):
        sugestoes = []
        self._busca_similar(self.root, palavra, "", 0, limite_distancia, sugestoes)
		
        return sugestoes

    def _busca_similar(self, node, palavra, caminho, dist, limite, sugestoes):
        if dist > limite:
            return
        if node.is_end_of_word and self._distancia_levenshtein(caminho, palavra) <= limite:
            sugestoes.append(caminho)
        for char, filho in node.children.items():
            self._busca_similar(filho, palavra, caminho + char, dist, limite, sugestoes)

    def _distancia_levenshtein(self, palavra1, palavra2):
        len1, len2 = len(palavra1), len(palavra2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif palavra1[i - 1] == palavra2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[len1][len2]
    
trie = Trie()

# Inserção livros na Trie
livros = [
    "Dom Quixote",
    "A Divina Comédia",
    "Orgulho e Preconceito",
    "O Morro dos Ventos Uivantes",
    "Cem Anos de Solidão",
    "O Pequeno Príncipe",
    "A Revolução dos Bichos"
]
for livro in livros:
    trie.inserir(livro)

# autocompletar
print("Sugestões de autocompletar para 'O':")
print(trie.autocompletar("O"))

# Correção 
print("\nSugestões de correção para 'Revolucao':")
print(trie.correcao_automatica("Revolucao"))