from src.sum_the_sum import sum_of_sums
import unittest
import time

class MyTestCase(unittest.TestCase):

    def test1(self):
        self.assertEquals(55, sum_of_sums(3))

    def test2(self):
        self.assertEquals(630, sum_of_sums(5))

    def test3(self):
        self.assertEquals(14740530850, sum_of_sums(100))

    def test4(self):


        tester = 5* (10 ** 4)
        res = sum_of_sums(tester)
        print(f'Sum of sum ={res}')

    def test5(self):
        tester = 9 * 10 ** 8

        start = time.time()
        res = sum_of_sums(tester)
        end = time.time()
        print(f'Res={res} Calculated in {end-start} seconds')

if __name__ == '__main__':
    unittest.main()
