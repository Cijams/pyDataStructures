import unittest
import random
from pyMap import PyMap


pm = PyMap.PyMap()


class MyTestCase(unittest.TestCase):
    def test_map(self):
        pm.put(5, 6)
        pm.put(7, 9)
        self.assertTrue(pm, ({7: 9}, {5: 6}))
        self.assertEqual(pm.keys(), [7, 5])
        self.assertEqual(pm.values(), [9, 6])
        pm.pop()
        self.assertTrue(pm)
        pm.pop()
        self.assertEqual(pm.__str__(), "")

        for e in range(5):
            pm.put(e, e+1)

        print(pm)
        pm.remove_key(4)
        print(pm)
        pm.contains_value(4)
        self.assertTrue(pm.contains_value(4))
        self.assertTrue(pm.contains_key(3))


if __name__ == '__main__':
    unittest.main()
