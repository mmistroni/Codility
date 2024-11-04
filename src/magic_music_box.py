#https://www.codewars.com/kata/6710e54f8ef071fe99eebd07/train/python
import re
NOTES = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]

pattern = r"\b\w*(DO|RE|MI|FA|SOL|LA|SI)\w*\b"

def check_notes(words):
    bad = [w for w in words if  not re.findall(pattern, w)]
    if bad == words:
        return False
    return True

# the box
def recurse(words, notes, note_idx, word_idx, holder):
    if not words:
        #word sempty
        return holder
    elif  not check_notes(notes):
        # Only words that do not match
        return holder
    else:
        # Rset, we dont need to  remove words, we just check
        # if they are aalrady in the holder
        # We just need to find out when to stop cycle for
        # words that do not fit
        note_idx = note_idx % 7
        note = notes[note_idx]
        current = words[word_idx]
        print(f'Looking for {note} in {current}')
        if current.find(note) >= 0:
            holder.append(current)
            words.remove(current)
        else:
            word_idx +=1
    return recurse(words, notes, note_idx + 1, word_idx, holder)


def magic_music_box(words):

    # so we need to loop thu all the notes, and check
    # if current word contains the note. If it does, remove workd
    # and add it to the box
    holder = []
    res =  recurse(words, NOTES, 0, 0, holder)
    return res