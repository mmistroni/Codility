#https://www.codewars.com/kata/6710e54f8ef071fe99eebd07/train/python

NOTES = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]

# the box
def recurse(words, notes, note_idx, holder):
    if not words:  # We need a better altenrative. this will not work
        return holder
    elif not notes: # not sure  if this will work
        return holder
    else:
        note_idx = note_idx % 7
        current = words[0]
        note = notes[note_idx]
        if current.find(note) >=0:
            holder.append(current)
            words.remove(current)
            notes.remove(note)
        return recurse(words, notes, note_idx + 1, holder)


def magic_music_box(words):

    # so we need to loop thu all the notes, and check
    # if current word contains the note. If it does, remove workd
    # and add it to the box
    return recurse(words, NOTES, 0, [])