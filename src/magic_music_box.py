#https://www.codewars.com/kata/6710e54f8ef071fe99eebd07/train/python
import re
NOTES = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]

pattern = r"\b\w*(DO|RE|MI|FA|SOL|LA|SI)\w*\b"

notes_dict = {'DO' : 0, 'RE' : 1, 'MI' : 2,
                      'FA' : 3, 'SOL' : 4, 'LA' : 5, 'SI' : 6}


def magic_music_box(words):

    if not words:
        return []

    holder = []
    seen = set()
    for idx, w in enumerate(words):
        print(w)  # Not really there, The sorting mechanism is not quite right
        match = re.search(pattern, w)
        if match:
            if w not in seen:
                seen.add(w)
                note = match.group(1)
                holder.append((w, notes_dict.get(note), idx))

    sorted_l = sorted(holder, key=lambda x: (x[1], x[2]))

    return [t[0] for t in sorted_l]