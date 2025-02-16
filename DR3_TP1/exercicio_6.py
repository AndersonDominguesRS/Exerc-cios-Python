class MinHeap:
    def __init__(self):
        self.heap = []
    def parent(self, index):
        return (index - 1) // 2
    def left_child(self, index):
        return 2 * index + 1 #Mudar

    def right_child(self, index):
	
        return 2 * index + 2

    def insert(self, key):
        self.heap.append(key)
		
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)][0] > self.heap[index][0]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def pop(self):
        if len(self.heap) == 0:
            return None
			
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, index):
        inferior = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left][0] < self.heap[inferior][0]:
            inferior = left
			
        if right < len(self.heap) and self.heap[right][0] < self.heap[inferior][0]:
            inferior = right
			
        if inferior != index:
            self.heap[inferior], self.heap[index] = self.heap[index], self.heap[inferior]
            self.heapify_down(inferior)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def display(self):
        print([tarefa for prioridade, tarefa in self.heap])

class Task:
    def __init__(self):
        self.min_heap = MinHeap()

    def add_tarefa(self, prioridade, tarefa):
        self.min_heap.insert((prioridade, tarefa))

    def get_next_tarefa(self):
        return self.min_heap.pop()[1] if not self.min_heap.is_empty() else None

    def display_tarefas(self):
        self.min_heap.display()


