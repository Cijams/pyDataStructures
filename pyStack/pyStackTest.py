import unittest
import random
from pyStack import PyStack

ps = PyStack.PyStack()


class MyTestCase(unittest.TestCase):
    def test_push_peek(self):

        ps.push(5)
        self.assertEqual(ps.peek(), 5)
        ps.push(3)
        self.assertEqual(ps.peek(), 3)
        ps.push((4,2))
        self.assertEqual(ps.peek(), (4, 2))
        ps.push("Go")
        self.assertEqual(ps.peek(), "Go")
        ps.pop()

    def test_pop(self):
        ps.push(1)
        ps.push(2)
        ps.push(3)

        self.assertEqual(ps.pop(), 3)
        self.assertEqual(ps.pop(), 2)
        self.assertEqual(ps.pop(), 1)

        ps.pop()

    def test_is_empty(self):
        self.assertTrue(ps.is_empty())
        ps.push(4)
        self.assertFalse((ps.is_empty()))
        ps.pop()
        self.assertTrue(ps.is_empty())

    def test_size(self):
        while not ps.is_empty():
            ps.pop()
        self.assertEqual(ps.size(), 0)
        for i in range(0, 10):
            ps.push(i)
        self.assertEqual(ps.size(), 10)

    def test_clear(self):
        ps.clear()
        for x in range(0, 15):
            ps.push(random.randint(0, 101))
        self.assertEqual(ps.size(), 15)
        ps.clear()
        self.assertEqual(ps.size(), 0)

    def test_str(self):
        ps.clear()
        for x in range(15):
            ps.push(x)
        self.assertTrue(True, True)


if __name__ == '__main__':
    unittest.main()
