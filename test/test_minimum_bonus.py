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
        tens_idx = [idx  for idx, i in enumerate(tst) if i == 10]
        bonus_pack = [0] * len(tst)
        for idx in tens_idx:
            bonus_pack[idx] = 1

        for idx in tens_idx:
            if idx != 0:
                if tst[idx-1] != 10:
                    bonus_pack[idx-1] =2

            # Ignore this
            if idx != len(tst)-1:
                if tst[idx+1] != 10:
                    bonus_pack[idx+1] =2

        for idx in range(0, len(tst)):
            if bonus_pack[idx] == 0:
                if idx < len(tst) -1:
                    if tst[idx] > tst[idx+1]:
                        bonus_pack[idx] = bonus_pack[idx+1] + 1
                    else:
                        tst[idx] = tst[idx + 1] -1
        print(bonus_pack)
        print(tst)
        print(f'Expected:{[1,2,1,2,3,1,2,3,4,1]}')



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
