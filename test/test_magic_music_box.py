from src.magic_music_box import magic_music_box, pattern, notes_dict
import re
import unittest
from collections import defaultdict, OrderedDict
import logging
from itertools import chain


class Player:
    def __init__(self, note, idx):
        self.note = note
        self.next = next
        self.seen_words = []
        self.idx = idx

    
    def handle(self, words):
        logging.info(f'{self.note} handling {words}')
        found = False
        for idx, word in enumerate(words):
            if self.note in word:
                if word not in self.seen_words:
                    self.seen_words.append(word)
                    # pass it on to the next player
                    #  
                    words.remove(word)
                    # we pass to the next 
                    found = True
                    break    
                else:
                    pass
                    
                    #words.remove(word) # problem here in usecase 2 we say found but it is not if it is a dupe
                    # this is the only usecase failing
        if not found:
            return
        if words:
            new_list = words[idx:] + words[0:idx]
            return self.next.handle(new_list)
        else:
            return
        # if we havent found a note we raise an exception
        
    def content(self):
        # if more than one we'll need to add increment
        if len(self.seen_words) == 1:
            return [(self.seen_words[0], self.idx)]
        else:
            holder = []
            counter = self.idx
            for w in self.seen_words:
                holder.append((w, counter))
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


        music_box[0].handle(words)

        res = list(chain(*[p.content() for p in music_box]))

        sorted_l = sorted(res, key=lambda x: (x[1]))

        result = [tpl[0] for tpl in sorted_l]
        return result

    def test_run_brain(self):
        samples = ['DOWN', 'REPTILE', 'AMIDST', 'SOFA']
        self.run_brain(samples)


    def test_one(self):
        words = ['DOWN', 'REPTILE', 'AMIDST', 'SOFA'] # words
        expected = ['DOWN', 'REPTILE', 'AMIDST', 'SOFA']  # expected
        result = self.run_brain(words)
        self.assertEqual(expected, result)
        r2 = magic_music_box(['DOWN', 'REPTILE', 'AMIDST', 'SOFA'])
        self.assertEqual(expected, r2)
        

    def test_two(self):
        words = ['DOWN', 'PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'SILENCE', 'DOWN', 'MARKDOWN'] # words

        expected = ['DOWN', 'REPTILE', 'AMIDST', 'SOFA', 'SOLAR', 'PLANE', 'SILENCE', 'MARKDOWN']  # expected
        res = magic_music_box(words)
        self.assertEqual(expected, res)

    def test_four(self):
        words = ['DOWN', 'AMIDST', 'SOFA', 'FACTION']
        res = magic_music_box(words)
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
    
    def test_usecaselast(self):
        words = ['INNOVATION', 'RESIST', 'RELATE', 'EROSION', 'HOUSE', 'MINIMAL', 'ENDOW', 'DOCTOR', 'EROSION', 'COLLABORATE', 'PREPARE', 'FAITHFUL', 'MODIFY', 'RESOLUTE', 'CREDIBLE', 'FACTOR', 'BASIC', 'FOUNTAIN', 'RIVER', 'BUFFALO', 'CHAIR', 'MONTAIN', 'MONTAIN', 'REACTOR', 'DOLLY', 'MOUNTAIN', 'LANDSCAPE', 'ABSOLUTE', 'SINGULAR', 'MINIMAL', 'FACTOR', 'CONSISTENT', 'CREDIBLE', 'MOUNTAIN', 'GLACIAL', 'WINDOW', 'EROSION', 'GATE', 'DODGE', 'NIGHT', 'LIBRARY', 'INNOVATION', 'DREAMER', 'DESOLATE', 'INNOVATION', 'LANDSCAPE', 'SOLAR', 'FACTORIAL', 'HELICOPTER', 'GLACIAL', 'SADOMASOCHISM', 'LANDSCAPE', 'VISIBLE', 'COMMIT', 'HELICOPTER', 'EROSION', 'SOLAR', 'BEDROOM', 'BASIC', 'ADORABLE', 'COLLABORATE', 'DODGE', 'REMINDER', 'CORRECT', 'RESOLUTE', 'COMIC', 'CREDIBLE', 'SOLID', 'SUNSHINE', 'FISH', 'RESIST', 'SINGULAR', 'FAITHFUL', 'MONTAIN', 'SIMPLIFY', 'PREDOMINATE', 'DOCTOR', 'DOCTOR', 'LIBRARY', 'LATERAL', 'DREAMER', 'ABSOLUTE', 'DODGE', 'MINIMAL', 'FACTOR', 'CHAIR', 'COLLABORATE', 'CHAIR', 'COMIC', 'SILENT', 'CLOUD', 'ADORABLE', 'VISIBLE', 'ROW', 'BOOK', 'LANDSCAPE', 'NIGHT', 'RELATION', 'FANTASTIC', 'DREAMER'] 
        expected =  ['ADORABLE', 'RELATE', 'COMIC', 'BUFFALO', 'SOLAR', 'GLACIAL', 'SITUATION', 'DODGE', 'RESIST', 'MIMICRY', 'FANTASTIC', 'SOLUBLE', 'LANDSCAPE', 'VISIBLE', 'WINDOW', 'CORRECT', 'COMMIT', 'FANATIC', 'CONSOLIDATE', 'CLARITY', 'SILENT', 'DOBLE', 'CREDIBLE', 'MIRACLE', 'FAIRYTALE', 'ABSOLUTE', 'SINGULAR', 'CONSISTENT', 'PREDOMINATE', 'REINFORCE', 'MINIMAL', 'FACTOR']

        wrongs = ['CORRECT', 'PLATFORM', 'CONSISTENT', 'COMIC', 'HELICOPTER', 'DODGE', 'WINDOW', 'KITCHEN', 'ELABORATE', 'SADOMASOCHISM', 'SOLAR', 'CREDIBLE', 'BOOK', 'REINFORCE', 'HOUSE', 'SITUATION', 'CHAIR', 'SUNSHINE', 'FANATIC', 'BEDROOM', 'PERMITS', 'ADORABLE', 'FANTASTIC', 'PREDOMINATE', 'TREATMENT', 'GARDEN', 'MISTAKE', 'MIMICRY', 'EXAMPLE', 'GATE', 'PLATFORM', 'REINFORCE', 'REMINDER', 'ENVIRONMENT', 'MONTAIN', 'PREDOMINATE', 'PREDOMINATE', 'LIBRARY', 'FANTASTIC', 'EMIGRANT', 'GATE', 'PERMITS', 'FACILITATE', 'DOBLE', 'FAITHFUL', 'SISTER', 'MOUNTAIN', 'CHAIR', 'ADORABLE', 'ENVIRONMENT', 'PREDOMINATE', 'FISH', 'MIRACLE', 'RIVER', 'RESOLUTE', 'SISTER', 'REACTOR', 'BEDROOM', 'SOLSTICE', 'PREDOMINATE', 'EROSION', 'COLLABORATE', 'MISTAKE', 'FACTORIAL', 'DORMITORY', 'FACTOR', 'SITUATION', 'FACTOR', 'RESIST', 'DREAMER', 'HELICOPTER', 'SOLSTICE', 'ABSOLUTE', 'FREEDOM', 'RELATION', 'PARK', 'RELATION', 'SINGULAR', 'SOLUTION', 'DOLLY', 'SOLUBLE', 'ENVIRONMENT', 'CREDIBLE', 'EROSION', 'COLLABORATE', 'ELABORATE', 'ROW', 'ENVIRONMENT', 'TREATMENT', 'PLATFORM']

        res = magic_music_box(words)
        self.assertEqual(expected, res)

