import unittest
from pyHashTable.Probing.PyHashTablePr import PyHashTablePr


pt = PyHashTablePr()


class MyTestCase(unittest.TestCase):
    def test_hash_table(self):
        self.assertEqual(([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []), pt.table)
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
        self.assertEqual(([20], [3], [11], [11], [11], [11], [11], [11], [11], [11], [11], [11],
                          [8], [11], [11], [5]), pt.table)
        pt.add(11)
        self.assertEqual(([20], [3], [], [], [], [], [], [], [], [11], [11], [11], [11], [11], [11], [11], [11], [11],
                          [11], [8], [11], [11], [5], [11], [], [], [], [], [], [], [], []), pt.table)



if __name__ == '__main__':
    unittest.main()
