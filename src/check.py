import json
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from node import node
from edge import edge
from queue import PriorityQueue


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{},{}".format(self.name, self.age)


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
    # ga.load_from_json("A0.json")
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

    g = DiGraph()
    for i in range(6):
        g.add_node(i)
    g.add_edge(0, 1, 1.5)
    g.add_edge(1, 0, 2)
    g.add_edge(2, 3, 9.23)
    g.add_edge(3, 2, 32)
    g.add_edge(4, 3, 21)
    g.add_edge(2, 4, 41)
    g.add_edge(5, 3, 8)
    g.add_edge(4, 5, 7)
    g.add_edge(0, 5, 87)
    g.add_edge(4, 1, 98)

    ga = GraphAlgo(g)
    # print(ga)

    for n in g.get_all_v().keys():
        print("connected_component of node-> "+str(n))
        print(ga.connected_component(n))
    print("connected_components of g")
    print(ga.connected_components())


if __name__ == '__main__':
    main()
