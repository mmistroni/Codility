#https://www.hackerrank.com/challenges/picking-numbers/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


def solution(arr):
    sorted_arr = sorted(arr, key=lambda k:k)
    counter_holder = []
    counter = 0
    current_min = None
    for idx, item in enumerate(sorted_arr):
        if idx == 0:
            current_min=item
            counter +=1
            continue
        if item - current_min <=1:
            counter +=1
        else:
            counter_holder.append(counter)
            counter = 1
            current_min=item
    counter_holder.append(counter)
    return max(counter_holder)








