# https://www.hackerrank.com/challenges/minimum-loss/problem?isFullScreen=true
def solution(price):
    with_idx = [(price[idx], idx) for idx in range(0, len(price))]

    sorted_idx = sorted(with_idx, key = lambda tpl: tpl[0], reverse=True)

    start, idx = sorted_idx[0]

    min_loss = None
    for nxt, nxt_idx in sorted_idx[1:]:
        if nxt_idx < idx:
            pass
        if min_loss == None:
            min_loss = start - nxt
        else:
            if idx < nxt_idx:
                min_loss = min(start - nxt, min_loss)
        start = nxt
        idx = nxt_idx
    return min_loss



