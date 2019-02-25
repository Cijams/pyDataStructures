import unittest
from .PyHashTable import PyHashTable

pt = PyHashTable()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        pt.add(5)
        pt.add('r')
        pt.add(333)

        print(hash('r'))
        print(hash('r'))

        pt.print_table()

if __name__ == '__main__':
    unittest.main()
