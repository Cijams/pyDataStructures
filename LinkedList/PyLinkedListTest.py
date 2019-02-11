import unittest
import random
#from LinkedList import PyLinkedList
from .PyLinkedList import PyLinkedList


#pl = PyLinkedList.PyLinkedList()
pl = PyLinkedList()


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
        print(pl.clear())
        print(pl.iterate())

        pl.remove(5)
        print(pl.iterate())


if __name__ == '__main__':
    unittest.main()
