import unittest
from blowing_birthday_cakes import blow_candles
import  time
class MyTestCase(unittest.TestCase):

    def test_simple(self):
        candles = "1321"

        '''
         0 2 1
         0 1 1 0
         
        
        
        '''

        self.assertEqual(blow_candles(candles), 3)

    def test_simple2(self):
        candles = "2113"
        self.assertEqual(blow_candles(candles), 5)


    def test_simple3(self):
        candles = "0323456"
        self.assertEqual(blow_candles(candles), 9)


    def test_simple4(self):
        candles = "1110"
        self.assertEqual(blow_candles(candles), 1)

    def test_simple5(self):
        candles = "121"
        self.assertEqual(blow_candles(candles), 2)


    def test_something(self):
        tests = [
            ["1321", 3],
            ["0323456", 9],
            ["2113", 5],
            ["1110", 1],
            ["121", 2]
        ]


        for st, exp in tests:
            start = time.time()

            print(f'testing:{st}')

            self.assertEqual(blow_candles(st), exp)
            end = time.time()
            print(f'Took {start - end}')

if __name__ == '__main__':
    unittest.main()
