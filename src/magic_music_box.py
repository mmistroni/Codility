#https://www.codewars.com/kata/6710e54f8ef071fe99eebd07/train/python
import re
from collections import defaultdict
NOTES = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]

pattern = r"\b\w*(DO|RE|MI|FA|SOL|LA|SI)\w*\b"

notes_dict = {'DO' : 0, 'RE' : 1, 'MI' : 2,
                      'FA' : 3, 'SOL' : 4, 'LA' : 5, 'SI' : 6}


def magic_music_box(words):

    if not words:
        return []

    holder = []
    seen = set()

    ddict = defaultdict(list)

    for idx, w in enumerate(words):
        patterns = "DO|RE|MI|FA|SOL|LA|SI".split("|")
        for p in patterns:
            match = re.search(p, w)
            if match:
                note = match.group(0)
                break
            else:
                continue
        if note:        
            ddict[note].append(1)
            if w not in seen:
                seen.add(w)
                nidx = notes_dict.get(note)
                if len(ddict[note]) > 1:
                    nidx += 7
                holder.append((w, nidx, nidx))

    sorted_l = sorted(holder, key=lambda x: (x[1]))

    return [t[0] for t in sorted_l]
        