class GrafoKruskal:
    def __init__(self, vertices) :
        self.vertices = vertices
		
        self.arestas = []

    def adicionar_aresta(self, u, v, peso):
	
        self.arestas.append((peso, u, v))

    def encontrar(self, pai, vertice):
		#print(pai)
	
        if pai[vertice] == vertice:
            return vertice
        return self.encontrar(pai, pai[vertice])

    def unir(self, pai, rank, vertice1, vertice2):
	
        raiz1 = self.encontrar(pai, vertice1)
        raiz2 = self.encontrar(pai, vertice2)

        if rank[raiz1] < rank[raiz2] :
            pai[raiz1] = raiz2
        elif rank[raiz1] > rank[raiz2]:
            pai[raiz2] = raiz1
        else:
            pai[raiz2]  = raiz1
            rank[raiz1] += 1

    def kruskal_mst(self): 
        mst = []
		
        self.arestas.sort( )
        pai = {}
        rank = {}

        for vertice in self.vertices:
		
            pai[vertice] = vertice
            rank[vertice] = 0

        for peso, u, v in self.arestas:
		
            if self.encontrar(pai, u) != self.encontrar(pai, v):
			
			
                self.unir(pai, rank, u, v)
                mst.append((u, v, peso))

        return mst
		
# krukal
grafo_kruskal = GrafoKruskal(['A', 'B', 'C', 'D', 'E'])
grafo_kruskal.adicionar_aresta('A', 'B', 1)
grafo_kruskal.adicionar_aresta('A', 'C', 3)
grafo_kruskal.adicionar_aresta('B', 'C', 1)
grafo_kruskal.adicionar_aresta('B', 'D', 4)
grafo_kruskal.adicionar_aresta('C', 'D', 2)
grafo_kruskal.adicionar_aresta('C', 'E', 5)
grafo_kruskal.adicionar_aresta('D', 'E', 1)

mst_kruskal = grafo_kruskal.kruskal_mst()
print("MST (Kruskal):", mst_kruskal)
