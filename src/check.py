
import timeit
from queue import Queue

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
import random



def graphCreator(v: int):
    g = DiGraph()
    for i in range(v):
        pos = (random.uniform(0, 15), random.uniform(0, 15), random.uniform(0, 15))
        g.add_node(i, pos)
    return g

def main():
    # rand_dict = {"age": 34,"name": "yossi"}
    # print(rand_dict)
    # with open("yossi.json", 'w') as json_file:
    #     json.dump(rand_dict, json_file)
    # fp = open("yossi.json")
    # stud_yossi = Student(**json.load(fp))
    # print(stud_yossi)
    #
    # fp = open("A0.json")
    # g = DiGraph(**json.load(fp))
    # print(g)

    # def Convert(string):
    #     li = float(list(string.split(",")))
    #     return li
    #
    # str1 = "2.524,6.2,93.025"
    # print(Convert(str1))
    # li = Convert((str1))
    # print(li[0])

    # ga = GraphAlgo()
    # ga.load_from_json("../data/A0")
    # print(ga)
    # ga.save_to_json("moshe2.json")
    # ga1=GraphAlgo()
    # ga1.load_from_json("moshe2.json")
    # #print(ga1)
    # q = PriorityQueue()
    #
    # q.put((1,"yosef"))
    # tmp = q.get()[1]
    # print(tmp)

    # g = DiGraph()
    # for i in range(6):
    #     g.add_node(i)
    # g.add_edge(0, 1, 5)
    # g.add_edge(3, 2, 32)
    # g.add_edge(4, 3, 21)
    # g.add_edge(3, 2, 32)
    # g.add_edge(4, 3, 21)
    # g.add_edge(2, 4, 41)
    # g.add_edge(5, 3, 8)
    # g.add_edge(4, 5, 7)
    # g.add_edge(0, 5, 87)
    # g.add_edge(4, 1, 98)
    # #
    # ga = GraphAlgo(g)
    # ga.plot_graph()
    # print(ga)

    #
    # for n in g.get_all_v().keys():
    #     print("connected_component of node-> " + str(n))
    #     print(ga.connected_component(n))
    # print("connected_components of g")
    # print(ga.connected_components())

    g = DiGraph()
    for i in range(9):
        g.add_node(i, None)
    g.add_edge(0, 1, 3)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 0, 7)
    g.add_edge(4, 5, 3)
    g.add_edge(5, 6, 3)
    g.add_edge(6, 4, 4)
    g.add_edge(7, 6, 4)
    g.add_edge(7, 8, 3)

    ga = GraphAlgo(g)
    # print(ga.connected_component(4))
    print(ga.connected_components())



    # v, e = 10**6, 10**4
    # random.seed(2)
    # g = graphCreator(v)
    # for i in range(e):
    #     w = random.uniform(0, 30)
    #     n1 = random.randint(0, v - 1)
    #     n2 = random.randint(0, v - 1)
    #     g.add_edge(n1, n2, w)
    # ga1 = GraphAlgo(g)
    # n1 = random.randint(0, v - 1)
    # start = timeit.default_timer()
    # ga1.connected_component(n1)
    # mid = timeit.default_timer()
    # print("time for connected_component-> " + str(mid - start))
    # ga1.connected_components()
    # end = timeit.default_timer()
    # print("time for connected_components-> " + str(end - start))


if __name__ == '__main__':
    main()
