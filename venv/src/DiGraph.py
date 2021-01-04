
from GraphInterface import GraphInterface
from node import node
from edge import edge

class DiGraph(GraphInterface):
    graph:dict
    edges:dict
    nodeSize:int
    edgeSize:int
    MC:int

    def __init__(self):
        self.graph = {}
        self.edges = {}
        self.nodeSize = 0
        self.edgeSize = 0
        self.MC = 0

    def __init__(self, Edges, Nodes):
        self.graph = {}
        self.edges = {}
        self.nodeSize = 0
        self.edgeSize = 0
        self.MC = 0
        for n in Nodes:
            p = list(n.get("pos").split(","))
            newPos = (float(p[0]),float(p[1]),float(p[2]))
            newNode = node(n.get("id"),newPos)
            self.graph[n.get("id")] = newNode
            self.nodeSize+=1
            self.MC += 1
            self.edges[n.get("id")] = [{},{}]
        for e in Edges:
            src = e.get("src")
            dest = e.get("dest")
            w = e.get("w")
            self.add_edge(src,dest,w)

    def v_size(self) -> int:
        return self.nodeSize

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.edges.get(id1)[0]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges.get(id1)[1]

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if(self.graph.get(id1)==None or self.graph.get(id2) ==None):
            return False
        if(self.edges.get(id1)[1].get(id2) == None):
            self.edges.get(id1)[1][id2]=weight
            self.edges.get(id2)[0][id1]=weight
            self.edgeSize+=1
            self.MC+=1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if (self.graph.get(node_id) != None):
            return False
        else:
            n = node(node_id, pos)
            self.graph[node_id] = n
            self.edges[node_id] = [{},{}]
            self.nodeSize += 1
            self.MC+=1
            return True

    def remove_node(self, node_id: int) -> bool:
        if(self.graph.get(node_id)==None):
            return False
        for eIn in self.edges.get(node_id)[0]:
            self.edges.get(eIn)[1].pop(node_id)
            self.edgeSize-=1
            self.MC += 1
        for eOut in self.edges.get(node_id)[1]:
            self.edges.get(eOut)[0].pop(node_id)

        self.edges.pop(node_id)
        self.graph.pop(node_id)
        self.nodeSize-=1
        self.MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if(self.graph.get(node_id1)==None or self.graph.get(node_id2)==None):
            return False
        if(self.edges.get(node_id1)[1].get(node_id2)==None):
            return False

        self.edges.get(node_id1)[1].pop(node_id2)
        self.edges.get(node_id2)[0].pop(node_id1)
        self.edgeSize-=1
        self.MC += 1
        return True

    def __str__(self):
        s=""
        for n in self.graph.values():
            s+=str(n)+"\n"
            s+="    edges in: "+str(self.all_in_edges_of_node(n.getKey()))+"\n"
            s+="    edges out: "+str(self.all_out_edges_of_node(n.getKey()))+"\n\n"
        return s

