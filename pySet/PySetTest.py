import unittest
from pySet import PySet


ps = PySet.PySet()


class MyTestCase(unittest.TestCase):
    def test_something(self):

        ps.add(5)
        ps.add(6)
        ps.add(7)
        ps.add(5)
        ps.add(6)
        ps.add(3)

        self.assertEqual(ps.iterate(), {3, 5, 6, 7})
        ps.remove(5)
        self.assertEqual(ps.iterate(), {3, 6, 7})

        ps.remove(3)
        ps.remove(7)
        ps.remove(6)

        self.assertEqual(set(), ps.iterate())
        self.assertFalse(ps.remove(4), False)

        ps.add(5)
        self.assertEqual(ps.iterate(), {5})
        ps.change(5, 8)
        self.assertEqual(ps.iterate(), {8})

        for _ in range(0, 10):
            ps.add(_)
        self.assertEqual(ps.length(), 10)
        ps.clear()
        self.assertEqual(ps.iterate(), set())
        self.assertEqual(ps.length(), 0)


if __name__ == '__main__':
    unittest.main()
