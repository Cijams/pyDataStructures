class PySet:
    def __init__(self, head=None):
        self.head = head

    # Adds an element to the set.
    def add(self, data=None):
        if not self.contains(data):
            curr_node = self._Node(data)
            curr_node.next = self.head
            self.head = curr_node

    # Returns True if the set contains the data.
    def contains(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    # Remove an element from the set.
    def remove(self, data):
        curr = self.head
        try:
            if curr.data == data:
                self.head = curr.next
                return True
            while curr:
                if curr.next.data == data:
                    curr.next = curr.next.next
                    return True
                curr = curr.next
        except AttributeError:
            return False

    # Prints the set
    def iterate(self):
        return_set = set()
        curr = self.head
        while curr:
            return_set.add(curr.data)
            curr = curr.next
        return return_set

    # Finds an element in the set and alters the value.
    def change(self, data, mod):
        curr = self.head
        while curr:
            if curr.data == data:
                curr.data = mod
                break
            curr = curr.next

    # Returns the length of the set.
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    # Clears the set.
    def clear(self):
        self.head = None

    # Node class for linking and data storage.
    class _Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
