
def heapify_up(heap,index):
    parent = (index-1)//2
    if parent >=0 and heap[parent]> heap[index]:
        heap[parent],heap[index] = heap[index],heap[parent]
        heapify_up(heap,parent)
        
def heapify_down(heap,index,heap_size):
    left = index * 2 + 1 
    right = index * 2 + 2
    smallest = index 
    if left < heap_size and heap[left] < heap[smallest]:
        smallest = left
    if right < heap_size and heap[right]< heap[smallest]:
        smallest = right
    if smallest != index:
        heap[index],heap[smallest] = heap[smallest],heap[index]
        heapify_down(heap,smallest,heap_size)

class minheap:
    def __init__(self) :
        self.heap = []
    def insert(self,value):
        self.heap.append(value)
        heapify_up(self.heap,len(self.heap)-1)
    
    def delete(self):
        if self.heap is None:
            print('it is empty')
            return
        min_val = self.heap[0]
        self.heap[0]=self.heap[-1]
        heapify_down(self.heap,0,len(self.heap))
    

root = minheap()
root.insert(4)
root.insert(8)
root.insert(1)
root.insert(9)
root.insert(3)
root.insert(2)
root.delete()
print(root.heap)