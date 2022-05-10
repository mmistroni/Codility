import unittest

from src.stonewall import  solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [8, 8,  5, 7, 9,  8, 7, 4,  8]
        self.assertEqual(7, solution(A))

    def test_wrong(self):
        A = [1,1,1]
        self.assertEqual(1, solution(A))

    def test_wrong2(self):
        A = [1, 2, 3, 3, 2, 1]
        self.assertEquals(3, solution(A))


    def test_calculateTAnkLenght(self):
        import math
        vt = 3500 * 1000
        rds = 120 / 2
        prdct = rds * rds * math.pi
        print(vt / prdct)


#30-92-93
#63551368
# Md M ahasan
if __name__ == '__main__':
    unittest.main()
