#https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/

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


def loop(start_idx, end_idx, candidate, steps, fib_dict):
    counter = 0
    while True:
        diff_to_end = end_idx - candidate
        if diff_to_end in fib_dict.keys():
            counter += 1
            end_idx = candidate;
            if steps:
                candidate = steps.pop()
            else:
                diff_to_end = end_idx - start_idx
                if diff_to_end in fib_dict.keys():
                    return counter
                return -1

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
    start = -1
    end = len(A)

    holder = []
    while ones:
        candidate = ones.pop(-1)
        param = ones.copy()
        res = loop(start, end, candidate, param, fib_dict)
        print(f'candidate:{candidate}, ones:{ones}. result:{res}')

        if res > 0:
            holder.append(res)
    print(f'Before returning we have:{holder}')
    return min(holder) if holder else -1