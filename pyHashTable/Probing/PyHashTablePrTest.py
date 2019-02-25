import unittest
from pyHashTable.Probing.PyHashTablePr import PyHashTable


pt = PyHashTable()


class MyTestCase(unittest.TestCase):
    def test_hash_table(self):
        self.assertEqual(([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []), pt.table)
        pt.add(5)
        pt.add(2)
        pt.add(3)
        print(pt.get_table())


if __name__ == '__main__':
    unittest.main()
