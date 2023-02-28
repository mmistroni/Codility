#https://www.hackerrank.com/challenges/funny-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def solution(s):
    r = s[::-1]

    first = [ord(c) for c in s]

    second = [ord(c) for c in r]

    diff_one = [abs(first[i] - first[i+1]) for i in range(0, len(first)-1)]

    diff_two = [abs(second[i] - second[i+1]) for i in range(0, len(second) - 1)]

    return "Funny" if diff_one == diff_two else "Not Funny"


