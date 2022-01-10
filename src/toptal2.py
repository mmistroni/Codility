

def partition_seats(numpassengers, S, numcars):
    first_car= S.pop(0)
    numpassengers -= first_car  # filling firstcar
    numcars +=1
    if numpassengers <= 0:
        return numcars
    return partition_seats(numpassengers, S, numcars)


def arrange(P, S):
    sorted_seats = sorted(S, key=lambda x:x, reverse=True)
    numpassengers = sum(P)

    return partition_seats(numpassengers, sorted_seats, 0)





