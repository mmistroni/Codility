import unittest
from relative_prime_numbers import relatively_prime

class MyTestCase(unittest.TestCase):

    def test_something1(self):
        self.assertEquals(relatively_prime(8, [1, 2, 3, 4, 5, 6, 7]), [1, 3, 5, 7])

    def test_something2(self):
        self.assertEquals(relatively_prime(15, [72, 27, 32, 61, 77, 11, 40]), [32, 61, 77, 11])

    def test_something3(self):
        self.assertEquals(relatively_prime(210, [15, 100, 2222222, 6, 4, 12369, 99]), [])




if __name__ == '__main__':
    unittest.main()
