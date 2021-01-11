import random
from math import inf

from src.GraphAlgo import GraphAlgo
import timeit


class checkG:

    @staticmethod
    def checkGraph(File):
        s = File.split("/")
        f = s[2]
        ga = GraphAlgo()
        ga.load_from_json(File)
        # ga.plot_graph()
        print(f)
        print("connected_components")
        start = timeit.default_timer()
        com = ga.connected_components()
        end = timeit.default_timer()
        print("components size: "+str(len(com)))
        # print(com)
        print("time to check connected_components-> " + str(end - start) + " sec")
        v = ga.get_graph().get_all_v()
        n = random.choice(v).getKey()
        print("connected_component on Node num -> " +str(n))
        start = timeit.default_timer()
        com = ga.connected_component(n)
        end = timeit.default_timer()
        # print(com)
        print("time to check connected_component-> " + str(end - start) + " sec")
        print("-------------------------------------------")
        print()


def main():

    checkG.checkGraph("../data/G_10_80_1.json")
    checkG.checkGraph("../data/G_100_800_1.json")
    checkG.checkGraph("../data/G_1000_8000_1.json")
    checkG.checkGraph("../data/G_10000_80000_1.json")
    checkG.checkGraph("../data/G_20000_160000_1.json")
    checkG.checkGraph("../data/G_30000_240000_1.json")


if __name__ == '__main__':
    main()
