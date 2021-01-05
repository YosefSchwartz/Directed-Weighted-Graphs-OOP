import unittest
from src.DiGraph import DiGraph
from src.node import node
from random import seed
import random


# def graphCreator(vSize: int):
#     graph = DiGraph()
#     for i in range(vSize):
#         n = node(i)
#         graph.add_node(n)
#     return graph


class MyTestCase(unittest.TestCase):

    def adding_test(self):
        # g1 = graphCreator(6)
        g1 = DiGraph()
        for i in range(6):
            pos = (random.uniform(0, 15), random.uniform(0, 15), random.uniform(0, 15))
            g1.add_node(i, pos)
        seed(1)
        inRange = random.randint(0, 6)
        outRange = random.randint(7, 12)
        n1 = g1.get_all_v().get(inRange)
        n2 = g1.get_all_v().get(outRange)
        self.assertEqual(False, (n1 is None))
        self.assertEqual(None, n2)
        g1.add_edge(0, 1, 1)
        g1.add_edge(0, 2, 2.5)
        g1.add_edge(2, 4, 7.9)
        g1.add_edge(2, 0, 16.2)
        eIn0 = g1.all_in_edges_of_node(0)
        eOut0 = g1.all_out_edges_of_node(0)
        self.assertEqual(16.2, eIn0.get(2))
        self.assertEqual(None, eIn0.get(1))
        self.assertEqual(None, eIn0.get(5))
        self.assertEqual(None, eOut0.get(6))
        self.assertEqual(1, eOut0.get(1))
        self.assertEqual(2.5, eOut0.get(2))

    def removing_test(self):
        # g2 = graphCreator(6)
        g2 = DiGraph()
        for i in range(6):
            pos = (random.uniform(0, 15), random.uniform(0, 15), random.uniform(0, 15))
            g2.add_node(i, pos)
        g2.add_edge(0, 1, 1)
        g2.add_edge(0, 2, 2.5)
        g2.add_edge(2, 4, 7.9)
        g2.add_edge(2, 0, 16.2)
        g2.add_edge(2, 5, 1.2)
        g2.add_edge(5, 6, 9.5)
        g2.add_edge(5, 6, 9)
        g2.add_edge(2, 5, 1)
        self.assertEqual(12, g2.get_mc())
        self.assertEqual(6, g2.nodeSize)
        self.assertEqual(6, g2.edgeSize)
        eOut2 = g2.all_out_edges_of_node(2)
        self.assertEqual(7.9, eOut2.get(4))
        self.assertEqual(1.2, eOut2.get(5))
        eOut5 = g2.all_out_edges_of_node(5)
        self.assertEqual(9.5, eOut5.get(6))
        g2.remove_node(5)
        self.assertEqual(None, g2.get_all_v().get(5))
        eOut2 = g2.all_out_edges_of_node(2)
        self.assertEqual(None, eOut2.get(5))
        eOut5 = g2.all_out_edges_of_node(5)
        self.assertEqual(None, eOut5.get(6))
        g2.remove_edge(2, 4)
        eOut2 = g2.all_out_edges_of_node(2)
        self.assertEqual(None, eOut2.get(4))
        self.assertEqual(16, g2.get_mc())
        self.assertEqual(5, g2.nodeSize)
        self.assertEqual(3, g2.edgeSize)


if __name__ == '__main__':
    unittest.main()
