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

    def test_four(self):
        res = magic_music_box(['DOWN', 'AMIDST', 'SOFA', 'FACTION'])
        self.assertEqual(res, ['DOWN'])


    def test_five(self):
    
        res = magic_music_box(['PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'FLOOR', 'SIMILAR'])         

        self.assertEqual(res, [])

    def test_duplicates(self):
        res = magic_music_box(['DOOR', 'DOOR', 'REPTILE', 'REPTILE', 'SIMILAR', 'SIMILAR', 'SOFA', 'SOFA', 'DISSOLVED', 'DISSOLVED', 'LAPTOP', 'LAPTOP', 'RESIST', 'RESIST'])
        expected =  ['DOOR', 'REPTILE', 'SIMILAR', 'SOFA', 'DISSOLVED', 'LAPTOP', 'RESIST']
        self.assertEqual(expected, res)

    def test_otherusecase(self):
        res = magic_music_box(['RECORD', 'LAPTOP', 'DOWN', 'CAR', 'MOUSE', 'DINNER', 'CORRECT'])
        self.assertEqual(['DOWN', 'CORRECT'], res)

    def test_otherusecases2(self):
        res = magic_music_box(['RECORD', 'COMIC', 'LAPTOP', 'DOWN', 'CAR', 'MOUSE', 'DINNER', 'CORRECT'])
        self.assertEqual( ['DOWN', 'CORRECT', 'COMIC'], res)

    def test_otherusecases3(self):
        res = magic_music_box(['RECORD', 'COMIC', 'LAPTOP', 'DOWN', 'CAR', 'FAMILY', 'MOUSE', 'DINNER', 'CORRECT'])
        self.assetEqual( ['DOWN', 'CORRECT', 'COMIC', 'FAMILY'], res)

    def test_otherusecases4(self):
        res = magic_music_box(['RECORD', 'COMIC', 'DOWN', 'CAR', 'FAMILY', 'MOUSE', 'DISSOLVED', 'DINNER', 'CORRECT'])
        self.assertEqual(['DOWN', 'CORRECT', 'COMIC', 'FAMILY', 'DISSOLVED'], res)

    def test_otherusecases5(self):
        res = magic_music_box(['RECORD', 'COMIC', 'LAPTOP', 'SYLLABLE', 'DOWN', 'CAR', 'FAMILY', 'MOUSE', 'DISSOLVED', 'DINNER', 'CORRECT'])
        self.assertEqual( ['DOWN', 'CORRECT', 'COMIC', 'FAMILY', 'DISSOLVED', 'LAPTOP'], res)

