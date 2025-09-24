import unittest
import itertools
from src.trumpness_detector import trump_detector

class MyTestCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(0, trump_detector("I will build a huge wall"))
    
    def test_two(self):

        self.assertEqual(4, trump_detector("HUUUUUGEEEE WAAAAAALL"))
    def test_three(self):
        self.assertEquals( 2.5, trump_detector("MEXICAAAAAAAANS GOOOO HOOOMEEEE"))
    def test_four(self):
        self.assertEquals(1.89, trump_detector("America NUUUUUKEEEE Oooobaaaamaaaaa"))
    def test_five(self):
        self.assertEquals(1.56, 
                          trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT"))
    def test_mytester(self):
        sentence = 'HUUUUUGEEEE WAAAAAALL'

        letters = [char for char in sentence if char in ['A', 'E', 'I', 'O', 'U']]

        # 2. Sort the list of letters
        sorted_letters = sorted(letters)
        
        # 3. Use itertools.groupby to group and count
        letter_counts = {}
        for key, group in itertools.groupby(sorted_letters):
            letter_counts[key] = len(list(group))
            
        print(letter_counts)




if __name__ == '__main__':
    unittest.main()
