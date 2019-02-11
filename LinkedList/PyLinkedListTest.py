import unittest
from LinkedList import PyLinkedList


pl = PyLinkedList.PyLinkedList()


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


if __name__ == '__main__':
    unittest.main()
