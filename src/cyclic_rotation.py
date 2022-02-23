


def sol(A, K):

    with_idx = [(item, idx) for idx, item in enumerate(A)]

    mapped = [(tpl[0], (tpl[1] + K) % len(A) ) for tpl in with_idx]

    sorted_arr = sorted(mapped, key=lambda tpl: tpl[1])
    return [tpl[0] for tpl in sorted_arr]


