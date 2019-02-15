import unittest
from BinaryTree import PyBinaryTree


bt = PyBinaryTree.PyBinaryTree()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        bt.insert(5)
        bt.insert(3)
        bt.insert(1)
        bt.insert(6)

        bt.in_order_traversal()
        print()
        bt.post_order_traversal()
        print()
        bt.pre_order_traversal()


if __name__ == '__main__':
    unittest.main()
