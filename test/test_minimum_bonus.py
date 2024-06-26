import unittest

from minimum_bonus import minimum_bonus


sample_test_cases = [
    #                     scores      expected
    ([20,30,10,30,40,10,20,30,40,30],   20),
    (                   [10, 20, 30],    6),
    (                   [30, 20, 10],    6),
    (               [30, 20, 20, 10],    6),
    (               [10, 20, 20, 30],    6),
    (               [20, 20, 20, 20],    4),
    (       [20, 30, 40, 30, 20, 10],   13),
]

class MyTestCase(unittest.TestCase):


    def calculate_bonus(self, inarray):
        bon_array = []
        for idx in range(0, len(inarray)):
            if idx == 0:
                # first one, default 1
                bon_array.append(1)
            else:
                if inarray[idx] > inarray[idx-1]:
                    latest = bon_array[-1]
                    bon_array.append(latest + 1)
                else:
                    bon_array.append(1)

        return bon_array


    def test_rule_of_10(self):
        tst = [20, 30, 10, 30, 40, 10, 20, 30, 40, 30]
        tens = [1 if i == 10 else 0 for i in tst]
        # then we know where the tens are
        # so we can start populating array from there



        # what we are trying to do is to find tens. and then work
        # out from the tens

        print(tens)







    def xtester1(self):

        tst = [20,30,10,30,40,10,20,30,40,30]

        res = self.calculate_bonus(tst)

        print(f'Array is:{res}. sum is:{sum(res)}')



    def test_1(self):
        self.assertEqual(minimum_bonus([20,30,10,30,40,10,20,30,40,30]),20)

    def test_1(self):
        self.assertEqual(minimum_bonus([10, 20, 30]), 6)

    def test_2(self):
        self.assertEqual(minimum_bonus([30, 20, 10]), 6)
    def test_3(self):
        self.assertEqual(minimum_bonus([30, 20, 20, 10]), 6)

    def test_4(self):

        self.assertEqual(minimum_bonus([10, 20, 20, 30]), 6)

    def test_5(self):
        self.assertEqual(minimum_bonus([20, 20, 20, 20]), 4)

    def test_6(self):
        self.assertEqual(minimum_bonus([20, 30, 40, 30, 20, 10]), 13)




if __name__ == '__main__':
    unittest.main()
