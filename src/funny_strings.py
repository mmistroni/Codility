def solution(s):
    r = s[::-1]

    first = [ord(c) for c in s]

    second = [ord(c) for c in r]

    diff_one = [first[i+1] - first[i] for i in range(0, len(l)-1)]

    diff_two = [second[i + 1] - second[i] for i in range(0, len(l) - 1)]

    return "Funny" if diff_one == diff_two else "Not funny"


