import unittest
from Codility.src.frog_jmp import jump

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(3, jump(10,85,30))

if __name__ == '__main__':
    unittest.main()
