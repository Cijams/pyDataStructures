import unittest
from pyGraph import PyGraph


pg = PyGraph.PyGraph()


class MyTestCase(unittest.TestCase):
    def test_graph(self):
        self.assertEqual(True, True)
        pg.add_edge('a', 'f')
       # print(pg)
        pg.clear()
       # print(pg)

        pg.add_edge('a', 'c')
        pg.add_edge('c', 'b')
        pg.add_edge('c', 'e')
        pg.add_edge('c', 'd')
        pg.add_edge('b', 'e')
        pg.add_edge('r', 'h')
       # print(pg)
        print()

        pg.remove_edge('a', 'c')
        #print(pg)
        pg.add_edge('a', 'c')
        print(pg)
        print()

    def test_paths(self):
        pg.add_edge('a', 'e')
        pg.add_edge('e', 'd')
        print(pg.detect_path('a', 'd'))

    def test_bfs(self):
        pg.clear()

        pg.add_edge('a', 'c')
        pg.add_edge('c', 'b')
        pg.add_edge('c', 'e')
        pg.add_edge('c', 'd')
        pg.add_edge('b', 'e')
        pg.add_edge('r', 'h')
        print(pg)
        pg.breadth_first_search('a')



if __name__ == '__main__':
    unittest.main()
