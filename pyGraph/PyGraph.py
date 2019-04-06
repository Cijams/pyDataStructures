"""
Christopher Ijams
Graph - Two way
A data structure consisting of a finite set of connected nodes and edges.
"""


class PyGraph:
    def __init__(self):
        self.graph = {'a': set(),
                      'b': set(),
                      'c': set(),
                      'd': set(),
                      'e': set(),
                      'f': set()}

    def __str__(self):
        string = ""
        for e in self.graph:
            string += str(e) + " "
            if str(self.graph.get(e)) == "set()":
                string += "{ }\n"
            else:
                string += str(self.graph.get(e)) + "\n"
        return string

    def add_edge(self, u, v):
        try:
            self.graph[u].add(v)
            self.graph[v].add(u)
        except KeyError as e:
            return e

    def remove_edge(self, u, v):
        try:
            self.graph[u].remove(v)
            self.graph[v].remove(u)
        except KeyError as e:
            return e

    def clear(self):
        self.graph = {'a': set(),
                      'b': set(),
                      'c': set(),
                      'd': set(),
                      'e': set(),
                      'f': set()}

    def minimum_spanning_tree(self):
        pass

    def depth_first_search(self):
        pass

    def breadth_first_search(self, start):
        visited = {}
        for e in self.graph:
            visited[e] = False

        print(visited)

    def topological_sort(self):
        pass

    def shortest_path(self):
        pass

    def detect_path(self, start, end, path=[]):
        path = path + [start]   # a list that keeps adding start
        if start == end:
            return path
        for node in self.graph[start]:
            if node not in path:
                newpath = self.detect_path(node, end, path)
                if newpath:
                    return newpath
                return None

    def detect_cycle(self):
        pass


