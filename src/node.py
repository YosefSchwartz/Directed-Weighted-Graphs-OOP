class node:
    key: int
    tag: int
    pos: tuple
    weight: float

    def __init__(self, key: int, pos: tuple):
        self.key = key
        self.pos = pos
        self.weight = 0
        self.tag = 0

    def getKey(self) -> int:
        return self.key

    def getWeight(self) -> float:
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getPos(self) -> tuple:
        return self.pos

    def setPos(self, pos):
        self.pos = pos

    def getTag(self) -> int:
        return self.tag

    def setTag(self, tag: int):
        self.tag = tag

    def make_comparator(less_than):
        def compare(x, y):
            if less_than(x, y):
                return -1
            elif less_than(y, x):
                return 1
            else:
                return 0

            return compare

    def __str__(self):
        s = "key: " + str(self.key) + ", pos: " + str(self.pos)
        return s
