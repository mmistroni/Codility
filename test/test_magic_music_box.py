from magic_music_box import magic_music_box, pattern, notes_dict
import re
import unittest
from collections import defaultdict

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
        from collections import defaultdict
        words = ['DOWN', 'PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'SILENCE', 'DOWN', 'MARKDOWN']  # words
        expected = ['DOWN', 'REPTILE', 'AMIDST', 'SOFA', 'SOLAR', 'PLANE', 'SILENCE', 'MARKDOWN']  # expected

        holder = []
        seen = set()

        ddict = defaultdict(list)

        for idx, w in enumerate(words):
            patterns = "DO|RE|MI|FA|SOL|LA|SI".split("|")
            for p in patterns:
                match = re.search(pattern, "SOLAR")
                if match:
                    note = match.group(1)
                    break

            ddict[note].append(1)
            if w not in seen:
                seen.add(w)
                nidx = notes_dict.get(note)
                if len(ddict[note]) > 1:
                    nidx += 7
                holder.append((w, nidx, nidx))

        sorted_l = sorted(holder, key=lambda x: (x[1]))

        res = [t[0] for t in sorted_l]
        self.assertEquals(expected, res)


    def test_sample(self):
        words = ['DOWN', 'PLANE', 'AMIDST', 'REPTILE', 'SOFA', 'SOLAR', 'SILENCE', 'DOWN', 'MARKDOWN']
        #['DOWN', 'REPTILE', 'AMIDST', 'SOFA'] # words

        pattern = r"\b\w*(DO|RE|MI|FA|SOL|SI)\w*\b"

        patterns = "DO|RE|MI|FA|SOL|LA|SI".split("|")
        for p in patterns:
            match = re.search(pattern, "SOLAR")
            if match:
                res = match.group(1)
                print(res)
                break







