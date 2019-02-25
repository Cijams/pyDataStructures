import unittest
import random
from pyLinkedList.Single import PySinglyLinkedList

pl = PySinglyLinkedList.PyLinkedList()


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
        self.assertIsNotNone(pl.iterate())

        pl.clear()
        self.assertEqual(0, len(pl.iterate()))

        for _ in range(0, 10):
            pl.add(_)
        self.assertEqual(pl.index_of(2), 3)

        pl.remove(9)
        pl.remove(5)
        pl.remove(0)
        self.assertEqual([1, 2, 3, 4, 6, 7, 8], pl.iterate())

        for _ in range(0, 10):
            pl.remove(_)
        self.assertEqual(0, len(pl.iterate()))

        for _ in range(1, 11):
            pl.add(_)

        self.assertEqual(5, pl.middle())
        pl.add(12432)
        self.assertEqual(6, pl.middle())

        pl.clear()

        for _ in range(0, 10000):
            pl.add(random.randint(0, 5))

        pl.remove_duplicates()
        self.assertEqual([0, 1, 2, 3, 4, 5], pl.iterate())

        pl.clear()
        pl.add(1)
        pl.modify__node(1, 5)
        self.assertEqual([5], pl.iterate())

        pl.clear()
        pl.add(1)
        pl.add(2)
        pl.add(3)
        pl.add(4)
        pl.add(5)
        pl.add(6)
        pl.reverse()
        self.assertEqual([6, 5, 4, 3, 2, 1], pl.iterate())

        pl.detect_loop()
        pl.remove_loop()
        pl.reverse()

        pl.rotate(3)     # 1, 2, 3, 4, 5, 6
        self.assertEqual([4, 5, 6, 1, 2, 3], pl.iterate())
        pl.rotate(5)
        self.assertEqual([5, 6, 1, 2, 3, 4], pl.iterate())
        pl.rotate(4)

        pl.loopify()
        pl.remove_loop()
        self.assertEqual(pl.iterate(), [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
