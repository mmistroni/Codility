import unittest

from fib_frog import solution
import heapq
import time

import timeit

def fibonacci_seq(n, limit=None):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

    return [f for f in fib if f <= limit] if limit else fib

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

    def BFS_SP(self):
        graph = self.adjlist
        start = self.nodes[0]
        goal = self.nodes[-1]
        explored = []

        # Queue for traversing the
        # graph in the BFS
        queue = [[start]]

        # If the desired node is
        # reached
        if start == goal:
            print("Same Node")
            return

        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]

            # Condition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = graph[node]

                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour == goal:
                        print("Shortest path = ", *new_path)
                        return len(new_path)
                explored.append(node)

        # Condition when the nodes
        # are not connected
        print("So sorry, but a connecting" \
              "path doesn't exist :(")
        return -1

class MyTestCase(unittest.TestCase):



    def probe_graph(self, A):
        seq = fibonacci_seq(max(len(A), 10))

        seq = seq[1:]
        fib_dict = dict((seq[i], i) for i in range(0, len(seq)))

        ones = [idx for idx in range(0, len(A)) if A[idx] == 1]
        ones = [-1] + ones + [len(A)]

        g = Graph(ones, fib_dict)

        for idx, item in enumerate(ones):
            for dst in ones[idx+1:]:
                g.AddEdge(item, dst)

        g.Display_AdjList()
        print('--Shortest--')
        return g.BFS_SP()



    def test_pythongraph(self):
        # nearly there. We just need to explore adjacency list and graph
        A = [1, 1, 0, 0, 0]
        res = solution(A)

        print(f'-- distance to end is:{res}')


    def test_newtest2(self):
        print('---- NEXT --')
        A = [1, 1, 0, 0, 0]
        res = self.probe_graph(A)
        print(f'-- distance to end is:{res}')

    def test_fibfrog(self):
        from itertools import product, combinations_with_replacement

        #The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number.

        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        fib_seq = fibonacci_seq(len(A) + 1, len(A))[:-1]

        ones = [idx for idx in range(0, len(A)) if A[idx] == 1]

        combilen = len(ones)

        # Step 1, all possible combinations of fibonacci which sums
        # to len(A) + 1

        good_tpls = []

        for p in combinations_with_replacement(fib_seq, combilen):
            if sum(p) == len(A) + 1:
                good_tpls.append(p)

        print(f'Valids are:{good_tpls}')


        ones = [-1] + ones + [len(A)]

        # find  all possible differences between all indexes
        # let's try the product
        print(f'Ones are:{ones} ')
        print(f'Fib seq is {fib_seq}')

        differences = [ones[j] - ones[i] for i in range(len(ones)) for j in range(i + 1, len(ones))]
        print(differences)

        fib_right = [d for d in differences if d < len(fib_seq) and d in fib_seq]
        print(f'Only good ones are :{fib_right}')

        res = [tpl for tpl in good_tpls if all([i in fib_right for i in tpl])]

        s_res = sorted(res, key = lambda t: len(t))
        print(f'Shortest is {s_res[0]}')



        return

        #not good. seems i need to find all possible diffs, notjust
        # difference with previous

        diff = [ones[i + 1] - ones[i] for i in range(len(ones) - 1)]

        # Not yet htere but close. do not uniquify

        goods = list(set(diff).intersection(fib_seq))

        target = len(A)
        tpl = None
        for p in product(goods, repeat=len(goods)):
            print(p)
            if sum(p) == target:
                if tpl is None:
                    tpl = p
                else:
                    if len(p) < len(tpl):
                        tpl = p

        print(f'We have found:{tpl}')






        res = solution(A)
        self.assertEquals(3, res)

    def test_fibfrog2(self):
        A = []
        jumps = solution(A)
        #res = self.probe(A)
        #res = solution(A)

        self.assertEquals(1, jumps)

    def test_fibfrog3(self):
        A = [1]
        jumps = solution(A)
        self.assertEquals(1, jumps)

    def test_fibfrog4(self):
        A = [1, 1, 1]
        start = time.time()
        jumps = self.probe_graph(A)
        end = time.time()
        print(f'{end - start} = {jumps}')

        start = time.time()

        res = solution(A)
        end = time.time()
        print(f'{end - start} = {jumps}')

        self.assertEquals(2, res)

    def test_zeros(self):
        A = [0, 0, 0]
        jumps = solution(A)
        self.assertEquals(-1, jumps)

    def test_anotherfail(self):
        A =  [0, 0, 0, 1, 0]
        jumps =solution(A)
        self.assertEquals(-1, jumps)

    def test_anotheranotherfail(self):
        A = [1, 1, 0, 0, 0]

        res = fibonacci_seq(len(A) + 1, len(A))

        ones = [idx for idx in range(0, len(A)) if A[idx] == 1]
        ones = [-1] + ones + [len(A)]

        # Strategy #1. find all possible differences between the ones

        jumps = 2
        self.assertEquals(2, jumps)
        #https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

    def test_allzerors(self):
        A = [0] * 100000
        start = time.time()
        jumps = self.probe_graph(A)
        end = time.time()
        print(f'{end-start} = {jumps}')
        #https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/


    def test_fib_sequence(self):
        # Promising. But we'll need next step now. So we only have 27 numbers
        # which are less than 100k
        # Then we need to find max distance between start and any items to the end, that will narrow down
        # the numbers to consider as that will be the first jump
        # then comes the difficult part we have to think about as we should find every possible
        # diffs betweeh 1s and see if they are fib numbers.
        start = time.time()
        res = fibonacci_seq(100000, 100000)
        end = time.time()
        print(f'{end - start} = {len(res)}')


if __name__ == '__main__':
    unittest.main()
