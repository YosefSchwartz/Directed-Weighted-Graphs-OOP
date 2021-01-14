import timeit
import unittest
from math import inf
from random import seed
import random
# import timeout_decorator
from numpy import sort

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def graphCreator(v: int):
    g = DiGraph()
    for i in range(v):
        pos = (random.uniform(0, 15), random.uniform(0, 15), random.uniform(0, 15))
        g.add_node(i, pos)
    return g


class MyTestCase(unittest.TestCase):
    def test_init(self):
        """
           checks that the init is done like supposed
        """
        g = DiGraph()
        g.add_node(0, None)
        g.add_node(1, None)
        g.add_node(2, (0, 1, 2))
        g.add_edge(0, 2, 5.7)
        g.add_edge(2, 1, 0.4)
        ga = GraphAlgo(g)
        self.assertEqual(g, ga.get_graph())

    def test_load_save_from_json(self):
        """
           checks the correctness of loading and saving from json file
        """
        v, e = 4, 4
        seed(1)
        g = graphCreator(v)
        for i in range(e):
            w = random.uniform(0, 30)
            n1 = random.randint(0, v - 1)
            n2 = random.randint(0, v - 1)
            g.add_edge(n1, n2, w)
        ga1 = GraphAlgo(g)
        ga2 = GraphAlgo()
        ga1.save_to_json("jsonTest.json")  # save g1
        ga2.load_from_json("jsonTest.json")  # load the g1 text file to g2
        self.assertEqual(g, ga2.get_graph())  # check if g2=graph(that g1 init to) like supposed to
        self.assertEqual(ga2.get_graph(), ga1.get_graph())  # check if g2=g1 like supposed to

    @staticmethod
    def save_load_TimeTest():
        """
           checks the time of loading and saving from json file in big graph
        """
        v, e = 1000000, 100000
        seed(2)
        g = graphCreator(v)
        for i in range(e):
            w = random.uniform(0, 30)
            n1 = random.randint(0, v - 1)
            n2 = random.randint(0, v - 1)
            g.add_edge(n1, n2, w)
        ga1 = GraphAlgo(g)
        ga2 = GraphAlgo()
        ga1.save_to_json("jsonTest.json")  # save g1
        ga2.load_from_json("jsonTest.json")

    def test_shortestPath(self):
        """
           checks the correctness of the shortest path
        """
        g = graphCreator(6)
        g.add_edge(0, 1, 0.5)
        g.add_edge(0, 2, 16.6)
        g.add_edge(1, 3, 1.2)
        g.add_edge(1, 2, 1.0)
        g.add_edge(2, 1, 5.5)
        g.add_edge(2, 3, 8.3)
        g.add_edge(4, 2, 7.0)
        g.add_edge(5, 4, 2.0)
        ga = GraphAlgo(g)
        path1 = [0, 1, 2]
        path2 = [5, 4, 2, 1, 3]
        path3 = [2, 1, 3]
        path11 = ga.shortest_path(0, 2)
        path22 = ga.shortest_path(5, 3)
        path33 = ga.shortest_path(2, 3)
        path44 = ga.shortest_path(4, 0)

        self.assertEqual(1.5, path11[0])
        self.assertEqual(15.7, path22[0])
        self.assertEqual(6.7, path33[0])
        self.assertEqual(inf, path44[0])
        self.assertEqual(True, (path11[1] == path1))
        self.assertEqual(True, (path22[1] == path2))
        self.assertEqual(True, (path33[1] == path3))
        self.assertEqual(0, len(path44[1]))
        self.assertEqual(inf, path44[0])

    @staticmethod
    def test_shortestPath_Time():
        """
           checks the time for the shortest path on a big graph
        """
        v, e = 1000000, 100000
        seed(2)
        g = graphCreator(v)
        for i in range(e):
            w = random.uniform(0, 30)
            n1 = random.randint(0, v - 1)
            n2 = random.randint(0, v - 1)
            g.add_edge(n1, n2, w)
        ga1 = GraphAlgo(g)
        n1 = random.randint(0, v-1)
        n2 = random.randint(0, v-1)
        ga1.shortest_path(n1, n2)

    def test_connected_component_s(self):
        """
           checks the correctness of the connected_components and connected_component
        """
        g = graphCreator(6)
        g.add_edge(0, 1, 0.5)
        g.add_edge(0, 2, 16.6)
        g.add_edge(1, 3, 1.2)
        g.add_edge(1, 2, 1.0)
        g.add_edge(2, 1, 5.5)
        g.add_edge(2, 3, 8.3)
        g.add_edge(4, 2, 7.0)
        g.add_edge(5, 4, 2.0)
        ga = GraphAlgo(g)
        component0 = ga.connected_component(0)
        component1 = ga.connected_component(1)
        component2 = ga.connected_component(2)
        component3 = ga.connected_component(3)
        component4 = ga.connected_component(4)
        component5 = ga.connected_component(5)
        self.assertEqual(True, component0 == [0])
        self.assertEqual(True, sorted(component1) == [1, 2])
        self.assertEqual(True, sorted(component2) == [1, 2])
        self.assertEqual(True, component3 == [3])
        self.assertEqual(True, component4 == [4])
        self.assertEqual(True, component5 == [5])

        components = ga.connected_components()
        #  brt
        self.assertEqual(True, (sorted(components) == [[0], [1, 2], [3], [4], [5]]))

        g.add_edge(0, 5, 4)
        g.add_edge(1, 5, 7)
        g.add_edge(4, 1, 12)
        g.add_edge(5, 0, 45)
        g.remove_edge(2, 1)

        c0 = [0, 1, 4, 5]
        c1 = [0, 1, 4, 5]
        c2 = [2]
        c3 = [3]
        c4 = [0, 1, 4, 5]
        c5 = [0, 1, 4, 5]

        component0 = ga.connected_component(0)
        component1 = ga.connected_component(1)
        component2 = ga.connected_component(2)
        component3 = ga.connected_component(3)
        component4 = ga.connected_component(4)
        component5 = ga.connected_component(5)

        self.assertEqual(True, sorted(component0) == c0)
        self.assertEqual(True, sorted(component1) == c1)
        self.assertEqual(True, sorted(component2) == c2)
        self.assertEqual(True, sorted(component3) == c3)
        self.assertEqual(True, sorted(component4) == c4)
        self.assertEqual(True, sorted(component5) == c5)

        g.add_edge(2, 1, 45)
        g.add_edge(3, 2, 7.9)

        components = sorted(ga.connected_components())
        excepted = [[0, 1, 2, 3, 4, 5]]
        self.assertEqual(excepted, sorted(components))

    @staticmethod
    def test_connected_component_time():
        """
           checks the time for the connected_component on a big graph
        """
        v, e = 10**6, 10**5
        seed(2)
        g = graphCreator(v)
        for i in range(e):
            w = random.uniform(0, 30)
            n1 = random.randint(0, v - 1)
            n2 = random.randint(0, v - 1)
            g.add_edge(n1, n2, w)
        ga1 = GraphAlgo(g)
        n1 = random.randint(0, v - 1)
        start = timeit.default_timer()
        ga1.connected_component(n1)
        end = timeit.default_timer()
        print("time for connected_component-> "+str(end-start))

    @staticmethod
    def test_connected_components_time():
        """
           checks the time for the connected_components on a big graph
        """
        v, e = 10**5, 10**5
        seed(2)
        g = graphCreator(v)
        for i in range(e):
            w = random.uniform(0, 30)
            n1 = random.randint(0, v - 1)
            n2 = random.randint(0, v - 1)
            g.add_edge(n1, n2, w)
        ga1 = GraphAlgo(g)
        start = timeit.default_timer()
        ga1.connected_components()
        end = timeit.default_timer()
        print("time for connected_components-> "+str(end-start))


if __name__ == '__main__':
    unittest.main()
