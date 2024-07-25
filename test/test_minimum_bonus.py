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


def _calculate_bonus(inarray):
    bon_array = []
    for idx in range(0, len(inarray)):
        if idx == 0:
            if inarray[idx] < inarray[idx+1]:
            # first one, default 1
                bon_array.append(1)
        else:
            if inarray[idx] > inarray[idx - 1]:
                latest = bon_array[-1]
                bon_array.append(latest + 1)
            else:
                bon_array.append(1)

    return bon_array


def _minimum_bonus(scores):
    allb = _calculate_bonus(scores)



    return sum(allb)



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

    def _rule_of_10(self, tst):
        tens_idx = [idx  for idx, i in enumerate(tst) if i == 10]
        bonus_pack = [0] * len(tst)
        for idx in tens_idx:
            bonus_pack[idx] = 1
            if idx > 0:
                bonus_pack[idx-1] = 2
            if idx < len(tst)-1:
                bonus_pack[idx+1] = 2

        print(f'Tst is:{tst}')
        print(f'Bonus is:{bonus_pack}')

        # once we fill the 10s we start to fill the right
        # then the left
        # then we have to fill the array till all zeros are gone


    def test_rule_of_10(self):
        tst = [20, 30, 40, 30, 20, 10]# 1 2 3  2 1 1
        # working
        # [20, 30, 10, 30, 40, 10, 20, 30, 40, 30]# 6
        res = self._rule_of_10(tst)
        # Next stop: start from the first item you can populate on the right
        #print(res)
        #print(sum(res))
        #self.assertEquals(13, sum(res))

    def test_rule_of_10_2(self):
        tst = [10, 20, 30]
                           # working
        # [20, 30, 10, 30, 40, 10, 20, 30, 40, 30]# 6
        res = self._rule_of_10(tst)
        # Next stop: start from the first item you can populate on the right
        #print(res)
        #print(sum(res))
        #self.assertEquals(13, sum(res))

    def test_rule_of_10_3(self):
        tst = [30, 20, 10]
        self._rule_of_10(tst)

    def test_rule_of_10_4(self):
        tst =  [10, 20, 20, 30]
        self._rule_of_10(tst)

    def test_rule_of_10_5(self):
        tst =  [20, 20, 20, 20]
        self._rule_of_10(tst)

    def test_rule_of_10_5(self):
        tst =  [20, 30, 40, 30, 20, 10]
        self._rule_of_10(tst)


    def xtester1(self):

        tst = [20,30,10,30,40,10,20,30,40,30]

        res = self.calculate_bonus(tst)

        print(f'Array is:{res}. sum is:{sum(res)}')



    def test_1(self):
        self.assertEqual(_minimum_bonus([20,30,10,30,40,10,20,30,40,30]),20)

    def test_1(self):
        self.assertEqual(_minimum_bonus([10, 20, 30]), 6)

    def test_2(self):
        self.assertEqual(_minimum_bonus([30, 20, 10]), 6)




    def test_3(self):
        self.assertEqual(minimum_bonus([30, 20, 20, 10]), 6)

    def test_4(self):

        self.assertEqual(minimum_bonus([10, 20, 20, 30]), 6)

    def test_5(self):
        self.assertEqual(minimum_bonus([20, 20, 20, 20]), 4)

    def test_6(self):
        self.assertEqual(minimum_bonus([20, 30, 40, 30, 20, 10]), 13)
        #                                 1   2   4    3    2    1





if __name__ == '__main__':
    unittest.main()
