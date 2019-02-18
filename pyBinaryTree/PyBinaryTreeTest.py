import unittest
from pyBinaryTree import PyBinaryTree


bt = PyBinaryTree.PyBinaryTree()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        bt.insert(5)
        bt.insert(3)
        bt.insert(1)
        bt.insert(6)
        bt.insert("r")

        self.assertEqual(bt.in_order_traversal(), [1, 3, 5, 6])
        self.assertEqual(bt.post_order_traversal(), [1, 3, 6, 5])
        self.assertEqual(bt.pre_order_traversal(), [5, 3, 1, 6])

        self.assertEqual(15, bt.sum())
        bt.insert(15)
        self.assertEqual(bt.sum(), 30)

        self.assertEqual(bt.search_dfs(5).data, 5)
        self.assertEqual(bt.search_dfs(1).data, 1)
        self.assertEqual(bt.search_dfs(6).data, 6)
        self.assertEqual(PyBinaryTree.PyBinaryTree._Node, type(bt.search_dfs(5)))
        self.assertEqual(bt.search_dfs(700), None)

        bt.clear()
        self.assertEqual(bt.height(), None)

        bt.insert(50)
        bt.insert(25)
        bt.insert(35)
        bt.insert(15)
        bt.insert(10)
        bt.insert(75)
        bt.insert(85)

        self.assertEqual(bt.height(), 4)
        self.assertEqual(bt.min(), 10)
        self.assertEqual(bt.max(), 85)

        bt.insert(0)
        bt.insert(100)
"""
        bt.insert(0)
        bt.insert(100)

        self.assertEqual(bt.height(), 5)
        self.assertEqual(bt.min(), 0)
        self.assertEqual(bt.max(), 100)
"""

if __name__ == '__main__':
    unittest.main()
