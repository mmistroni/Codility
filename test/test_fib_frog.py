import unittest

from fib_frog import solution
import heapq

def fibonacci_seq(n):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

def fibonacci2(n):
    if n == 0:
        return 0
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

def find_next(start, nextes, fib_dict):
    holder = []
    for i in nextes:
        diff = i - start
        if diff in fib_dict.keys():
            holder.append(i)

    return holder


def find_all_trees(A):
    def find_all_next(start_idx, remainder, fib_dict):
        return [i for i in remainder if (i - start_idx) in fib_dict.keys()]

    seq = fibonacci_seq(max(len(A), 10))[1:]
    fib_dict = dict((seq[i], i) for i in range(0, len(seq)))
    ones = [idx for idx in range(0, len(A)) if A[idx] == 1]

    adj_list_dict = {}
    ones = [-1] + ones + [len(A)]
    for idx, item in enumerate(ones):
        nxts  = find_all_next(item, ones[idx+1:], fib_dict)
        adj_list_dict[item] = nxts
    adj_list_dict[ones[-1]] = ones[-1]
    return adj_list_dict



def find_jumps(A):
    def dfs(node, graph, visited, component, end):
        component.append(node)  # Store answer
        visited[node] = True  # Mark visited
        if end in component:  # Not quite there. if a component has no children we need to remove it
            return
        for child in graph[node]:
            if not visited.get(child) and graph.get(child):  # Check whether the node is visited or not
                return dfs(child, graph, visited, component, end)


    # Not quite there. we need to check the indexes that got he
    graph = find_all_trees(A)

    component = []
    visited = {}

    dfs(-1, graph, visited, component, len(A))
    jumps = len(component) - 1

    return jumps


from collections import defaultdict


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

class MyTestCase(unittest.TestCase):


    def probe_graph(self, A):
        seq = fibonacci_seq(max(len(A), 10))[1:]
        fib_dict = dict((seq[i], i) for i in range(0, len(seq)))

        ones = [idx for idx in range(0, len(A)) if A[idx] == 1]
        ones = [-1] + ones + [len(A)]

        g = Graph(ones, fib_dict)

        for idx, item in enumerate(ones):
            for dst in ones[idx+1:]:
                g.AddEdge(item, dst)

        g.Display_AdjList()
        print('--Shortest--')
        return g.find_shortest()



    def test_pythongraph(self):
        # nearly there. We just need to explore adjacency list and graph
        A = [1, 1, 0, 0, 0]
        res = self.probe_graph(A)

        print(f'-- distance to end is:{res}')


    def test_newtest2(self):
        print('---- NEXT --')
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        res = self.probe_graph(A)
        print(f'-- distance to end is:{res}')

    def test_fibfrog(self):
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        res = solution(A)
        self.assertEquals(3, res)

    def test_fibfrog2(self):
        A = []
        jumps = find_jumps(A)
        #res = self.probe(A)
        #res = solution(A)

        self.assertEquals(1, jumps)

    def test_fibfrog3(self):
        A = [1]
        jumps = find_jumps(A)
        self.assertEquals(1, jumps)

    def test_fibfrog4(self):
        A = [1, 1, 1]
        res = self.probe_graph(A)
        print(f'-- distance to end is:{res}')


    def test_zeros(self):
        A = [0, 0, 0]
        jumps = find_jumps(A)
        self.assertEquals(-1, jumps)

    def test_anotherfail(self):
        A =  [0, 0, 0, 1, 0]
        jumps = find_jumps(A)
        self.probe_graph(A)

    def test_anotheranotherfail(self):
        A = [1, 1, 0, 0, 0]
        jumps = find_jumps(A)
        self.assertEquals(2, jumps)
        #https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

if __name__ == '__main__':
    unittest.main()
