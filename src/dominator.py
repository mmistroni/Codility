from collections import Counter

def _sol1(A):
    c = Counter(A)
    tp = sorted(c.items(), key=lambda tpl: tpl[1], reverse=True)

    tst = dict.fromkeys(A)

    top = tp[0]
    if len(top[1]) > len(A) / 2:
        return top[0]
    return -1

def _sol2(A):

    from collections import defaultdict
    holder = defaultdict(list)
    for idx, item  in enumerate(A):
        holder[item].append(idx)
    tp = sorted(holder.items(), key=lambda tpl: len(tpl[1]), reverse=True)
    top = tp[0]
    if len(top[1]) > len(A) / 2:
        return top[1][1]
    return -1


def solution( A):
    return _sol2(A)

