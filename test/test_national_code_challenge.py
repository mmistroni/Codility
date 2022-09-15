import unittest

from national_code_week import solution, build_graph

class MyTestCase(unittest.TestCase):
    def test_one(self):
        A = [0, 3, 4, 2, 6, 3]
        B = [3, 1, 3, 3,  3, 5]
        self.assertEqual(6, solution(A, B))

    def test_two(self):
        A = [0, 4, 4, 2, 7, 6, 3]
        B = [3, 5, 1, 3, 4, 3, 4]
        res = solution(A, B)
        #from pprint  import pprint
        #pprint(res)
        self.assertEqual(16, res )

    def test_three(self):
        A = [0, 4, 2, 2, 4]
        B = [1, 3, 1, 3, 5]
        self.assertEqual(9, solution(A, B))

    def xtest_buildAdjacency(self):
        A = [0, 3, 4, 2, 6, 3]
        B = [3, 1, 3, 3, 3, 5]

        from collections import defaultdict
        from itertools import combinations

        graph = build_graph(A, B)
        print(graph.display_adj_list())
        
        
        for start, end in combinations(set(A+B), 2):
            print(f'Distance between {start}, {end}={graph.find_distance(start, end, 0)}')


            

if __name__ == '__main__':
    unittest.main()
