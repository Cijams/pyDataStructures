"""
Christopher Ijams
Map
Associative container storing key value pairs.
"""


class PyMap:
    def __init__(self):
        self.head = None

    def __str__(self):
        hm = ""
        while self.head:
            hm += "{" + str(self.head.key) + ": " + str(self.head.value) + "}"
            hm += ", "
            self.head = self.head.next
        hm = hm[:-2]
        return hm

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def put(self, key=None, value=None):
        if self.head:
            curr = self._Node(key, value)
            curr.next = self.head
            self.head = curr
        else:
            self.head = self._Node(key, value)


    def get(self):
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def pop(self):
        pass

    def remove(self):
        pass

    class _Node:
        def __init__(self, key=None, value=None):
            self.next = None
            self.key = key
            self.value = value

