import unittest
from .PyLinkedList import PyLinkedList


pl = PyLinkedList()


class MyTestCase(unittest.TestCase):
    def test_add(self):
        pl.add(1)
        pl.add(2)
        pl.add(3)
        pl.add(5)

        print(pl.iterate())
        print(pl.size())
        print(pl.contains(2))

if __name__ == '__main__':
    unittest.main()
