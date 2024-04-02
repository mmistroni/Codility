#https://www.codewars.com/kata/59321f29a010d5aa80000066/train/python



def shortest_arrang(num_of_students):

    # gauss formula

    holders = []

    '''
    Sum = n * (a + (n - 1)) / 2
    where:

    n - the number of consecutive integers to be added
    a - the first number in the sequence
    
    '''

    a = 1
    n = 1

    # need to find the clause

    holders = []

    while True:
        # Not quite right. this is a brute force
        # We need to rethink this...
        

        sm = n * (a + (n - 1)) / 2
        if int(sm) < num_of_students:
            n +=1
        if int(sm) > num_of_students:
            a +=1
            n = 1
        if int(sm) == num_of_students:
            holders.append([a, n])
            break

    if holders:
        a, n = holders[-1]
        return list(range(a, n+1))
    return [-1]