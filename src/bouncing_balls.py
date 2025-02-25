#https://www.codewars.com/kata/5544c7a5cb454edb3c000047


def bouncing_ball(h, bounce, window):
    # your code
    # we need to compare bounce vs height of window
    # Ok so ball bounces at 0.66 of the obtained height


    if h > 0 and 0 < bounce < 1 and window < h:
        n = 1 # first drop
        bounce_factor  = bounce
        while True:
            h = h * bounce_factor 
            if h > window:
                n +=2 # if its higher then she see it twice
            else:
                break
            
        return n
    
    return -1