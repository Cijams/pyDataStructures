import unittest
from pyHeap.pyMinHeap import PyMinHeap

mh = PyMinHeap.PyMinHeap()


# noinspection PyListCreation
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        t = []
        t.append(5)
        t.append(9)
        print(t)
        print()
        t[0], t[1] = t[1], t[0]
        print(t)


if __name__ == '__main__':
    unittest.main()
