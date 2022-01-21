def sol(A):
    range = len(A) + 1
    expected = (range * (range+1)) / 2
    sumInA = sum(A)
    return expected - sumInA


