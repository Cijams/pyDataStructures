class PyBinaryTree:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data=None):
        if self.head is None:
            self.head = self._Node(data)
        else:
            self._insert(self.head, data)

    def _insert(self, curr, data):
        if data < curr.get_data():
            if curr.get_left() is None:
                curr.set_left(self._Node(data))
            else:
                self._insert(curr.get_left(), data)
        else:
            if curr.get_right() is None:
                curr.set_right(self._Node(data))
            else:
                self._insert(curr.get_right(), data)

    def delete(self):
        pass

    def delete_tree(self):
        self.head = None

    def search(self):
        pass

    def rank(self):
        pass

    def pre_order_traversal(self):
        pass

    def in_order_traversal(self):
        self._in_order_traversal(self.head)

    def _in_order_traversal(self, curr):
        if curr.get_left():
            self._in_order_traversal(curr.get_left())
        print(curr.get_data())
        if curr.get_right():
            self._in_order_traversal(curr.get_right())

    def post_order_traversal(self):
        pass

    def level_order_traversal(self):
        pass

    def is_bst(self):
        pass

    def lowest_common_ancestor(self):
        pass

    def height(self):
        pass

    def floor(self):
        pass

    def ceil(self):
        pass

    def sum(self):
        pass

    def is_complete(self):
        pass

    class _Node:
        def __init__(self, data=None):
            self.data = data
            self.left = None
            self.right = None

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def get_data(self):
            return self.data

        def set_left(self, left=None):
            self.left = left

        def set_right(self, right=None):
            self.right = right
