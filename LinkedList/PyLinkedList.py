class PyLinkedList:
    def __init__(self):
        self.head = self.Node(None)

    def add(self, data=None):
        if not self.head.data:
            self.head.data = data
            return "First Time"
        else:
            count = 0
            print(self.head.data)
            print(self.head.get_next())
            print(self.head.set_next(data))
            print(self.head.get_next())
            self.head = self.head.get_next
            print(self.head.data)
            """
            while self.head.get_next() is not None:
                count = count+1
                print(self.head.get_data())
                self.head = self.head.get_next
                print("yep")
            self.head.get_next = self.Node(data)
            """
            return count




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
