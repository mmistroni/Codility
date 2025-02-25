#https://www.codewars.com/kata/5544c7a5cb454edb3c000047


def bouncing_ball(h, bounce, window):
    # your code
    # we need to compare bounce vs height of window
    if h > 0 and 0 < bounce < 1 and window < h:
        start = 1
        bounce_height = h * bounce
        if window > bounce_height:
            return start
        else:
            return start + 2
    return -1