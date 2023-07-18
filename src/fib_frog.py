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

def find_next(start, nextes, fib_dict):
    holder = []
    for i in nextes:
        diff = i - start
        if diff in fib_dict.keys():
            holder.append(i)

    return holder

def probe(A):
    seq = fibonacci_seq(max(len(A), 10))[1:]
    fib_dict = dict((seq[i], i) for i in range(0, len(seq)))

    ones = [idx for idx in range(0, len(A)) if A[idx] == 1]
    ones = [-1] + ones + [len(A)]

    counter = 0
    current = ones[0]
    for i in ones[1:]:
        # Next Hint: We do one loop from beginning to end
        # find the max
        # then start from max to end
        c_idx = ones.index(current)
        nextes = find_next(current, ones[c_idx + 1:], fib_dict)
        if nextes:
            counter += 1
            current = nextes[-1]

    return counter if counter > 0 else -1



def solution(A):
    return probe(A)