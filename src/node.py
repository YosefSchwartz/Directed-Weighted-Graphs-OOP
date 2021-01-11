
class node:
    """
    This class represent one node on directed weighted graph
    each node contain data and unique id
    """
    key: int
    tag: int
    pos: tuple
    weight: float

    def __init__(self, key: int, pos: tuple):
        """
        Constructor function
        """
        self.key = key
        self.pos = pos
        self.weight = 0
        self.tag = 0
        self.CMP = 0

    def getKey(self) -> int:
        """
        :return - key of this node
        """
        return self.key

    def getWeight(self) -> float:
        """
        :return - weight of this node
        """
        return self.weight

    def setWeight(self, weight):
        """
        Set this weight to new weight
        :param - weight
        """
        self.weight = weight

    def getPos(self) -> tuple:
        """
        :return - position of this node, None if none
        """
        return self.pos

    def setPos(self, pos):
        """
        Set this position to new position
        :param - position in tuple
        """
        self.pos = pos

    def getTag(self) -> int:
        """
        :return - tag of this node
        """
        return self.tag

    def setTag(self, tag: int):
        """
        Set this tag to new tag
        :param - tag
        """
        self.tag = tag

    def make_comparator(less_than):
        """
        Compare function, compare two nodes by their weight
        """
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

    def __str__(self):
        """
        ToString function
        """
        s = "key: " + str(self.key) + ", pos: " + str(self.pos)
        return s
