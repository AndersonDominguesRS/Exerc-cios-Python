def pop(self):
       if len(self.heap) == 0:
           
           return None
       if len(self.heap) == 1:
           return self.heap.pop()

       root = self.heap[0]
       self.heap[0] = self.heap.pop()
       self.heapify_down(0)
       print("finalizado")
       return root