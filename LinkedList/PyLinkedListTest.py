import unittest
import random
from LinkedList import PyLinkedList
#from .PyLinkedList import PyLinkedList -


pl = PyLinkedList.PyLinkedList()
#pl = PyLinkedList() -


class MyTestCase(unittest.TestCase):
    def test_list(self):
        pl.add(1)
        pl.add(2)
        pl.add(3)
        pl.add(5)

        self.assertTrue(pl.contains(2))
        self.assertTrue(pl.contains(3))
        self.assertTrue(pl.contains(5))
        self.assertTrue(pl.contains(1))

        self.assertEqual(pl.size(), 4)
        self.assertEqual([1, 2, 3, 5], pl.iterate())
        self.assertIsNotNone(pl.get(1))

        self.assertEqual(pl.get_first(), 1)
        self.assertEqual(pl.get_last(), 5)

    def test_two(self):
        for _ in range(0, 10):
            pl.add(random.randint(0, 100))
        print(pl.iterate())
        pl.clear()
        print(pl.iterate())
        print("_______________________________")
        for _ in range(0, 10):
            pl.add(_)

        print("_")
        print(pl.index_of(2))
        print("_")

        print(pl.iterate())
        pl.remove(9)
        print(pl.iterate())
        pl.remove(5)
        print(pl.iterate())
        pl.remove(0)
        print(pl.iterate())

        for _ in range(0, 10):
            pl.remove(_)
        print(pl.iterate())
        print(pl.index_of(2))

        for _ in range(1, 11):
            pl.add(_)
        print(pl.iterate())
        print(pl.middle())
        pl.add(12432)
        print(pl.middle())

        pl.clear()

        for _ in range(0, 1000):
            pl.add(random.randint(0, 10))
        print(pl.iterate())
        print(pl.remove_duplicates())
        print(pl.iterate())

        pl.modify__node(5, 9)
        print(pl.iterate())

        print("__________________")
        pl.reverse()
        print(pl.iterate())


if __name__ == '__main__':
    unittest.main()
