# https://www.codewars.com/kata/595ef0c7458ad5facc000019


def calculate_bonus(inarray):
    bon_array = []
    for idx in range(0, len(inarray)):
        if idx == 0:
            # first one, default 1
            bon_array.append(1)
        else:
            if inarray[idx] > inarray[idx - 1]:
                latest = bon_array[-1]
                bon_array.append(latest + 1)
            else:
                bon_array.append(1)

    return bon_array


def minimum_bonus(scores):
    allb = calculate_bonus(scores)
    return sum(allb)


