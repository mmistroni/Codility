import unittest

from src.pi_code_challenge import solution

from collections import Counter


class MyTestCase(unittest.TestCase):

    def try_with_counter(self, s1, s2):
        if s1 ==  s2:
            return len(s1)
        len_to_check = len(s1)
        c = Counter(s1 + s2)
        sorted_items = sorted(c.items(), key=lambda x: x[1], reverse=True)

        start = 0;
        letters  =0
        while start < len_to_check:
            tpl = sorted_items.pop(0)
            letters  +=1
            start += tpl[1]

        return letters



    def test_something(self):
        p, q  = "abc", 'bcd'

        self.assertEqual(2, solution(p, q))

    def test_something2(self):
        p, q  = "axxz", 'yzwy'

        self.assertEqual(2, solution(p, q))

    def test_something3(self):
        p, q  = "bacad", 'abada'

        self.assertEqual(1, solution(p, q))

    def test_something4(self):
        p, q  = "amz", 'amz'

        self.assertEqual(3, solution(p, q))



if __name__ == '__main__':
    unittest.main()
