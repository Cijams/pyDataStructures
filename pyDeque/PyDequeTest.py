import unittest
from pyDeque import PyDeque


pd_unlimited = PyDeque.PyDeque()
pd_limited = PyDeque.PyDeque(5)


class MyTestCase(unittest.TestCase):
    def test_deque(self):
        for e in range(1, 6):
            pd_unlimited.append(e)

        self.assertEqual(pd_unlimited.count(), 5)
        self.assertEqual(str([1, 2, 3, 4, 5]), pd_unlimited.__str__())
        pd_unlimited.pop()
        self.assertEqual(str([1, 2, 3, 4]), pd_unlimited.__str__())
        pd_unlimited.pop_left()
        self.assertEqual(str([2, 3, 4]), pd_unlimited.__str__())
        pd_unlimited.append(5)
        self.assertEqual(str([2, 3, 4, 5]), pd_unlimited.__str__())
        pd_unlimited.append_left(1)
        self.assertEqual(str([1, 2, 3, 4, 5]), pd_unlimited.__str__())

        pd_unlimited.clear()
        self.assertEqual(pd_unlimited.__str__(), str([]))

        for e in range(1, 11):
            pd_limited.append(e)
        self.assertEqual(str([1, 2, 3, 4, 5]), pd_limited.__str__())

        for e in range(1, 6):
            pd_limited.pop_left()
        pd_limited.pop_left()

        for e in range(10):
            pd_limited.append(e)

        self.assertEqual(str([0, 1, 2, 3, 4]), pd_limited.__str__())
        pd_limited.extend(4)

        for e in range(5, 20):
            pd_limited.append(e)
        self.assertEqual(str([0, 1, 2, 3, 4, 5, 6, 7, 8]), pd_limited.__str__())

        pd_limited.max_len(3)
        self.assertEqual(3, pd_limited.count())
        self.assertEqual(str([0, 1, 2]), pd_limited.__str__())

        pd_limited.clear()
        for e in range(1, 7):
            pd_limited.append(e)
        self.assertEqual(str([1, 2, 3, 4, 5, 6]), pd_limited.__str__())
        print(pd_limited)
        pd_limited.rotate(2)
        print(pd_limited)


if __name__ == '__main__':
    unittest.main()
