import unittest
from src.tree import Node

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.t1 = Node(25, None)
        self.t2 = Node(12, self.t1)
        self.t3 = Node(18, self.t2)
        self.t4 = Node(40, self.t1)

    def test_something(self):
        print(f'Height of t1 is:{self.t1.height()}')
    def test_something2(self):
        print(f'Height of t2 is:{self.t2.height()}')
    def test_something3(self):
        print(f'Height of t3 is:{self.t3.height()}')
    def test_somethng4(self):
        print(f'Height of t4 is:{self.t4.height()}')

        assert self.t1.height() == 4, 'test 18 failed'


if __name__ == '__main__':
    unittest.main()
