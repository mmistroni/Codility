#

def divisors(n):
    i = 1
    result = []
    while (i * i < n):
        if (n % i == 0):
            result.append(i)
        i += 1
    if (i * i == n):
        result.append(i)
    return result

def find_peaks(N):
    peaks = []
    for idx in range(0, len(N)):
        if idx == 0:
            #
            if N[idx] > N[idx+1]:
                peaks.append(idx)

        if idx == len(N)-1:
            if N[idx] > N[idx-1]:
                peaks.append(idx)
        else:
            if N[idx-1] < N[idx] > N[idx + 1]:
                peaks.append(idx)


    return peaks


def solution(A):
    from itertools import islice
    peaks = find_peaks(A)
    n_divisors = divisors(len(A))[::-1]





    return None