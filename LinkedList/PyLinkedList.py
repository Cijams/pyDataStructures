class PyLinkedList:
    def __init__(self):
        self.head = self.Node(None)

    def link(self, d):
        temp = self.Node(d)
        print(temp.data)

    def get_link(self):
        print(self.head)

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
