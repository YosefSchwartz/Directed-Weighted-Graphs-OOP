import json
import random
from math import inf
import networkx as nx

from src.GraphAlgo import GraphAlgo
import timeit


class checkG:

    @staticmethod
    def load_from_json(file_name: str) -> nx.DiGraph():
        gg = nx.DiGraph()
        with open(file_name) as json_file:
            data = json.load(json_file)
            if data is not None:
                for node in data["Nodes"]:
                    key = node["id"]
                    if len(node) > 1:
                        pos = node["pos"]
                        gg.add_node(key, pos=pos)
                    else:
                        gg.add_node(key)
                for edge in data["Edges"]:
                    gg.add_edge(edge["src"], edge["dest"], weight=edge["w"])

                return gg

    @staticmethod
    def checkGraph(File):
        random.seed(5)
        s = File.split("/")
        f = s[2]
        ga = GraphAlgo()
        gaN = checkG.load_from_json(File)
        ga.load_from_json(File)
        # ga.plot_graph()
        print(f)
        print("  ---")

        v = ga.get_graph().get_all_v()
        v1 = random.choice(v).getKey()
        v2 = random.choice(v).getKey()

        start0 = timeit.default_timer()
        s1 = ga.shortest_path(v1, v2)
        end0 = timeit.default_timer()

        st = timeit.default_timer()
        s2 = nx.dijkstra_path(gaN, v1, v2)
        en = timeit.default_timer()
        s2d = nx.dijkstra_path_length(gaN, v1, v2)

        start = timeit.default_timer()
        com = ga.connected_components()
        end = timeit.default_timer()

        start1 = timeit.default_timer()
        com1 = nx.strongly_connected_components(gaN)
        end1 = timeit.default_timer()

        print("time to check shortest_path in Python-> " + str(end0 - start0) + " sec")
        print("time to check shortest_path in NetworkX-> " + str(en - start) + " sec")
        print("time to check connected_components in Python-> " + str(end - start) + " sec")
        print("time to check connected_components in NetworkX-> " + str(end1 - start1) + " sec")
        n = random.choice(v).getKey()
        print("connected_component on Node num -> " +str(n))
        start = timeit.default_timer()
        com = ga.connected_component(n)
        end = timeit.default_timer()
        # print(com)
        print("time to check connected_component-> " + str(end - start) + " sec")
        print("shortest_path")
        print("s1 -> " + str(s1))
        print("s2 -> (" + str(s2d) + ", " + str(s2) + ")")
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
