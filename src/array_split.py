def sol(A):
    tpls = ((A[0:idx], A[idx:]) for idx in range(1, len(A)))
    mapped = map(lambda tpl: abs(sum(tpl[0]) - sum(tpl[1])), tpls)
    sorted_items = sorted(mapped, key= lambda x:x)
    return sorted_items.pop(0)