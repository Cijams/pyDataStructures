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

    def get_min(self):
        pass

    def extract_min(self):
        pass

    def decrease_key(self):
        pass

    def insert(self):
        pass
        self.size += 1

    def delete(self):
        pass

    def heapify(self):
        pass

    def heap_sort(self):
        pass

    def get_left(self, index):
        try:
            return self.heap[index*2+1]
        except IndexError:
            return None

    def get_right(self, index):
        try:
            return self.heap[index*2+2]
        except IndexError:
            return None

    def get_parent(self, index):
        try:
            return self.heap[index/2]
        except IndexError:
            return None
