import unittest
from itertools import chain


word_dict = {'hello' : True, 'hellow' : True,
             'world' : True }

class MyTestCase(unittest.TestCase):

    def word_check(self, w):
        holder = []
        for i in range(0, len(w)):
            subset = w[0:i+1]
            if word_dict.get(subset):
                holder.append(subset)
        return holder

    def test_something(self):
        input_string = 'helloworld'

        all_data = [self.word_check(input_string[i:len(input_string)]) for i in range(0, len(input_string))]

        accumulator = chain(*all_data)
        print(set(accumulator))


if __name__ == '__main__':
    unittest.main()
