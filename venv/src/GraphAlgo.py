from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface
import json


class GraphAlgo(GraphAlgoInterface):
    ga: DiGraph

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

    def __str__(self):
        return str(self.ga)
