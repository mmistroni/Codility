import unittest
import itertools

from src.trumpness_detector import trump_detector
class MyTestCase(unittest.TestCase):
    
    def test_one(self):
        self.assertEquals(trump_detector("I will build a huge wall"), 0)
        
    def test_two(self):
        self.assertEquals(4, trump_detector("HUUUUUGEEEE WAAAAAALL"))
    
    
    def test_something(self):
        sentence = "HUUUUUGEEEE WAAAAAALL"

        vowels = ['a', 'e', 'i', 'o', 'u']

        # 1. Filter out non-alphabetic characters and convert to lowercase
        letters = [char for char in sentence.lower() if char in vowels]

        # 2. Sort the list of letters
        sorted_letters = sorted(letters)
        
        # 3. Use itertools.groupby to group and count
        letter_counts = {}
        for key, group in itertools.groupby(sorted_letters):
            letter_counts[key] = len(list(group))
        
        dupes = 0
        vowels = []
        for k, l in letter_counts.items():
            if l > 1:
                dupes += (l-1)
                vowels.append(k)

        print(f'vowels:{len(vowels)}, extra:{dupes}, res:{dupes / len(vowels)}')



    


if __name__ == '__main__':
    unittest.main()
