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
    seq = fibonacci_seq(len(A))[0:len(A)]
    d = dict((seq[i], i) for i in range(0, len(seq)))

    if not A:
        return 1
    if all([i for i in A if i == 0]):
        if len(A) in d.keys():
            return 1


    if len(A) in d:
        return 1
    ones = [idx for idx in range(0, len(A)) if A[idx] == 1]
    ones.append(len(A))
    start = -1
    counter = 0
    found = False
    while not found:
        if ones:
            tmp = ones.pop(0)
        else:
            found = True
        test = probe(start, tmp, d)

        if test:
            counter += 1
            if not ones:
                found = True
            else:
                start = tmp
    return counter
