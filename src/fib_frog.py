#https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/
'''
A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0



'''
def fibonacci_seq(n):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

def probe(prev, next, d):
    diff = next - prev
    if diff in d.keys():
        return True
    return False


def loop(candidate, steps, fib_dict):
    counter = 0
    next_idx = 0
    # We'll need to find out the break clause
    final = None
    while final != steps[-1]:
        final = steps[next_idx]
        diff_to_end = final - candidate
        if diff_to_end in fib_dict.keys():
            candidate = final
            if final == steps[-1]:
                return counter
        next_idx += 1

    return counter

def solution(A):
    seq = fibonacci_seq(max(len(A), 10))[1:]
    fib_dict = dict((seq[i], i) for i in range(0, len(seq)))

    ones = [idx for idx in range(0, len(A)) if A[idx] == 1]



    # hedges
    if not A:
        return 1
    else :
        if len(ones)  == 0:
            fibcheck = len(A) - (-1)
            if fibcheck in fib_dict.keys():
                return 1
            return -1
    # other hedge
    start_idx = -1
    counter = 0
    ones.append(len(A))
    holder = []
    end_idx = -1

    if abs(start_idx - ones[end_idx]) in fib_dict.keys():
        return 1

    for idx, i in enumerate(ones):
        diff = i - start_idx
        if diff in fib_dict.keys():
            res = loop(i,  ones[idx+1:], fib_dict)
            holder.append(res + 1)

    valids = [v for v in holder if v > 0]

    if not valids:
        return -1
    return min(valids)