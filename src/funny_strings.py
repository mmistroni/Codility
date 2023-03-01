#https://www.hackerrank.com/challenges/funny-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def solution(s):
    # Write your code here
    arr = [abs(ord(s[i - 1]) - ord(s[i])) for i in range(1, len(s))]
    return 'Funny' if arr == arr[::-1] else 'Not Funny'