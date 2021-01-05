from math import inf

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface
from queue import PriorityQueue
import json


class GraphAlgo(GraphAlgoInterface):
    ga: DiGraph
    re: dict

    def __init__(self, graph: DiGraph):
        self.ga = graph

    def __init__(self):
        graph = DiGraph([], [])
        self.ga = graph

    def get_graph(self) -> GraphInterface:
        return self.ga

    def load_from_json(self, file_name: str) -> bool:
        try:
            fp = open(file_name)
            g = DiGraph(**json.load(fp))
            self.ga = g
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            graph = {}
            graph["Edges"] = []
            graph["Nodes"] = []
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
        for n in self.get_graph().get_all_v():
            n.setTag(0)

    def Dijkstra(self, src: int):
        dist = PriorityQueue()
        self.re = {}
        self.resetTagTo0()
        for n in self.get_graph().get_all_v():
            n.setWeight(inf)
            self.re[n.getKey()] = None

        tmp = self.get_graph().getNode(src)
        tmp.setWeight(0)
        dist.put(tmp.getWeight(), tmp)

        while dist.empty() is False:
            tmp = dist.get()[1]
            for e in self.get_graph().all_out_edges_of_node(tmp.getKey()):
                dest = e[0]
                destNode = self.get_graph().getNode(dest)
                if destNode.getTag == 0:
                    newDist = e[1] + tmp.getWeight()
                    if newDist < destNode.getWeight:
                        destNode.setWeight(newDist)
                        self.re[dest] = tmp
                        dist.put(destNode.getWeight(),destNode)
            tmp.setTag(1)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.get_graph().getNode(id1) is None or self.get_graph().getNode(id2) is None:
            return float(inf), []

        if id1 is id2:
            return 0, [id1]

        self.Dijkstra(id1,id2)

        dest = self.re.get(id2)[1]
        if dest is None:
            return float(inf), []

        path = []
        dist = dest[1].getWeight

        while dest is not None:
            path.extend(dest)
            dest = self.re.get(dest)[1]

        path.reverse()

        return dist,path

    def __str__(self):
        return str(self.ga)
