"""
This class represent one node on directed weighted graph
each node contain data and unique id
"""


class node:
    key: int
    tag: int
    CMP:int
    pos: tuple
    weight: float

    """
    Constructor function
    """
    def __init__(self, key: int, pos: tuple):
        self.key = key
        self.pos = pos
        self.weight = 0
        self.tag = 0
        self.CMP = 0

    """
    @return - key of this node
    """
    def getKey(self) -> int:
        return self.key

    """
    @return - weight of this node
    """
    def getWeight(self) -> float:
        return self.weight

    """
    Set this weight to new weight
    @param - weight
    """
    def setWeight(self, weight):
        self.weight = weight

    """
    @return - position of this node, None if none
    """
    def getPos(self) -> tuple:
        return self.pos

    """
    Set this position to new position
    @param - position in tuple
    """
    def setPos(self, pos):
        self.pos = pos

    """
    @return - tag of this node
    """
    def getTag(self) -> int:
        return self.tag

    """
    Set this tag to new tag
    @param - tag
    """
    def setTag(self, tag: int):
        self.tag = tag

    """
    @return - CMP of this node
    """
    def getCMP(self) -> int:
        return self.CMP

    """
    Set this CMP to new CMP
    @param - CMP
    """
    def setCMP(self, CMP: int):
        self.CMP = CMP

    """
    Compare function, compare two nodes by their weight
    """
    def make_comparator(less_than):
        def compare(x, y):
            if less_than(x, y):
                return -1
            elif less_than(y, x):
                return 1
            else:
                return 0

            return compare

    def __repr__(self):
        return str([self.getKey()])
    """
    ToString function
    """
    def __str__(self):
        s = "key: " + str(self.key) + ", pos: " + str(self.pos)
        return s
