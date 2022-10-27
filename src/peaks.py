# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/
import math
def divisors(n):
  lis =[1]
  s = math.ceil(math.sqrt(n))
  for g in range(s,1, -1):
     if n % g == 0:
        lis.append(g)
        lis.append(int(n / g))
  return (set(lis))

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


def peaks_in_slices(peaks, divs, A):
    maxdivs = 0
    for subListLength in divs:
        if subListLength == 1:
            slists = [A]
        else:
            slists = [A[i:i + subListLength] for i in range(0, len(A), subListLength)]
        for sublist in slists:
            checks = set(peaks)-set(sublist)
            if len(checks) < len(peaks):
                maxdivs = max(maxdivs, subListLength)

    return maxdivs






def solution(A):
    from itertools import islice
    peaks = [A[idx] for idx in find_peaks(A)]
    n_divisors = divisors(len(A))

    if n_divisors:
        return peaks_in_slices(peaks, n_divisors, A)
    return 0
