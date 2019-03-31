"""
Christopher Ijams
Skip List
Linear, sorted single pointer data structure of non-contiguous memory location.
Sacrifices speed of adding elements for fast lookup via express lanes.
"""


class PySkipList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        curr = self.head
        definition = ""
        while curr:
            definition += str(curr.data) + ", "
            curr = curr.next
        return definition[:-2]

    # Adds a value to the linked list.
    def add(self, data):
        if not self.head:
            self.head = self._Node(data)
        else:
            prev = self.head
            curr = self.head.next
            while curr:
                if curr.data < data:
                    prev = prev.next
                    curr = curr.next


    # enforces express lane rules for optimal look up.
    def express(self):
        pass

    # Returns the _node that contains the specified data. Uses express lanes.
    def get(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    # Return the size of the list.
    def size(self):
        count = 0
        curr = self.head
        while curr:
            curr = curr.next
            count = count + 1
        return count

    # Removes an element from the list.
    def remove(self, data):
        curr = self.head
        try:
            if curr.data == data:
                self.head = self.head.next
                return True
            while curr:
                if curr.next.data == data:
                    curr.next = curr.next.next
                    return True
                curr = curr.next
        except AttributeError:
            return False

    # Clears the list.
    def clear(self):
        self.head = None

    # _Node class for data storage and link.
    class _Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
