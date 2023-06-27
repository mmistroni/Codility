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
    counter = 0
    start = -1
    end = len(A)

    found = False
    while not found:
        diff_to_end = end - start
        if diff_to_end in fib_dict.keys():
            counter += 1
        if not ones:
            break

        next = ones.pop(0)
        res = probe(start, next, fib_dict)
        if not res:
            continue
        else:
            counter +=1
            start = next
    if counter == 0:
        return -1
    return counter
