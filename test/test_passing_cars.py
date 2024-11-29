import unittest
from src.passing_cars import solution
from src.genomic_range_query import prefix_sums

class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [0, 1, 0, 1, 1]
        self.assertEquals(5, solution(A))

    def test_other(self):
        A = [0, 1, 0, 1, 1]
        zeros = []
        # we need to track the zeros
        passing_counter = 0
        for idx, item in enumerate(A):
            if item == 0:
                zeros.append(idx)
            else:
                passing_counter += len(zeros)
                if passing_counter > 1000000000:
                    return -1

        print(passing_counter)





if __name__ == '__main__':
    unittest.main()
