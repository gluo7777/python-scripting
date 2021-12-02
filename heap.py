class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def parent(self, childIndex: int) -> int:
        """\
        Returns index of parent
        """
        if childIndex % 2 == 1: # left child
            return int((childIndex - 1) / 2)
        else: # right child
            return int((childIndex - 2) / 2)

    def leftChild(self, parentIndex: int) -> int:
        index = 2 * parentIndex + 1
        return index if index < len(self.heap) else -1

    def rightChild(self, parentIndex: int) -> int:
        index = 2 * parentIndex + 2
        return index if index < len(self.heap) else -1

    def swap(self,i: int, j: int) -> None:
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def insert(self,val: int) -> None:
        print(f'Inserting {val} into {self.heap}')
        self.heap.append(val)
        index = len(self.heap) - 1
        while index != 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index,self.parent(index))
            index = self.parent(index)
        print(f'Heap after insertion: {self.heap}')

    def extract_min(self) -> int:
        print(f'Removing root element from {self.heap}')
        if len(self.heap) == 0:
            raise IndexError('Heap is empty')
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        nextIndex = 0
        # while nextIndex < len(self.heap):
        #     leftChild = self.leftChild(nextIndex)
        #     if leftChild == -1:
        #         break
        #     if self.heap[nextIndex] > self.heap[leftChild]:
        #         self.swap(nextIndex,leftChild)
        #     nextIndex = self.rightChild(nextIndex)
        #     if rightChild == -1:
        #         break
        #     if self.heap[nextIndex] > self.heap[rightChild]:
        #         self.swap(nextIndex,rightChild)
            

        print(f'Heap after extract_min: {self.heap}')
        return root

if __name__ == "__main__":
    minheap = MinHeap()
    minheap.insert(5)
    minheap.insert(4)
    minheap.insert(3)
    minheap.insert(9)
    minheap.insert(6)
    minheap.insert(11)
    minheap.insert(-100)
    minheap.insert(4)