from src.GraphAlgo import GraphAlgo
import timeit


class checkG:

    @staticmethod
    def checkGraph(File):
        s = File.split("/")
        f = s[2]
        ga = GraphAlgo()
        start = timeit.default_timer()
        ga.load_from_json(File)
        end = timeit.default_timer()
        print(f)
        print("time to load-> " + str(end - start) + " sec")
        print("connected_components")
        start = timeit.default_timer()
        com = ga.connected_components()
        print("components size: "+str(len(com)))
        print(com)
        end = timeit.default_timer()
        print("time to check connected_components-> " + str(end - start) + " sec")
        print("-------------------------------------------")
        print()


def main():

    checkG.checkGraph("../data/G_10_80_0.json")
    checkG.checkGraph("../data/G_100_800_0.json")
    checkG.checkGraph("../data/G_1000_8000_0.json")
    checkG.checkGraph("../data/G_10000_80000_0.json")
    checkG.checkGraph("../data/G_20000_160000_0.json")
    checkG.checkGraph("../data/G_30000_240000_0.json")


if __name__ == '__main__':
    main()
