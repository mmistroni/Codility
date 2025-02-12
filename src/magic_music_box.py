#https://www.codewars.com/kata/6710e54f8ef071fe99eebd07/train/python
import re

from collections import defaultdict
NOTES = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]

pattern = r"\b\w*(DO|RE|MI|FA|SOL|LA|SI)\w*\b"

notes_dict = {'DO' : 0, 'RE' : 1, 'MI' : 2,
                      'FA' : 3, 'SOL' : 4, 'LA' : 5, 'SI' : 6}
from itertools import chain


class Player:
    def __init__(self, note, idx):
        self.note = note
        self.next = next
        self.seen_words = []
        self.idx = idx

    
    def handle(self, words):
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

def magic_music_box(words):

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

    music_box[0].handle(words)

    res = list(chain(*[p.content() for p in music_box]))

    sorted_l = sorted(res, key=lambda x: (x[1]))

    result = [tpl[0] for tpl in sorted_l]
    return result

    

        
    