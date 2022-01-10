

def crop(message, K):
    words = message.split()
    limit = 0
    holder = []
    for idx, w in enumerate(words):
        limit += len(w)
        if limit <= K:
            holder.append(w)
            if idx < len(words) - 1:
                limit += 1
        else:
            break
    return ' '.join(holder)


