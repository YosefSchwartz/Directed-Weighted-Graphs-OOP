from GraphInterface import GraphInterface
from node import node


class DiGraph(GraphInterface):
    graph: dict
    edges: dict  # {integer:[in:{(int)src:weight},out:{(int)dest:weight}]}
    nodeSize: int
    edgeSize: int
    MC: int


    def __init__(self, Edges=None, Nodes=None):
        self.graph = {}
        self.edges = {}
        self.nodeSize = 0
        self.edgeSize = 0
        self.MC = 0
        if Nodes is not None and Edges is not None:
            for n in Nodes:
                p = list(n.get("pos").split(","))
                newPos = (float(p[0]), float(p[1]), float(p[2]))
                newNode = node(n.get("id"), newPos)
                self.graph[n.get("id")] = newNode
                self.nodeSize += 1
                self.MC += 1
                self.edges[n.get("id")] = [{}, {}]
            for e in Edges:
                src = e.get("src")
                dest = e.get("dest")
                w = e.get("w")
                self.add_edge(src, dest, w)

    def getNode(self, key):
        if self.graph is None:
            return None
        return self.graph.get(key)

    def v_size(self) -> int:
        return self.nodeSize

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.graph is None:
            return None
        if self.graph.get(id1) is None:
            return None
        if self.edges is None:
            return {}
        return self.edges.get(id1)[0]

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.graph is None:
            return None
        if self.graph.get(id1) is None:
            return None
        if self.edges is None:
            return {}
        return self.edges.get(id1)[1]

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.graph is None:
            return False
        if self.graph.get(id1) is None or self.graph.get(id2) is None or id1 is id2:
            return False

        if self.edges.get(id1)[1].get(id2) is None:
            self.edges.get(id1)[1][id2] = weight
            self.edges.get(id2)[0][id1] = weight
            self.edgeSize += 1
            self.MC += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.graph.get(node_id) is not None:
            return False
        else:
            n = node(node_id, pos)
            self.graph[n.getKey()] = n
            self.edges[n.getKey()] = [{}, {}]
            self.nodeSize += 1
            self.MC += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if self.graph is None:
            return False
        if self.graph.get(node_id) is None:
            return False
        for eIn in self.edges.get(node_id)[0]:
            self.edges.get(eIn)[1].pop(node_id)
            self.edgeSize -= 1
            self.MC += 1
        for eOut in self.edges.get(node_id)[1]:
            self.edges.get(eOut)[0].pop(node_id)

        self.edges.pop(node_id)
        self.graph.pop(node_id)
        self.nodeSize -= 1
        self.MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (self.graph.get(node_id1) == None or self.graph.get(node_id2) == None):
            return False
        if (self.edges.get(node_id1)[1].get(node_id2) == None):
            return False

        self.edges.get(node_id1)[1].pop(node_id2)
        self.edges.get(node_id2)[0].pop(node_id1)
        self.edgeSize -= 1
        self.MC += 1
        return True

    def __eq__(self, other):
        if isinstance(other, (DiGraph, GraphInterface)) is False:
            print("1")
            return False

        if sorted(self.graph) != sorted(other.get_all_v()):
            print("2")
            return False
        for n in self.get_all_v().keys():
            eOut1 = sorted(other.all_out_edges_of_node(n))
            eIn1 = sorted(other.all_in_edges_of_node(n))
            eOut2 = sorted(self.all_out_edges_of_node(n))
            eIn2 = sorted(self.all_in_edges_of_node(n))
            if eOut1 != eOut2 or eIn1 != eIn2:
                print("3")
                return False
        return True

    def __str__(self):
        s = ""
        for n in self.graph.values():
            s += str(n) + "\n"
            s += "    edges in: " + str(self.all_in_edges_of_node(n.getKey())) + "\n"
            s += "    edges out: " + str(self.all_out_edges_of_node(n.getKey())) + "\n\n"
        return s
