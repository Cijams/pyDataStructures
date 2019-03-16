"""
Christopher Ijams
Min Heap
Array-based implementation of a complete binary tree data
structure that satisfies the min heap property.
"""


class PyMinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    # Returns the minimum value from the heap.
    def get_min(self):
        return self.heap[0]

    # Removes the minimum value from the heap.
    def extract_min(self):
        pass
        self.size -= 1

    #
    def decrease_key(self):
        pass

    # Inserts a value into the heap.
    def insert(self, data):
        pass
        self.heap.append(data)
        self.size += 1

    # Removes a value from the heap.
    def delete(self, data):
        pass
        self.size -= 1

    # Enforces min heap order.
    def heapify(self, parr, left, right):
        smallest = parr
        if left:
            if smallest > left:
                smallest, left = left, smallest

    # Uses heapify on the heap to sort all of the data.
    def heap_sort(self):
        pass

    # Returns the left child of the node.
    def get_left(self, index):
        try:
            return self.heap[index*2+1]
        except IndexError:
            return None

    # Returns the right child of the node.
    def get_right(self, index):
        try:
            return self.heap[index*2+2]
        except IndexError:
            return None

    # Returns the parent of the node.
    def get_parent(self, index):
        try:
            return self.heap[index/2]
        except IndexError:
            return None
