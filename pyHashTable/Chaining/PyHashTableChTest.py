import unittest
import random
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

        self.assertEqual(([], [], [], [], [], [], [], ['hello, chris'], [], [], [], [], [], [], [], [], [], [], [4.6],
                          [2], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [33], [], [], [], [], [],
                          [], [], [], [], ['5'], [], [], [4], [], [], [], [], [], [], [], [], [], [], [], [], [], []),
                         pt.table)

        self.assertTrue(pt.contains(4))
        self.assertFalse(pt.contains(3))
        self.assertEqual(pt.get(4), 4)
        self.assertIsNone(pt.get(500))

        self.assertEqual(pt.get_size(), 6)
        for _ in range(100):
            pt.add(random.randint(0, 100))

        self.assertEqual(pt.get_table(), pt.table)
        pt.clear()
        pt.add(None)
        pt.add(bool)
        pt.clear()


if __name__ == '__main__':
    unittest.main()
