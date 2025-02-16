class MinHeap:
    def __init__(self):
        self.heap = []
		
		

    def parent(self, posicao):
        return (posicao - 1) // 2
		

    def left_child(self, posicao):
        return 2 * posicao + 1
		

    def right_child(self, posicao):
        return 2 * posicao + 2
		

    def insert(self, chave):
        self.heap.append(chave)
        self.heapify_up(len(self.heap) - 1) 
		
		

    def heapify_up(self, posicao):
        while posicao != 0 and self.heap[self.parent(posicao)] > self.heap[posicao]:
            self.heap[self.parent(posicao)], self.heap[posicao] = self.heap[posicao], self.heap[self.parent(posicao)]
            posicao = self.parent(posicao)

    def remove_min_test(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        pai = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return pai

    def heapify_down(self, posicao):
        smallest = posicao
        left = self.left_child(posicao)
        right = self.right_child(posicao)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != posicao:
            self.heap[smallest], self.heap[posicao] = self.heap[posicao], self.heap[smallest]
            self.heapify_down(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None
		
		
		

    def size(self): #VERIFICAR
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
    def display(self):
        print(self.heap)



min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(6)
min_heap.insert(5)
min_heap.insert(2)
min_heap.insert(4)

min_heap.display()  # [1, 2, 4, 5, 3, 6]
print("Finalizado")
print(min_heap.remove_min_test())  # 1
min_heap.display()  # [2, 3, 4, 5, 6]
