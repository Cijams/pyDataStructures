import unittest
from pyHashTable.Chaining.PyHashTableCh import PyHashTable

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

        self.assertEqual(pt.get_table(), ([], [4], [4.6], [2], [33], [], [], ['hello, chris'], [], [], [], [], [], [],
                                          ['5'], []))
        self.assertTrue(pt.contains(4))
        self.assertFalse(pt.contains(3))
        self.assertEqual(pt.get(4), 4)
        self.assertIsNone(pt.get(500))

        self.assertEqual(pt.get_size(), 6)
        pt.remove(4)

        self.assertEqual(pt.get_size(), 5)
        self.assertEqual(pt.get_table(), pt.table)
        pt.clear()
        self.assertEqual(pt.table, ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []))

        pt.add(None)
        pt.add(bool)
        self.assertEqual(pt.table, ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []))
        pt.clear()


if __name__ == '__main__':
    unittest.main()
