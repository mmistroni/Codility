from sum_the_sum import sum_of_sums
import unittest

class MyTestCase(unittest.TestCase):

    def test1(self):
        self.assertEquals(55, sum_of_sums(3))

    def test2(self):
        self.assertEquals(630, sum_of_sums(5))

    def test3(self):
        self.assertEquals(14740530850, sum_of_sums(100))



if __name__ == '__main__':
    unittest.main()
