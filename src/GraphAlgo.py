from math import inf
from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface
from queue import PriorityQueue
import matplotlib.pyplot as plt
import json
import numpy as np
import random as rnd


class GraphAlgo(GraphAlgoInterface):
    ga: DiGraph

    def __init__(self, graph=None):
        self.ga = graph

    def get_graph(self) -> GraphInterface:
        return self.ga

    def load_from_json(self, file_name: str) -> bool:
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
        try:
            graph = {"Edges": [], "Nodes": []}
            for n in self.get_graph().get_all_v().values():
                pos = str(n.getPos()[0]) + "," + str(n.getPos()[1]) + "," + str(n.getPos()[2])
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
        for n in self.get_graph().get_all_v().values():
            n.setTag(0)

    def resetCMPTo0(self):
        for n in self.get_graph().get_all_v().values():
            n.setCMP(0)

    def Dijkstra(self, src: int):
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
        component = []
        if self.get_graph() is None:
            return component
        if self.get_graph().getNode(id1) is None:
            return component
        for n in self.get_graph().get_all_v().values():
            if n.getCMP() != 0:
                if self.shortest_path(id1, n.getKey()[0] != inf and self.shortest_path(n.getKey()), id1)[0] != inf:
                    n.setCMP(1)
                    component.extend([n.getKey()])
            return component

    def connected_components(self) -> List[list]:
        components = []
        if self.get_graph() is None:
            return components
        self.resetCMPTo0()
        for n in self.get_graph().get_all_v().values():
            if n.getCMP() == 0:
                component = self.connected_component(n.getKey())
                components.extend([component])
        self.resetCMPTo0()
        return components

    def dfs(self, key, sign):
        if sign == 0:  # regular graph
            if self.get_graph().getNode(key).setTag(1):
                for dest in self.get_graph().all_out_edges_of_node(key).keys():
                    self.dfs(dest, 0)

        # elif sign == 1: # reversed graph

    def connected_components(self) -> List[list]:
        components = []
        s = []  # stack
        self.resetTagTo0()
        for n in self.get_graph().get_all_v().values():
            if n.getTag() == 0:
                s = self.dfs(n.getKey(), 0)
        self.resetTagTo0()
        while s.__sizeof__() != 0:
            n = s.pop()
            if n.getTag() == 0:
                components.extend([self.dfs(n.getKey(), 1)])
        return components

    def plot_graph(self) -> None:
        # Get limits of graph
        if self.get_graph() is None:
            return
        minX, minY, maxX, maxY = inf, inf, -inf, -inf
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

        if minX is inf:
            minX, maxX, minY, maxY = 1, 10, 1, 10
        else:
            n = self.get_graph().v_size()
            if maxX - minX < n or maxY - minY < n:
                maxX += n / 2
                minX -= n / 2
                maxY += n / 2
                minY -= n / 2
        k = maxX - minX

        X, Y = [], []
        for n in self.get_graph().get_all_v().values():
            if n.getPos() is None:
                n.setPos((rnd.uniform(minX, maxX), rnd.uniform(minY, maxY), rnd.uniform(0, 10)))
            # TODO check situation two nodes on same point
            # while X.__contains__(n.getPos()[0]) is F or Y.__contains__(n.getPos()[1] is True):
            # continue
            X.extend([n.getPos()[0]])
            Y.extend([n.getPos()[1]])
            plt.annotate(n.getKey(), (n.getPos()[0], n.getPos()[1]), (n.getPos()[0] + 1 / k, n.getPos()[1] + 1 / k),
                         c='g')
        plt.scatter(X, Y, s=100)

        for n in self.get_graph().get_all_v().values():
            nX = n.getPos()[0]
            nY = n.getPos()[1]
            for eOut in self.get_graph().all_out_edges_of_node(n.getKey()).keys():
                eX = self.get_graph().getNode(eOut).getPos()[0]
                eY = self.get_graph().getNode(eOut).getPos()[1]
                # TODO draw arrow on edge of node
                plt.annotate("", xy=(eX, eY), xytext=(nX, nY), arrowprops=dict(arrowstyle="->"))
        plt.show()

    def __str__(self):
        return str(self.ga)
