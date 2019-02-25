import unittest
from pySet import PySet

ps = PySet.PySet()
ps1 = PySet.PySet()
ps2 = PySet.PySet()


class MyTestCase(unittest.TestCase):
    def test_set(self):
        # Testing add.
        ps1.add(5)
        ps1.add(6)
        ps1.add(7)
        ps1.add(5)
        ps1.add(6)
        ps1.add(3)

        # Testing remove and iterate.
        self.assertEqual(ps1.iterate(), {3, 5, 6, 7})
        ps1.remove(5)
        self.assertEqual(ps1.iterate(), {3, 6, 7})
        ps1.remove(3)
        ps1.remove(7)
        ps1.remove(6)
        self.assertEqual(set(), ps1.iterate())
        self.assertFalse(ps1.remove(4), False)

        # Testing change.
        ps1.add(5)
        self.assertEqual(ps1.iterate(), {5})
        ps1.change(5, 8)
        self.assertEqual(ps1.iterate(), {8})

        # Testing clear and length.
        for _ in range(0, 10):
            ps1.add(_)
        self.assertEqual(ps1.length(), 10)
        ps1.clear()
        self.assertEqual(ps1.iterate(), set())
        self.assertEqual(ps1.length(), 0)

        # Testing pop.
        for _ in range(0, 10):
            ps1.add(_)
        self.assertEqual(ps1.iterate(), {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
        ps1.pop()
        self.assertEqual(ps1.iterate(), {1, 2, 3, 4, 5, 6, 7, 8, 9})

        # Testing difference.
        for _ in range(0, 10, 2):
            ps2.add(_)
        self.assertEqual({0, 1, 3, 5, 7, 9}, ps.difference(ps1, ps2))

        # Testing intersection.
        self.assertEqual({8, 2, 4, 6}, ps.intersection(ps1, ps2))

        # Testing disjoint.
        self.assertFalse(ps.is_disjoint(ps1, ps2))
        ps1.clear()
        ps2.clear()
        for _ in range(0, 5):
            ps1.add(_)
        for _ in range(5, 10):
            ps2.add(_)
        self.assertTrue(ps.is_disjoint(ps1, ps2))

        # Testing union.
        ps1.add(6)
        ps2.add(2)
        ps1.add(9)
        ps2.add(7)
        self.assertEqual(ps.union(ps1, ps2), {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

        # Testing subset.
        ps1.clear()
        ps2.clear()

        ps1.add(1)
        ps1.add(2)

        ps2.add(1)
        ps2.add(2)
        ps2.add(3)
        self.assertTrue(ps.is_subset(ps1, ps2))
        ps1.add(7)
        self.assertFalse(ps.is_subset(ps1, ps2))

        print(ps1.iterate())
        ps1.change(2, 1)
        print(ps1.iterate())


if __name__ == '__main__':
    unittest.main()
