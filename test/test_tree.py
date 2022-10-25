import unittest
from tree import Node

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.t1 = Node(25, None)
        self.t2 = Node(12, self.t1)
        self.t3 = Node(18, self.t2)
        self.t4 = Node(40, self.t1)

    def test_something(self):
        assert self.t1.height() == 4, 'test 18 failed'


if __name__ == '__main__':
    unittest.main()
