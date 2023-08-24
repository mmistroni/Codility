#https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/
from collections import defaultdict
import heapq
from itertools import takewhile


def fibonacci_seq(n):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib



class Graph:

    def __init__(self, nodes: int, fib_dict):
        # Store the adjacency list as a dictionary
        # { 0 : [ 1, 2 ], 1 : [ 3, 4 ] }

        # The default dictionary would create an empty list as a default (value)
        # for the nonexistent keys.
        self.adjlist = defaultdict(list)
        self.nodes = nodes
        self.fib_dict = fib_dict

    # Assuming that the edge is bidirectional
    def AddEdge(self, src: int, dst: int):
        diff = dst -src
        if diff in self.fib_dict:
            self.adjlist[src].append(dst)
        #self.adjlist[dst].append(src)

    def Display_AdjList(self):
        for item in self.adjlist.items():
            print(item)

    def find_shortest(self):

        def dijkstra(graph, source):
            distance = {node: float('infinity') for node in self.nodes}


            distance[source] = 0
            queue = [(0, source)]
            while queue:
                print('looping...')
                current_distance, current_node = heapq.heappop(queue)

                if current_node == self.nodes[-1]:
                    print('Exiting..')
                    break
                if current_distance > distance[current_node]:
                    continue

                for neighbor  in graph[current_node]:
                    distance_through_current_node = current_distance + 1

                    if distance_through_current_node < distance[neighbor]:
                        distance[neighbor] = distance_through_current_node
                        heapq.heappush(queue, (distance[neighbor], neighbor))

            return distance[current_node]

        return dijkstra(self.adjlist, -1)



def solution(A):
    from collections import Counter

    if not A:
        return 1
    tst = Counter(A)
    if not tst.get(1):
        return -1

    seq = fibonacci_seq(max(len(A), 10))[1:]
    fib_dict = dict((seq[i], i) for i in range(0, len(seq)))

    ones = [idx for idx in range(0, len(A)) if A[idx] == 1]
    ones = [-1] + ones + [len(A)]

    g = Graph(ones, fib_dict)

    for idx, item in enumerate(ones):
        for dst in ones[idx + 1:]:
            g.AddEdge(item, dst)

    res = g.find_shortest()

    if res == 0:
        return -1
    return res
