import unittest
from .PyHashTable import PyHashTable

pt = PyHashTable()


class MyTestCase(unittest.TestCase):
    def test_hash_table(self):
        pt.add("5")
        pt.add(4)
        pt.add(4)
        pt.add(4.6)
        pt.add("hello, chris")
        pt.add(2)
        pt.add(33)
        pt.get_table()
        self.assertEqual(pt.table, ([], [], ['hello, chris'], [], [4.6], [4, 2, 33], [], [], [], [], [], [], [], [],
                                    ['5'], []))
        self.assertTrue(pt.contains(4))
        self.assertFalse(pt.contains(3))
        self.assertEqual(pt.get(4), 4)
        self.assertIsNone(pt.get(500))

        self.assertEqual(pt.get_size(), 6)
        pt.remove(4)
        self.assertEqual(pt.table, ([], [], ['hello, chris'], [], [4.6], [2, 33], [], [], [], [], [], [], [], [],
                                    ['5'], []))
        self.assertEqual(pt.get_size(), 5)
        self.assertEqual(pt.get_table(), pt.table)
        pt.clear()
        self.assertEqual(pt.table, ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []))

        pt.add(None)
        pt.add(bool)
        self.assertEqual(pt.table, ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []))


if __name__ == '__main__':
    unittest.main()
