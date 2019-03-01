import unittest
import random
from .PyQueue import PyQueue

pq = PyQueue()


class MyTestCase(unittest.TestCase):
    def test_push_peek(self):
        pq.push(5)
        self.assertEqual(pq.peek(), 5)
        pq.push("Hello")
        self.assertEqual(pq.peek(), 5)

    def test_deque(self):
        pq.push(1)
        pq.push(2)
        pq.push(3)

        self.assertEqual(pq.deque(), 1)
        self.assertEqual(pq.deque(), 2)
        self.assertEqual(pq.deque(), 3)

    def test_is_empty(self):
        pq.push(17)
        self.assertFalse(pq.is_empty())
        pq.clear()
        self.assertTrue(pq.is_empty())

    def test_size(self):
        while not pq.is_empty():
            pq.deque()
        self.assertEqual(pq.size(), 0)
        for i in range(0, 10):
            pq.push(i)
        self.assertEqual(pq.size(), 10)

    def test_clear(self):
        pq.clear()
        for x in range(0, 15):
            pq.push(random.randint(0, 100))
        self.assertEqual(pq.size(), 15)
        pq.clear()
        self.assertEqual(pq.size(), 0)

    def test_str(self):
        pq.clear()
        for x in range(15):
            pq.push(x)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
