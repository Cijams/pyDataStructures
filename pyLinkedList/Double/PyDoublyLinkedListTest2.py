import unittest
from .PyDoublyLinkedList import PyDoublyLinkedList


pd = PyDoublyLinkedList()


class MyTestCase(unittest.TestCase):
    def test_DLL(self):
        self.assertEqual(True, True)
        pd.add(1)
        pd.add(2)
        pd.add(3)
        pd.add(4)
        pd.add(5)

        print(pd)
        pd.delete_middle_node()
        print(pd)

        pd.add(6)
        pd.add(7)
        pd.add(8)
        pd.add(9)
        print(pd)
        self.assertEqual(pd.return_kth_to_last_element(2), 8)
        print(pd.return_kth_to_last_element(5))
        print(pd.return_kth_to_last_element(100))

        print(pd)
        pd.add(4)
        pd.add(2)
        pd.add(1)
        print(pd)
        pd.remove_duplicates()
        print(pd)

        pd.clear()
        pd.add(1)
        pd.add(2)
        pd.add(3)
        pd.add(2)
        pd.add(1)
        print(pd.is_palindrome())
        self.assertTrue(pd.is_palindrome())

        pd.remove(1)
        self.assertFalse(pd.is_palindrome())



if __name__ == '__main__':
    unittest.main()
