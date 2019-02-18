class PyLinkedList:
    def __init__(self, head=None):
        self.head = head

    # Add an element to the list.
    def add(self, data=None):
        curr__node = self._Node(data)
        curr__node.next = self.head
        self.head = curr__node

    # Return the size of the list.
    def size(self):
        count = 0
        curr = self.head
        while curr:
            curr = curr.next
            count = count + 1
        return count

    # Returns true if the list has the data.
    def contains(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    # Returns the _node that contains the specified data.
    def get(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    # Returns the first element in the list.
    def get_first(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.data

    # Returns the last element in the list.
    def get_last(self):
        return self.head.data

    # Returns a list of the pySinglyLinkedList
    def iterate(self):
        _node_list = []
        curr = self.head
        while curr:
            _node_list.append(curr.data)
            curr = curr.next
        _node_list.reverse()
        return _node_list

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

    # Returns the middle of the list.
    def middle(self):
        if self.head:
            fast = slow = self.head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow.data

    # Removes duplicates from the list.
    def remove_duplicates(self):
        values = set(self.iterate())
        self.head = None
        for _ in values:
            self.add(_)
        return True

    # Changes the data in a specified _node in the list.
    def modify__node(self, index, data):
        mod = self.get(index)
        mod.data = data

    # Detects loops in the list.
    def detect_loop(self):
        node_map = {}
        curr = self.head

        while curr:
            if node_map.get(curr):
                node_map[curr] = node_map[curr]+1
            else:
                node_map[curr] = 1
            curr = curr.next

        for _ in node_map.keys():
            return True if node_map.get(_) > 1 else False

    # Removes any detected loops.
    def remove_loop(self):
        fast = slow = self.head
        while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if slow == fast:
                    self.head = slow
                    temp = self.head.next

                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = None

    # Shift the list by N elements left.
    def rotate(self, shift):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = self.head

        for _ in range(0, shift+1):
            curr = curr.next

        self.head = curr
        temp = self.head.next

        while temp.next != self.head:
            temp = temp.next
        temp.next = None

    def loopify(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = self.head

    # Reverses the list. - Helper
    def reverse(self):
        return self._reverse(self.head)

    # Reverses the list. - Recursion
    def _reverse(self, curr, prev=None):
        if curr.next:
            self._reverse(curr.next, curr)
        elif not curr.next:
            self.head = curr
        curr.next = prev

    # Returns the index of the specified data.
    def index_of(self, data):
        curr = self.head
        count = 0
        while curr:
            count += 1
            if curr.data == data:
                return self.size() - count+1
            curr = curr.next
        return False

    # Clears the list.
    def clear(self):
        self.head = None

    # _Node class for data storage and link.
    class _Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
