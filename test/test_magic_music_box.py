from src.magic_music_box import magic_music_box, pattern, notes_dict
import re
import unittest
from collections import defaultdict, OrderedDict
import logging

class Player:
    def __init__(self, note, idx):
        self.note = note
        self.next = next
        self.words = []
        self.idx = idx

    
    def handle(self, words):
        # Need to esabilish how to end the loop
        first = words[0]
        if self.note in words:
            if first not in self.words:
                # duplicate
                logging.info(f'{self.note} player handling:{first}')
                self.words.append(first)
            words.remove(first)
        self.next.handle(words)

    def content(self):
        # if more than one we'll need to add increment
        if len(self.words) == 1:
            return [(self.words[0], self.idx)]
        else:
            holder = []
            counter = self.idx
            for w in self.words:
                holder.append(w, counter)
                counter += 7
            return holder
    def __str__(self):
        return f'Idx={self.idx}, Nxt:{self.next.idx}'

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

    def run_brain(self, words):
        '''
        lets try this,  we define a chain where we have an holder per note, which link
        to the next holder and the last holder goes back to the first. then when there are no words
        we return and ask each holder to return what they got.
        '''
        NOTES = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]

        music_box = []
        # Init
        for idx, note in enumerate(NOTES):
            p = Player(note, idx)
            music_box.append(p)

        # populating next
        for idx, item in enumerate(music_box):
            nxt_idx = idx + 1 if idx < len(music_box) -1 else 0
            item.next = music_box[nxt_idx]

        for item in music_box:
            print(item)

        return music_box


    def test_run_brain(self):
        self.run_brain([])


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
        self.assertEqual( ['DOWN', 'CORRECT', 'COMIC', 'FAMILY'], res)

    def test_otherusecases4(self):
        res = magic_music_box(['RECORD', 'COMIC', 'DOWN', 'CAR', 'FAMILY', 'MOUSE', 'DISSOLVED', 'DINNER', 'CORRECT'])
        self.assertEqual(['DOWN', 'CORRECT', 'COMIC', 'FAMILY', 'DISSOLVED'], res)

    def test_otherusecases5(self):
        res = magic_music_box(['RECORD', 'COMIC', 'LAPTOP', 'SYLLABLE', 'DOWN', 'CAR', 'FAMILY', 'MOUSE', 'DISSOLVED', 'DINNER', 'CORRECT'])
        self.assertEqual( ['DOWN', 'CORRECT', 'COMIC', 'FAMILY', 'DISSOLVED', 'LAPTOP'], res)

