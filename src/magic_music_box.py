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
    while True:
        # we exit either when array is empty or when we found all the notes
        # if a note is missing we should break and return what we have
        if not words:
            break
        for note in patterns:
            note_found = False
            for idx, word in enumerate(words):
                if note in word:
                    if word not in found:
                        found.append(word)
                    else:
                        dupes.append(word)
                    note_found = True
                    words.pop(idx)   
            if not note_found:#
                return found  
            else:
                continue     
        
    return found


def magic_music_box(words):

    if not words:
        return []
    return play(words)
    