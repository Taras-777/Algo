import unittest
from main import Graph


class BellmanFordTest(unittest.TestCase):
    def setUp(self):
        self.g = Graph(4)
        self.g.addEdge(0, 1, 2)
        self.g.addEdge(1, 2, -3)
        self.g.addEdge(1, 3, -2)
        self.g.addEdge(2, 3, -3)

    def test_bellman_ford_(self):
        self.assertEqual(self.g.BellmanFord(0), [0, 2, -1, -4])

    def test_bellman_ford_with_ing(self):
        self.assertEqual(self.g.BellmanFord(1),[float("Inf"), 0, -3, -6])

unittest.main()