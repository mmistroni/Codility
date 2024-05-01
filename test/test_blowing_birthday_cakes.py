import unittest
from blowing_birthday_cakes import blow_candles

class MyTestCase(unittest.TestCase):
    def test_something(self):
        def basic_test_cases():
            tests = [
                ["1321", 3],
                ["0323456", 9],
                ["2113", 5],
                ["1110", 1],
                ["121", 2]
            ]
            for st, exp in tests:
                self.assertEqual(blow_candles(st), exp)


if __name__ == '__main__':
    unittest.main()
