import unittest
from pyGraph import PyGraph


pg = PyGraph.PyGraph()

class MyTestCase(unittest.TestCase):
    def test_graph(self):
        pg.test()


if __name__ == '__main__':
    unittest.main()
