from node import node

class edge:
    weight:float
    src:node
    dest:node

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def setSrc (self, src):
        self.src = src

    def getSrc(selfself) -> node:
        return self.src

    def setdest(self, dest):
        self.dest = dest

    def getdest(selfself) -> node:
        return self.dest

    def setweight(self, weight):
        self.weight = weight

    def getweight(selfself) -> float:
        return self.weight

