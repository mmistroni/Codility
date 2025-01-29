#https://www.codewars.com/kata/6710e54f8ef071fe99eebd07/train/python
import re

from collections import defaultdict
NOTES = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]

pattern = r"\b\w*(DO|RE|MI|FA|SOL|LA|SI)\w*\b"

notes_dict = {'DO' : 0, 'RE' : 1, 'MI' : 2,
                      'FA' : 3, 'SOL' : 4, 'LA' : 5, 'SI' : 6}


def play(words):
    patterns = "DO|RE|MI|FA|SOL|LA|SI".split("|")
        
    found = []
    dupes = []

    looping = 0
    ddict = defaultdict(list)

    
    while True:
        # we exit either when array is empty or when we found all the notes
        # if a note is missing we should break and return what we have
        if not words:
            break
        lookup_idx = 0
        seen = []
        # for loop. 
        for note in patterns:
            note_found = False
            for idx, word in enumerate(words[lookup_idx:]):
                if note in word:
                    ddict[note].append(1)
                    if word not in seen:
                        nidx = notes_dict.get(note)
                        if len(ddict[note]) > 1:
                            nidx += 7
                        found.append((word,nidx))
                        seen.append(word)
                    else:
                        dupes.append(word)
                    note_found = True
                    words.remove(word)
                    break
                       
            if not note_found:#
                # start from beginning
                idx = 0
            else:
                lookup_idx = idx if idx <= len(words)-1 else 0
                continue     
    return found

def magic_music_box(words):

    if not words:
        return []
    found =  play(words)
    sorted_l = sorted(found, key=lambda x: (x[1]))

    res = [t[0] for t in sorted_l]    
    return res

    