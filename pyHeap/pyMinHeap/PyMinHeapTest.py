import unittest
from pyHeap.pyMinHeap import PyMinHeap

mh = PyMinHeap.PyMinHeap()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        v = 5
        t = 10

        print(v)
        print(t)

        v, t = t, v

        print(v)
        print(t)



if __name__ == '__main__':
    unittest.main()
