import unittest
import random


from pyLinkedList.Skip.PySkipList import PySkipList


ps = PySkipList()


class MyTestCase(unittest.TestCase):
    def test_skipList(self):
        for e in range(25):
            ps.add(random.randint(0, 100))
        print(ps)


if __name__ == '__main__':
    unittest.main()
