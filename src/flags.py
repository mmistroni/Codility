#https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/


def solution(N):
    current_min = (N[0], 0)
    current_max = (N[0], 0)
    holder = []
    for idx, item in enumerate(N[1:]):
        if not current_min:
            current_min = (item, idx)
            continue
        if not current_max:
            current_max  = (item, idx)
        if item < current_max[0]:
            holder.append(current_max)
            current_min = None
            current_max = None
        elif item > current_max[0]:
            current_max =(item, idx)
        elif item < current_min[0]:
            current_min = (item, idx)

    return len(holder)


