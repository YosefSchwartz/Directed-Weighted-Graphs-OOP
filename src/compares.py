from math import inf

from src.GraphAlgo import GraphAlgo
import timeit


class checkG:

    @staticmethod
    def checkGraph(File):
        s = File.split("/")
        f = s[2]
        ga = GraphAlgo()
        print(ga)
        start = timeit.default_timer()
        ga.load_from_json(File)
        # ga.plot_graph()
        end = timeit.default_timer()
        print(f)
        print("time to load-> " + str(end - start) + " sec")
        print("connected_components")
        # for i in range():
        #     if ga.shortest_path(0, i) != inf:
        #         if ga.shortest_path(i, 0) != int:
        #             print(i)
        # print()
        start = timeit.default_timer()
        com = ga.connected_components()
        end = timeit.default_timer()
        print("components size: "+str(len(com)))
        print(com)
        print("time to check connected_components-> " + str(end - start) + " sec")
        print("-------------------------------------------")
        print()


def main():

    checkG.checkGraph("../data/G_10_80_1.json")
    # checkG.checkGraph("../data/G_100_800_0.json")
    # checkG.checkGraph("../data/G_1000_8000_0.json")
    # checkG.checkGraph("../data/G_10000_80000_0.json")
    # checkG.checkGraph("../data/G_20000_160000_0.json")
    # checkG.checkGraph("../data/G_30000_240000_0.json")


if __name__ == '__main__':
    main()
