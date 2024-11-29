import unittest
from src.snail import can_crawl


class MyTestCase(unittest.TestCase):

    def test_example1(self):
        rubber_band = 10
        snail_speed = 2  # 2 unit minute
        rate_of_rubber_band = 1 # 1 unit minute
        self.assertEqual(True, can_crawl(rubber_band, snail_speed, rate_of_rubber_band))

    def test_example2(self):
        rubber_band = 100
        snail_speed = 1  # 2 unit minute
        rate_of_rubber_band = 2  # 1 unit minute
        self.assertEqual(False, can_crawl(rubber_band, snail_speed, rate_of_rubber_band))


    def test_example3(self):
        rubber_band = 100000
        snail_speed = 0.1  # 2 unit minute
        rate_of_rubber_band = 0.05  # 1 unit minute
        self.assertEqual(False, can_crawl(rubber_band, snail_speed, rate_of_rubber_band))



if __name__ == '__main__':
    unittest.main()
