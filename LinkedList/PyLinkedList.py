class PyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data=None):
        temp_node = self.Node(data)
        temp_node.set_next(self.head)
        self.head = temp_node

    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            temp = temp.get_next()
            count = count + 1
        return count

    def contains(self, data):
        temp = self.head
        while temp is not None:
            if temp.get_data() == data:
                return True
            temp = temp.get_next()
        return False

    def get(self):
        pass

    def get_first(self):
        pass

    def get_last(self):
        pass

    def iterate(self):
        node_list = []
        temp = self.head
        while temp is not None:
            node_list.append(temp.get_data())
            temp = temp.get_next()
        node_list.reverse()
        return node_list

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
