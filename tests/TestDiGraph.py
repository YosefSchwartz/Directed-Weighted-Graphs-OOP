import random
import unittest

from src.DiGraph import DiGraph


def graphCreator(vSize: int):
    g = DiGraph()
    for i in range(7):
        pos = (random.uniform(0, 15), random.uniform(0, 15), random.uniform(0, 15))
        g.add_node(i, pos)
    return g


class MyTestCase(unittest.TestCase):

    def test_add_of_edge_node(self):
        """
            checks the adding of nodes and edges to the graph
        """
        g1 = graphCreator(6)
        random.seed(1)
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

    def test_removing(self):
        """
           checks the removing of nodes and edges from the graph
        """
        g2 = graphCreator(7)
        g2.add_edge(0, 1, 1)
        g2.add_edge(0, 2, 2.5)
        g2.add_edge(2, 4, 7.9)
        g2.add_edge(2, 0, 16.2)
        g2.add_edge(2, 5, 1.2)
        g2.add_edge(5, 6, 9.5)
        g2.add_edge(5, 6, 9)
        g2.add_edge(2, 5, 1)
        self.assertEqual(13, g2.get_mc())
        self.assertEqual(7, g2.nodeSize)
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
        self.assertEqual(None, eOut5)
        g2.remove_edge(2, 4)
        eOut2 = g2.all_out_edges_of_node(2)
        self.assertEqual(None, eOut2.get(4))
        self.assertEqual(15, g2.get_mc())
        self.assertEqual(6, g2.nodeSize)
        self.assertEqual(4, g2.edgeSize)


if __name__ == '__main__':
    unittest.main()
