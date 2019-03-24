import unittest
from pyLinkedList.Double import PyDoublyLinkedList


pd = PyDoublyLinkedList.PyDoublyLinkedList()


class MyTestCase(unittest.TestCase):
    def test_doubly_linked_list(self):
        self.assertTrue(True)
        self.assertIsNone(pd.get_last())
        pd.add(5)
        self.assertEqual(pd.get_last(), 5)
        pd.add(6)
        pd.add(7)

        self.assertEqual(pd.size(), 3)
        self.assertTrue(pd.contains(5))
        self.assertFalse(pd.contains(8))
        self.assertIsNotNone(pd.get(5))
        self.assertEqual(pd.get_last(), 7)

        self.assertEqual(pd.size(), 3)
        pd.remove(6)
        pd.remove(7)
        pd.remove(5)
        self.assertEqual(pd.size(), 0)
        for x in range(4):
            pd.add(x)
        self.assertEqual(pd.middle(), 2)
        pd.clear()

        print("HERE IS START OF REVERSE______")
        for e in range(1, 6):
            pd.add(e)
        print("before reverse: " + str(pd))
        pd.reverse()
        print("after reverse: " + str(pd))

        pd.clear()


if __name__ == '__main__':
    unittest.main()
