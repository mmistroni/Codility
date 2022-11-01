import  math
def grade(input):
    if input < 38:
        return input
    else:
        result = input / 5
        nxt_mult = math.ceil(result)
        test =  5 * nxt_mult
        if (test - input) < 3:
            return test
        return input
