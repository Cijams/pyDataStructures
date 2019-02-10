class PyLinkedList:
    def __init__(self):
        self.head = self.Node(None)

    def add(self):
        pass
        # True/False return

    def add_first(self):
        pass

    def add_last(self):
        pass

    def contains(self):
        pass

    def get(self):
        pass

    def get_first(self):
        pass

    def get_last(self):
        pass


    class Node:
        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next_node = next_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next_node

        def set_next(self, next_node=None):
            self.next_node = next_node
