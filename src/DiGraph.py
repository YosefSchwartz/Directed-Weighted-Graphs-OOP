from GraphInterface import GraphInterface
from node import node

"""
This class represent a directed weighted graph
It is contain two dictionaries of edges and nodes, two variable that save node and edge size,
and counter for all act that performed on this graph  
"""


class DiGraph(GraphInterface):
    graph: dict
    edges: dict  # {integer:[in:{(int)src:weight},out:{(int)dest:weight}]}
    nodeSize: int
    edgeSize: int
    MC: int


    """
    Constructor function, can get empty graph or from JSON file
    """
    def __init__(self, Edges=None, Nodes=None):
        self.graph = {}
        self.edges = {}
        self.nodeSize = 0
        self.edgeSize = 0
        self.MC = 0
        if Nodes is not None and Edges is not None:
            for n in Nodes:
                if n.get("pos") is not None:
                    p = list(n.get("pos").split(","))
                    newPos = (float(p[0]), float(p[1]), float(p[2]))
                newPos = None
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

    """
    return node by id, o.w. None 
    """
    def getNode(self, key):
        if self.graph is None:
            return None
        return self.graph.get(key)

    """
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    """
    def v_size(self) -> int:
        return self.nodeSize

    """
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    """
    def e_size(self) -> int:
        return self.edgeSize

    """
    return a dictionary of all the nodes in the Graph, each node is represented using a pair
    (node_id, node_data)
    """
    def get_all_v(self) -> dict:
        return self.graph

    """
    return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (other_node_id, weight)
    """
    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.graph is None:
            return None
        if self.graph.get(id1) is None:
            return None
        if self.edges is None:
            return {}
        return self.edges.get(id1)[0]

    """
    return a dictionary of all the nodes connected from node_id , each node is represented using a pair
    (other_node_id, weight)
    """
    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.graph is None:
            return None
        if self.graph.get(id1) is None:
            return None
        if self.edges is None:
            return {}
        return self.edges.get(id1)[1]

    """
    Returns the current version of this graph,
    on every change in the graph state - the MC should be increased
    @return: The current version of this graph.
    """
    def get_mc(self) -> int:
        return self.MC

    """
    Adds an edge to the graph.
    @param id1: The start node of the edge
    @param id2: The end node of the edge
    @param weight: The weight of the edge
    @return: True if the edge was added successfully, False o.w.

    Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
    """
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

    """
    Adds a node to the graph.
    @param node_id: The node ID
    @param pos: The position of the node
    @return: True if the node was added successfully, False o.w.

    Note: if the node id already exists the node will not be added
    """
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

    """
    Removes a node from the graph.
    @param node_id: The node ID
    @return: True if the node was removed successfully, False o.w.

    Note: if the node id does not exists the function will do nothing
    """
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

    """
    Removes an edge from the graph.
    @param node_id1: The start node of the edge
    @param node_id2: The end node of the edge
    @return: True if the edge was removed successfully, False o.w.

    Note: If such an edge does not exists the function will do nothing
    """
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

    """
    Equalization function, check if two graphs are equal by compare nodes and edges.
    """
    def __eq__(self, other):
        if isinstance(other, (DiGraph, GraphInterface)) is False:
            return False
        if sorted(self.graph) != sorted(other.get_all_v()):
            return False
        for n in self.get_all_v().keys():
            eOut1 = sorted(other.all_out_edges_of_node(n))
            eIn1 = sorted(other.all_in_edges_of_node(n))
            eOut2 = sorted(self.all_out_edges_of_node(n))
            eIn2 = sorted(self.all_in_edges_of_node(n))
            if eOut1 != eOut2 or eIn1 != eIn2:
                return False
        return True

    """
    ToString function
    """
    def __str__(self):
        s = ""
        for n in self.graph.values():
            s += str(n) + "\n"
            s += "    edges in: " + str(self.all_in_edges_of_node(n.getKey())) + "\n"
            s += "    edges out: " + str(self.all_out_edges_of_node(n.getKey())) + "\n\n"
        return s
