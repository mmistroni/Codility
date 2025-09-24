import unittest
import itertools

from src.trumpness_detector import trump_detector
class MyTestCase(unittest.TestCase):
    
    def test_one(self):
        self.assertEquals(trump_detector("I will build a huge wall"), 0)
        
    def test_two(self):
        self.assertEquals(4, trump_detector("HUUUUUGEEEE WAAAAAALL"))
    
    def test_three(self):
        self.assertEquals(2.5, trump_detector("MEXICAAAAAAAANS GOOOO HOOOMEEEE"))

    def test_four(self):
        self.assertEquals(1.89, trump_detector("America NUUUUUKEEEE Oooobaaaamaaaaa"))

    def test_five(self):
        self.assertEquals(1.56, 
                trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT"))


    
    def test_something(self):
        # https://www.codewars.com/kata/57829376a1b8d576640000d6/train/python
        def group_consecutive_letters_itertools(sentence: str) -> list:
            """
            Groups consecutive identical letters using itertools.groupby.
            """
            return [(key, len(list(group))) for key, group in itertools.groupby(sentence)]        


        sentence = "IIII KIIIDD YOOOUUU NOOOOOOTTT" #
        # --> 14 extra vowels on 9 base ones give 1.55555555... which is rounded to 1.56
        #"HUUUUUGEEEE WAAAAAALL"

        vowels = ['a', 'e', 'i', 'o', 'u']

        my_sentence = "IIII KIIIDD YOOOUUU NOOOOOOTTT"
        grouped_letters = group_consecutive_letters_itertools(my_sentence)

        sampled = [t for t in grouped_letters if t[0].lower() in vowels]

        reduced = [t[1]-1 for t in sampled]
        print(f'Extras:{sampled}={sum(reduced)}')

        numv = [t[0] for t in sampled]

        print(f'NV:{numv}={len(numv)}')


    


if __name__ == '__main__':
    unittest.main()
