"""
Christopher Ijams
Binary Tree
Node based tree data structure of two elements each.
"""


class PyBinaryTree:
    def __init__(self, head=None):
        self.head = head
        self._order = []

    def __str__(self):
        definition = self.pre_order_traversal()
        return str(definition)

    # Insert first Node or call main method.
    def insert(self, data=None):
        if self.head is None:
            self.head = self._Node(data)
        else:
            self._insert(self.head, data)

    # Insert a node into the binary tree.
    def _insert(self, curr, data):
        if type(data) is int:
            if data < curr.data:  # investing merging into AND here
                if curr.left is None:
                    curr.left = self._Node(data)
                else:
                    self._insert(curr.left, data)
            else:
                if curr.right is None:
                    curr.right = self._Node(data)
                else:
                    self._insert(curr.right, data)

    # Delete a specified Node from the tree.
    def delete(self):
        pass

    # Deletes the entire tree
    def clear(self):
        self.head = None

    # Returns the specified Node. - Helper
    def search_dfs(self, data):
        return self._search_dfs(self.head, data)

    # Returns the specified Node.
    def _search_dfs(self, curr, data):
        if not curr or curr.data == data:
            return curr
        if data < curr.data:
            return self._search_dfs(curr.left, data)
        if data >= curr.data:
            return self._search_dfs(curr.right, data)

    def search_bfs(self):
        pass

    def _search_bfs(self):
        pass

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
        self._order.append(curr.data)
        if curr.left:
            self._pre_order_traversal(curr.left)
        if curr.right:
            self._pre_order_traversal(curr.right)

    # Returns a list of nodes in in-ordered condition. - Helper
    def in_order_traversal(self):
        self._order = []
        self._in_order_traversal(self.head)
        return self._order

    # Returns a list of nodes in pre-ordered condition.
    def _in_order_traversal(self, curr):
        if curr.left:
            self._in_order_traversal(curr.left)
        self._order.append(curr.data)
        if curr.right:
            self._in_order_traversal(curr.right)

    # Returns a list of nodes in post-ordered condition. - Helper
    def post_order_traversal(self):
        self._order = []
        self._post_order_traversal(self.head)
        return self._order

    # Returns a list of nodes in post-ordered condition.
    def _post_order_traversal(self, curr):
        if curr.left:
            self._post_order_traversal(curr.left)
        if curr.right:
            self._post_order_traversal(curr.right)
        self._order.append(curr.data)

    # Returns a list of node by their height level.
    def level_order_traversal(self):
        pass

    # Prints the height of the binary tree.
    def height(self):
        return self._height(self.head) if self.head else None

    def _height(self, curr):
        if curr:
            left_depth = self._height(curr.left)
            right_depth = self._height(curr.right)
            return left_depth + 1 if left_depth > right_depth\
                else right_depth + 1
        else:
            return 0

    # flips the binary tree.
    def flip(self):
        pass

    # Returns the depth of the node in the tree.
    def depth(self, data):
        pass

    # Returns the smallest value in the tree. - Helper
    def min(self):
        return self._min(self.head)

    # Returns the smallest value in the tree. - Helper
    def _min(self, curr):
        return self._min(curr.left) if curr.left else curr.data

    # Returns the largest value in the tree. - Helper
    def max(self):
        return self._max(self.head)

    # Returns the largest value in the tree.
    def _max(self, curr):
        return self._max(curr.right) if curr.right else curr.data

    # Returns the total sum of the data in the tree. - Helper
    def sum(self):
        return self._sum(self.head)

    # Returns the total sum of the data in the tree.
    def _sum(self, curr):
        return curr.data + self._sum(curr.left) + self._sum(curr.right)\
            if curr else 0

    # Returns true if the data-structure is a complete binary tree
    def is_complete(self):
        pass

    # _Node class for data storage and link:
    class _Node:
        def __init__(self, data=None):
            self.data = data
            self.left = None
            self.right = None
