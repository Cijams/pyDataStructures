class PyLinkedList:
    def __init__(self, head=None):
        self.head = head

    # Add an element to the list.
    def add(self, data=None):
        curr__node = self._Node(data)
        curr__node.set_next(self.head)
        self.head = curr__node

    # Return the size of the list.
    def size(self):
        count = 0
        curr = self.head
        while curr:
            curr = curr.get_next()
            count = count + 1
        return count

    # Returns true if the list has the data.
    def contains(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return True
            curr = curr.get_next()
        return False

    # Returns the _node that contains the specified data.
    def get(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return curr
            curr = curr.get_next()
        return None

    # Returns the first element in the list.
    def get_first(self):
        curr = self.head
        while curr.get_next():
            curr = curr.get_next()
        return curr.get_data()

    # Returns the last element in the list.
    def get_last(self):
        return self.head.get_data()

    # Returns a list of the LinkedList
    def iterate(self):
        _node_list = []
        curr = self.head
        while curr:
            _node_list.append(curr.get_data())
            curr = curr.get_next()
        _node_list.reverse()
        return _node_list

    # Removes an element from the list.
    def remove(self, data):
        curr = self.head
        try:
            if curr.get_data() == data:
                self.head = self.head.get_next()
                return True
            while curr:
                if curr.get_next().get_data() == data:
                    curr.set_next(curr.get_next().get_next())
                    return True
                curr = curr.get_next()
        except AttributeError:
            return False

    # Reverses the list.
    def reverse(self):
        pass

    # Returns the middle of the list.
    def middle(self):
        if self.head:
            fast = self.head
            slow = self.head
            while fast and fast.get_next():
                fast = fast.get_next().get_next()
                slow = slow.get_next()
            return slow.get_data()

    # Removes duplicates from the list.
    def remove_duplicates(self):
        pass

    # Changes the data in a specified _node in the list.
    def modify__node(self):
        pass

    # Detects loops in the list.
    def detect_loop(self):
        pass

    # Removes any detected loops.
    def remove_loop(self):
        pass

    # Shift the list by N elements left.
    def rotate(self):
        pass

    # Returns the index of the specified data.
    def index_of(self, data):
        curr = self.head
        count = 0
        while curr:
            count += 1
            if curr.get_data() == data:
                return self.size() - count+1
            curr = curr.get_next()
        return False

    # Clears the list.
    def clear(self):
        self.head = None

    # _Node class for data storage and link.
    class _Node:
        def __init__(self, _data=None):
            self._data = _data
            self._next = None

        def get_data(self):
            return self._data

        def get_next(self):
            return self._next

        def set_next(self, _next=None):
            self._next = _next
