class PyBinaryTree:
    def __init__(self, head=None):
        self.head = head
        self._count = 0
        self._data = 0
        self._order = []
        self._found = False

    # Insert first Node or call main method.
    def insert(self, data=None):
        if self.head is None:
            self.head = self._Node(data)
        else:
            self._insert(self.head, data)

    # Insert a node into the binary tree.
    def _insert(self, curr, data):
        if type(data) is int:
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

    # Delete a specified Node from the tree.
    def delete(self):
        pass

    # Deletes the entire tree
    def clear(self):
        self.head = None
        self._count = 0
        self._order = []
        self._found = False

    # Returns the position of the specified Node. - Helper
    def search(self, data):
        self._count = 0
        self._found = False
        return self._search(self.head, data)

    # Returns the position of the specified Node.
    def _search(self, curr, data):
        if not self._found:
            self._count += 1
            if curr.get_data() == data:
                self._found = True
                return self._count
            if curr.get_left():
                self._search(curr.get_left(), data)
            if curr.get_right():
                self._search(curr.get_right(), data)
        return self._count

    # Returns level of the specified Node
    def rank(self):
        pass

    # Returns a list of nodes in pre-ordered condition. - Helper
    def pre_order_traversal(self):
        self._order = []
        self._pre_order_traversal(self.head)
        return self._order

    # Returns a list of nodes in pre-ordered condition.
    def _pre_order_traversal(self, curr):
        self._order.append(curr.get_data())
        if curr.get_left():
            self._pre_order_traversal(curr.get_left())
        if curr.get_right():
            self._pre_order_traversal(curr.get_right())

    # Returns a list of nodes in in-ordered condition. - Helper
    def in_order_traversal(self):
        self._order = []
        self._in_order_traversal(self.head)
        return self._order

    # Returns a list of nodes in pre-ordered condition.
    def _in_order_traversal(self, curr):
        if curr.get_left():
            self._in_order_traversal(curr.get_left())
        self._order.append(curr.get_data())
        if curr.get_right():
            self._in_order_traversal(curr.get_right())

    # Returns a list of nodes in post-ordered condition. - Helper
    def post_order_traversal(self):
        self._order = []
        self._post_order_traversal(self.head)
        return self._order

    # Returns a list of nodes in post-ordered condition.
    def _post_order_traversal(self, curr):
        if curr.get_left():
            self._post_order_traversal(curr.get_left())
        if curr.get_right():
            self._post_order_traversal(curr.get_right())
        self._order.append(curr.get_data())

    # Returns a list of node by their height level.
    def level_order_traversal(self):
        pass

    # Prints the height of the binary tree.
    def height(self):
        if self.head:
            self._count = 0
            self._data = 0
            self._height(self.head)
            return self._data
        else:
            return None

    def _height(self, curr):
        self._count += 1
        if self._count > self._data:
            self._data = self._count
        if curr.get_left():
            self._height(curr.get_left())
            self._count -= 1
        if curr.get_right():
            self._height(curr.get_right())
            self._count -= 1

    def min(self):
        self._data = 0
        return self._min(self.head)

    def _min(self, curr):
        if curr.get_left():
            self._min(curr.get_left())
        else:
            self._data = curr.get_data()
        return self._data

    def max(self):
        self._data = 0
        return self._max(self.head)

    def _max(self, curr):
        if curr.get_right():
            self._max(curr.get_right())
        else:
            self._data = curr.get_data()
        return self._data

    # Returns the total sum of the data in the tree. - Helper
    def sum(self):
        self._count = 0
        return self._sum(self.head)

    # Returns the total sum of the data in the tree.
    def _sum(self, curr):
        self._count += curr.get_data()
        if curr.get_left():
            self._sum(curr.get_left())
        if curr.get_right():
            self._sum(curr.get_right())
        return self._count

    # Returns true if the data-structure is a complete binary tree
    def is_complete(self):
        pass

    # _Node class for data storage and link:
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
