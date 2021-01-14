from math import inf
from typing import List

from src.node import node
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from queue import PriorityQueue, Queue
import matplotlib.pyplot as plt
import json
import random as rnd
import numpy as np


class GraphAlgo(GraphAlgoInterface):
    """
    This class represents some algorithms that occurred on DiGraph (directed weighted graph)
    """
    ga: DiGraph

    def __init__(self, graph=None):
        """
        Constructor function
        """
        self.ga = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.ga

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            fp = open(file_name)
            g = DiGraph(**json.load(fp))
            self.ga = g
            fp.close()
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            graph = {"Edges": [], "Nodes": []}
            for n in self.get_graph().get_all_v().values():
                if n.getPos() is not None:
                    pos = str(n.getPos()[0]) + "," + str(n.getPos()[1]) + "," + str(n.getPos()[2])
                else:
                    pos = None
                graph.get("Nodes").extend([{"pos": pos, "id": n.getKey()}])
                eOut = self.get_graph().all_out_edges_of_node(n.getKey())
                for e in eOut.keys():
                    graph.get("Edges").extend([{"src": n.getKey(), "w": eOut.get(e), "dest": e}])
            with open(file_name, 'w') as json_file:
                json.dump(graph, json_file)
            return True
        except Exception as e:
            print(e)
            return False

    def resetTagTo0(self):
        """
        Reset all tags of each node to zero
        """
        for n in self.get_graph().get_all_v().values():
            n.setTag(0)

    def Dijkstra(self, src: int):
        """
        Dijkstra algorithms

        For more:
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        """
        dist = PriorityQueue()
        re = {}
        self.resetTagTo0()

        for n in self.get_graph().get_all_v().values():
            n.setWeight(inf)
            re[n.getKey()] = None

        tmp = self.get_graph().getNode(src)
        tmp.setWeight(0)
        dist.put((tmp.getWeight(), tmp))

        while dist.empty() is False:
            tmp = dist.get()[1]
            for dest in self.get_graph().all_out_edges_of_node(tmp.getKey()):
                destNode = self.get_graph().getNode(dest)
                if destNode.getTag() == 0:
                    edgeW = self.get_graph().all_out_edges_of_node(tmp.getKey()).get(dest)
                    newDist = edgeW + tmp.getWeight()
                    if newDist < destNode.getWeight():
                        destNode.setWeight(newDist)
                        re[dest] = tmp
                        dist.put((destNode.getWeight(), destNode))
            tmp.setTag(1)
        return re

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        :param id1: The start node id
        :param id2: The end node id
        :return: The distance of the path, a list of the nodes ids that the path goes through
        """
        if self.get_graph() is None:
            return float(inf), []
        if self.get_graph().getNode(id1) is None or self.get_graph().getNode(id2) is None:
            return float(inf), []
        if id1 is id2:
            return 0, [id1]
        re = self.Dijkstra(id1)
        dest = re.get(id2)
        dist = self.get_graph().getNode(id2).getWeight()
        if dest is None:
            return float(inf), []
        path = []
        path.extend([id2])
        while dest is not None:
            path.extend([dest.getKey()])
            dest = re.get(dest.getKey())
        path.reverse()
        return dist, path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        :param id1: The node id
        :return: The list of nodes in the SCC

        Notes:
        If the graph is None or id1 is not in the graph,
        the function should return an empty list []
        """
        component = []
        if self.get_graph() is None:
            return component
        if self.get_graph().getNode(id1) is None:
            return component
        n = self.get_graph().getNode(id1)
        self.resetTagTo0()
        Vout = self.DFS(n, [])
        self.resetTagTo0()
        Vin = self.DFS_Opp(n, [])
        return list(set(Vout).intersection(Vin))

    def DFS(self, n: node, s: list):
        """
        DFS algorithms - iterative.
        The list are return sorted by finish time
        work by same principals of regular DFS algorithm

        For more - https://en.wikipedia.org/wiki/Depth-first_search
        :param n: source node
        :param s: list of node, order by finish time, the function will update the list not replace it!
        :return: list of node, sorted by finish time
        """
        q = [n]
        s2 = Queue()
        s1 = []
        n.setTag(1)
        while len(q) > 0:
            n = q.pop()
            Vout = self.get_graph().all_out_edges_of_node(n.getKey())
            niSize = len(Vout)
            for v in Vout.keys():
                nodeV = self.get_graph().getNode(v)
                if nodeV.getTag() == 0:
                    q.append(nodeV)
                    nodeV.setTag(1)
                else:
                    niSize -= 1
            if niSize == 0:
                s2.put(n.getKey())
            else:
                s1.append(n.getKey())
        while s2.empty() is False:
            s.append(s2.get())
        while len(s1) != 0:
            s.append(s1.pop())
        return s

    def DFS_Opp(self, n: node, s: list):
        """
        similar DFS, work on opposite edges (reflected at "all_in_edges_of_node")

        :param n: source node
        :param s: list of node, order by finish time, the function will update the list not replace it!
        :return: list of node, sorted by finish time
        """
        q = [n]
        s2 = Queue()
        s1 = []
        n.setTag(1)
        while len(q) > 0:
            n = q.pop()
            Vin = self.get_graph().all_in_edges_of_node(n.getKey())
            niSize = len(Vin)
            for v in Vin.keys():
                nodeV = self.get_graph().getNode(v)
                if nodeV.getTag() == 0:
                    q.append(nodeV)
                    nodeV.setTag(1)
                else:
                    niSize -= 1
            if niSize == 0:
                s2.put(n.getKey())
            else:
                s1.append(n.getKey())
        while s2.empty() is False:
            s.append(s2.get())
        while len(s1) != 0:
            s.append(s1.pop())
        return s

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        :return: The list all SCC

        Notes:
        If the graph is None the function should return an empty list []
        """
        s = []
        components = []
        self.resetTagTo0()
        for n in self.get_graph().get_all_v().values():
            if n.getTag() == 0:
                self.DFS(n, s)
        # dfs on the opp graph
        self.resetTagTo0()
        while len(s) > 0:
            x = s.pop()
            u = self.get_graph().getNode(x)
            if u.getTag() == 0:
                p = self.DFS_Opp(u, [])
                components.append(sorted(p))
        return components

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        :return: None
        """
        # Get limits of graph
        if self.get_graph() is None:
            return
        minX, minY, maxX, maxY = inf, inf, -inf, -inf
        # This block for compute the limits of screen
        for n in self.get_graph().get_all_v().values():
            if n.getPos() is not None:
                if n.getPos()[0] > maxX:
                    maxX = n.getPos()[0]
                if n.getPos()[0] < minX:
                    minX = n.getPos()[0]
                if n.getPos()[1] > maxY:
                    maxY = n.getPos()[0]
                if n.getPos()[1] < minY:
                    minY = n.getPos()[0]
        # If minX is inf, it mean that all of these variables are inf or -inf
        # and then we decide the limits is x[1,10], y[1,10]
        if minX is inf:
            minX, maxX, minY, maxY = 1, 10, 1, 10
        # Else, if we have limit but the sub is under node size, we increase
        # the limits by n/2 to whole side
        else:
            n = self.get_graph().v_size()
            if maxX - minX < n or maxY - minY < n:
                maxX += n / 2
                minX -= n / 2
                maxY += n / 2
                minY -= n / 2
        k = maxX - minX

        # Insert the x and y value to lists, and if None, compute random value between [min,max]
        X, Y = [], []
        for n in self.get_graph().get_all_v().values():
            if n.getPos() is None:
                n.setPos((rnd.uniform(minX, maxX), rnd.uniform(minY, maxY), rnd.uniform(0, 10)))
            X.extend([n.getPos()[0]])
            Y.extend([n.getPos()[1]])
            plt.annotate(n.getKey(), (n.getPos()[0], n.getPos()[1]), (n.getPos()[0], n.getPos()[1]),
                         c='r')
        plt.scatter(X, Y, s=100)

        # Draw all edges
        for n in self.get_graph().get_all_v().values():
            nX = n.getPos()[0]
            nY = n.getPos()[1]
            for eOut in self.get_graph().all_out_edges_of_node(n.getKey()).keys():
                eX = self.get_graph().getNode(eOut).getPos()[0]
                eY = self.get_graph().getNode(eOut).getPos()[1]
                plt.annotate("", xy=(eX, eY), xytext=(nX, nY), arrowprops=dict(arrowstyle="->"))
        plt.show()

    def __str__(self):
        """
        ToString function
        """
        return str(self.ga)
