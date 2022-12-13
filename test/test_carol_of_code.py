import unittest
from carol_of_code import solution

class MyTestCase(unittest.TestCase):

    def rotate(self, item, clockwise=True):
        if not clockwise:
            return item[1:] + [item[0]]
        else:
            return [item[-1]] + item[0:3]


    def test_rotate(self):
        inarr = list("WRGB")
        print(f'Clockwise: in:{inarr}, out:{self.rotate(inarr)}')



    def find_closest(self, left, right):
        right_side = left[2]
        left_side = right[4]

        if right_side == left_side:
            return 0
        else:
            right_in_right = right.find(right_side)
            left_in_left = left.find()






    def test_something(self):
        A =  ["RGBW", "GBRW"],
        self.assertEqual(1, solution(A))

    def test_something2(self):
        A = ["WBGR", "WBGR", "WRGB", "WRGB", "RBGW"]
        self.assertEqual(4, solution(A))

    def test_something3(self):
        A =  ["RBGW", "GBRW", "RWGB", "GBRW"],
        self.assertEqual(2, solution(A))

    def test_something4(self):
        A = ["GBRW", "RBGW", "BWGR", "BRGW"]
        self.assertEqual(2, solution(A))


if __name__ == '__main__':
    unittest.main()
