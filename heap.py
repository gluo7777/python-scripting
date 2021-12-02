from binarytree import Node,build

class MinHeap:
    def __init__(self) -> None:
        self.heap = []
        # helper functions
        ## left child
        self.leftChildIndex = lambda i : 2 * i + 1
        self.leftChild = lambda i : self.heap[self.leftChildIndex(i)]
        self.hasLeftChild = lambda i : self.leftChildIndex(i) < len(self.heap)
        ## right child
        self.rightChildIndex = lambda i : 2 * i + 2
        self.rightChild = lambda i : self.heap[self.rightChildIndex(i)]
        self.hasRightChild = lambda i : self.rightChildIndex(i) < len(self.heap)
        ## parent
        self.parentIndex = lambda i : int((i - 1) / 2) if i % 2 == 1 else int((i - 2) / 2)
        self.parent = lambda i : self.heap[self.parentIndex(i)]
        self.hasParent = lambda i : self.parentIndex(i) >= 0
    
    def printTree(self, header: str = None) -> None:
        binary_tree = build(self.heap)
        if header:
            print(header)
        print(binary_tree)

    def swap(self,i: int, j: int) -> None:
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def insert(self,val: int) -> None:
        print(f'Inserting {val}')
        self.heap.append(val)
        index = len(self.heap) - 1
        while self.hasParent(index) and self.heap[index] < self.parent(index):
            self.swap(index,self.parentIndex(index))
            index = self.parentIndex(index)
        self.printTree('Heap after insertion')

    def extract_min(self) -> int:
        return self.delete(0)
    
    def delete(self, index: int) -> int:
        print(f'Deleting element at index: {index}')
        if index >= len(self.heap):
            raise IndexError(f'Index ({index}) >= heap size ({len(self.heap)})')
        node_to_remove = self.heap[index]
        self.heap[index] = self.heap.pop()
        while self.hasLeftChild(index):
            minChild = self.leftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                minChild = self.rightChildIndex(index)
            if self.heap[minChild] >= self.heap[index]:
                break
            self.swap(minChild,index)
            index = minChild
        self.printTree('Heap after deletion')
        return node_to_remove

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
    minheap.printTree('Tree after all insertions')
    minheap.delete(1)
    minheap.extract_min()
    minheap.extract_min()
    minheap.extract_min()
    minheap.extract_min()
    