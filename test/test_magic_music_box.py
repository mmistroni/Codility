from magic_music_box import magic_music_box, pattern
import re
import unittest

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
        self.assertEquals(expected, result)

    def test_two(self):
        words = ['DOWN', 'PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'SILENCE', 'DOWN', 'MARKDOWN'] # words

        expected = ['DOWN', 'REPTILE', 'AMIDST', 'SOFA', 'SOLAR', 'PLANE', 'SILENCE', 'MARKDOWN']  # expected
        res = magic_music_box(words)
        self.assertEquals(expected, res)

    def test_three(self):
        words = []
        expected = []
        self.assertEquals(expected, magic_music_box(words))


    def test_sample(self):
        words = ['DOWN', 'PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'SILENCE', 'DOWN', 'MARKDOWN']
        #['DOWN', 'REPTILE', 'AMIDST', 'SOFA'] # words

        good = [w for w in words if re.search(pattern, w)]

        print(good)

        notes_dict = {'DO' : 0, 'RE' : 1, 'MI' : 2,
                      'FA' : 3, 'SOL' : 4, 'LA' : 5, 'SI' : 6}


        holder = []
        seen = set()
        for idx, w in enumerate(words):
            match = re.search(pattern, w)
            if match:
                if w not in seen:
                    seen.add(w)
                    note = match.group(1)
                    holder.append((w, notes_dict.get(note), idx))

        sorted_l= sorted(holder, key=lambda x: (x[1]))
        from pprint import pprint
        pprint(sorted_l)

