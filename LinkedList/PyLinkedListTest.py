import unittest
from LinkedList import PyLinkedList

pl = PyLinkedList.PyLinkedList()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pl.link(5)

    def test_get_link(self):
        pl.get_link()

if __name__ == '__main__':
    unittest.main()
