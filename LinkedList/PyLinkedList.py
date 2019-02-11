class PyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data=None):
        curr_node = self.Node(data)
        curr_node.set_next(self.head)
        self.head = curr_node

    def size(self):
        count = 0
        curr = self.head
        while curr:
            curr = curr.get_next()
            count = count + 1
        return count

    def contains(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return True
            curr = curr.get_next()
        return False

    def get(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return curr
            curr = curr.get_next()
        return None

    def get_first(self):
        curr = self.head
        while curr.get_next():
            curr = curr.get_next()
        return curr.get_data()

    def get_last(self):
        return self.head.get_data()

    def iterate(self):
        node_list = []
        curr = self.head
        while curr:
            node_list.append(curr.get_data())
            curr = curr.get_next()
        node_list.reverse()
        return node_list

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

    def reverse(self):
        pass

    def index_of(self):
        pass

    def clear(self):
        self.head = None

    class Node:
        def __init__(self, _data=None):
            self._data = _data
            self._next = None

        def get_data(self):
            return self._data

        def get_next(self):
            return self._next

        def set_next(self, _next=None):
            self._next = _next
