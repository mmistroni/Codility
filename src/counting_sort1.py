#https://www.hackerrank.com/challenges/countingsort1/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def solution(input_array):
    arr = [0] * len(input_array)
    for item in input_array:
        arr[item] += 1

    return arr[0:100]