import unittest

from src.bigger_is_greater import solution

class MyTestCase(unittest.TestCase):


    # https://www.nayuki.io/page/next-lexicographical-permutation-algorithm


    # https://www.geeksforgeeks.org/next-permutation/

    def next_permutation(self, word):
        """

        The following algorithm generates the next permutation lexicographically after a given permutation.
        It changes the given permutation in-place.

        Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
        Find the largest index l greater than k such that a[k] < a[l].
        Swap the value of a[k] with that of a[l].
        Reverse the sequence from a[k + 1] up to and including the final element a[n].


        :param word:
        :return:
        """

        # Find pivot
        for k in range(len(word)-2, -1, -1):
            if word[k] < word[k+1]:
                break
        else:
            return False


        #find pivot successor
        for l in range(len(word)-2, k, -1):
            if word[k] < word[l]:
                break
        #swap
        word[k], word[l] = word[l], word[k]

        first = word[0:k+1]
        second = word[k+1:] #[::-1]


        return first + second[::-1]


    def real_next_permutation(self, word):
        #https://stackoverflow.com/questions/4223349/python-implementation-for-next-permutation-in-stl
        pass

    def test_something(self):
        res = solution('ab')
        self.assertEqual('ba', res)

    def test_failed(self):
        res = solution('abdc')
        self.assertEquals('acbd', res)


    def test_something2(self):
        res = solution('bb')
        self.assertEqual('no answer', res)

    def test_something3(self):
        res = solution('hefg')
        self.assertEqual('hegf', res)

    def test_something4(self):
        res = solution('dhck')
        self.assertEqual('dhkc', res)

    def test_something5(self):
        res = solution('dkhc')
        self.assertEqual('hcdk', res)

    def test_something6(self):
        res = solution('abcd')
        self.assertEqual('abdc', res)

    def test_something7(self):
        res = solution('dcbb')
        self.assertEqual('no answer', res)

    def test_next_permsomething3(self):
        input_sequence = [2, 4, 1, 7, 5, 0]

        expected =  [2, 4, 5, 0, 1, 7]

        res = self.next_permutation(input_sequence)
        self.assertEqual(expected, res)

    def test_next_permsomething_sol(self):
        input_sequence = ''.join(map(lambda x: str(x), [2, 4, 1, 7, 5, 0]))

        expected =  ''.join(map(lambda x: str(x), [2, 4, 5, 0, 1, 7]))

        res = solution(input_sequence)
        self.assertEqual(expected, res)




if __name__ == '__main__':
    unittest.main()
