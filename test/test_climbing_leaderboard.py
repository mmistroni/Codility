import unittest
from src.climbing_leaderboard import solution
from heapq import  heappush, heapify, nlargest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        ranked = [100, 100, 50, 40, 40, 20, 10]

        player =   [5, 25, 50, 120 ]

        expected =  [6, 4, 2, 1]

        res = solution(ranked, player)

        self.assertEqual(expected, res)

    def test_something2(self):

        ranked = [100, 90, 90, 80, 75, 60]
        player = [50, 65, 77, 90, 102 ]

        expected =  [6, 5, 4, 2, 1]

        res = solution(ranked, player)

        self.assertEqual(expected, res)



if __name__ == '__main__':
    unittest.main()
