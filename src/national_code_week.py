from itertools import combinations
from collections import defaultdict
import logging

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
            logging.info(item)

    def find_distance(self, start, end, dist, visited):
        visited.add(start)
        children = [c for c in self.adjlist[start] if c not in visited]#
        if not children:
            return
        if end in children:
            return dist + 1
        else:
            for child in children:
                d = self.find_distance(child, end, dist+1, visited)
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
        if (end, start) in base_tpls:
            continue
        d = graph.find_distance(start, end, 0, set())
        if d % 2 == 1:
            odd_distances  +=1 #base_tpls.append((start, end, d))#odd_distances +=1
    return odd_distances

def solution(A, B):
    graph = build_graph(A, B)

    print(f'Adj list is\n{graph.display_adj_list()}')

    return calculate_distances(A, B, graph)