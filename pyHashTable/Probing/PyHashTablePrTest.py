import unittest
from pyHashTable.Probing.PyHashTablePr import PyHashTablePr


pt = PyHashTablePr()


class MyTestCase(unittest.TestCase):
    def test_hash_table(self):
        pt.add(5)
        pt.add(8)
        pt.add(3)
        pt.add(20)
        pt.add(11)
        pt.add(11)
        pt.add(11)
        pt.add(11)
        pt.add(11)
        pt.add(11)
        pt.add(11)
        pt.add(11)
        pt.add(11)
        pt.add(11)
        pt.add(11)
        pt.add(11)
        pt.add("hello")
        self.assertEqual(([20], [3], [11], [11], [11], [11], [11], [5], [], [], [], [], [8], [], [], [], ['hello'], [],
                          [], [], [], [], [], [], [], [11], [11], [11], [11], [11], [11], [11]), pt.table)
        pt.add('ftgh')
        pt.add('666')
        pt.add(535)
        pt.add(2)
        pt.add(1)
        pt.add(4)
        pt.add(6)
        pt.add(3)
        pt.add(7)
        pt.add(8)
        pt.add(99)
        pt.add(99)
        pt.add(6)
        pt.add(3)
        pt.add(3)
        pt.add(3)
        self.assertEqual(([20], [3], [3], [3], [3], [11], [11], [11], [11], ['ftgh'], [11], [11], [8], [8], [11], [3],
                          [4], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [5], [], [99], [99], [1], [], [],
                          [], [], [], [], [], [], [], [535], [6], [6], ['hello'], [], [2], [], [], [], [], [], [], [11],
                          [11], [11], [11], [11], [7], ['666']), pt.table)

        self.assertEqual(pt.contains(3), True)
        self.assertEqual(pt.contains(9001), False)
        pt.clear()
        pt.add(1)
        pt.add(2)
        pt.add(3)
        pt.remove(2)
        self.assertEqual(pt.table, ([], [3], [], [1], [], [], [], [], [], [], [], [], [], [], [], []))
        self.assertFalse(pt.contains(2), False)




if __name__ == '__main__':
    unittest.main()
