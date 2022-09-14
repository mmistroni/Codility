from itertools import combinations
from collections import defaultdict

from collections import defaultdict

class Graph:

    def __init__(self, nodes: int):
        # Store the adjacency list as a dictionary
        # { 0 : [ 1, 2 ], 1 : [ 3, 4 ] }

        # The default dictionary would create an empty list as a default (value)
        # for the nonexistent keys.
        self.adjlist = defaultdict(list)
        self.nodes = nodes

    # Assuming that the edge is bidirectional
    def add_edge(self, src: int, dst: int):
        self.adjlist[src].append(dst)
        self.adjlist[dst].append(src)

    def display_adj_list(self):
        for item in self.adjlist.items():
            print(item)

    def find_distance(self, start, end, dist):
        children = self.adjlist[start]
        if end in children:
            return dist + 1
        else:
            for child in children:
                d = self.find_distance(child, end, dist+1)
                if d:
                    return d

            return 0



def build_graph(A, B):
    graph = Graph(len(A))

    for start, end in zip(A, B):
        graph.add_edge(start, end)
    return graph

def calculate_distances(A, B, graph):
    base_tpls = list(zip(A, B))

    odd_distances = len(base_tpls)


    combis = [c for c in combinations(set(A+B), 2) if c not in base_tpls]
    for start, end in combis:
        d = graph.find_distance(start, end, 0)
        if d % 2 == 1:
            odd_distances +=1
    return odd_distances

def solution(A, B):
    graph = build_graph(A, B)

    return calculate_distances(A, B, graph)