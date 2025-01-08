from src.magic_music_box import magic_music_box, pattern, notes_dict
import re
import unittest
from collections import defaultdict
import logging

class MyTestCase(unittest.TestCase):
    sample_test_cases = [
        ('Simple example',
         ['DOWN', 'REPTILE', 'AMIDST', 'SOFA'],  # words
         ['DOWN', 'REPTILE', 'AMIDST', 'SOFA'],  # expected
         ),
        ('Example',
         ['DOWN', 'PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'SILENCE', 'DOWN', 'MARKDOWN'],  # words
         ['DOWN', 'REPTILE', 'AMIDST', 'SOFA', 'SOLAR', 'PLANE', 'SILENCE', 'MARKDOWN'],  # expected
         ),
        ('Empty',
         [],  # words
         [],  # expected
         ),
    ]

    def test_one(self):
        words = ['DOWN', 'REPTILE', 'AMIDST', 'SOFA'] # words
        expected = ['DOWN', 'REPTILE', 'AMIDST', 'SOFA']  # expected
        result = magic_music_box(words)
        self.assertEqual(expected, result)

    def test_two(self):
        words = ['DOWN', 'PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'SILENCE', 'DOWN', 'MARKDOWN'] # words

        expected = ['DOWN', 'REPTILE', 'AMIDST', 'SOFA', 'SOLAR', 'PLANE', 'SILENCE', 'MARKDOWN']  # expected
        res = magic_music_box(words)
        self.assertEqual(expected, res)

    def test_sample2(self):
        #words = ['DOWN', 'PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'SILENCE', 'DOWN', 'MARKDOWN']
        #expected = ['DOWN', 'REPTILE', 'AMIDST', 'SOFA', 'SOLAR', 'PLANE', 'SILENCE', 'MARKDOWN']  # expected
        words = []
        expected = []
        
        patterns = "DO|RE|MI|FA|SOL|LA|SI".split("|")
        
        found = []
        dupes = []

        while True:

            # we exit either when array is empty or when we found all the notes
            if not words:
                break
            # we need to find out the second condition, when the array is not empty    
            for note in patterns:
                note_found = False
                logging.info(f'Checking:{note} ')
                # if we cannot find the note in any of the workds
                for idx, word in enumerate(words):
                    if note in word:
                        if word not in found:
                            found.append(word)
                        else:
                            dupes.append(word)
                        note_found = True
                        words.pop(idx)   
                if not note_found:
                    return found         
            if not found:
                break
        print(f'We found:\n {found}')
        
        self.assertEqual(expected, found)

    
    
    def test_four(self):
        res = magic_music_box(['DOWN', 'AMIDST', 'SOFA', 'FACTION'])
        self.assertEqual(res, ['DOWN'])


    def test_five(self):
    
        res = magic_music_box(['PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'FLOOR', 'SIMILAR'])         

        self.assertEqual(res, [])



