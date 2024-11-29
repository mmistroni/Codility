import unittest

from src.toptal2 import arrange

class MyTestCase(unittest.TestCase):

    def test_something1(self):
        P = [1,4,1]
        S = [1, 5 ,1]
        res = arrange(P, S)
        print(f'Result is:{res}')
        self.assertEqual(2, res)

    def test_something2(self):
        P = [4, 4, 2, 4]
        S = [5,5,2,5]
        res = arrange(P, S)
        print(f'Result is:{res}')
        self.assertEqual(3, res)

    def test_something3(self):
        P = [2,3,4,2]
        S = [2,5,7,2]
        res = arrange(P, S)
        print(f'Result is:{res}')
        self.assertEqual(2, res)




if __name__ == '__main__':
    unittest.main()
