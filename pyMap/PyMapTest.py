import unittest
from pyMap import PyMap


pm = PyMap.PyMap()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pass
    pm.put(5, 6)
    pm.put(7, 9)
    print(pm)


if __name__ == '__main__':
    unittest.main()
