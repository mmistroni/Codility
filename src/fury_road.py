'''
You have to be at your work as soon as possible.
The road on your route to work may consist of two types of surface: asphalt or sand.
 To simplify the description, it will be denoted by a string R consisting
 only of the letters: "A" for an asphalt segment and "S" for a sand segment.
All segments represent the same distance. For example, R = "SAAS" describes
a road comprising of sand, asphalt, asphalt and sand segments.
When you go on foot, you need 20 minutes to pass through an asphalt
segment and 30 minutes through a sand segment.
You also have an electric scooter, which needs 5 minutes to pass through
an asphalt segment and 40 minutes through a sand segment.
You start your journey on the scooter,
but at any point you can get off the
scooter and go on foot for the rest of the journey.
What is the shortest time in which you can get to work?

https://app.codility.com/c/run/trainingXEV9SP-2CS/
'''

TRANSPORT_DICT = {'A' : [5, 20],
                  'S' : [40, 30]}
FOOT= {'A' : 20,
       'S' : 30}

SCOOTER = {'A' : 5,
           'S' : 40}


def solution(A):
    # Constraint here. Once you switch mean of transport,
    # you cannot go back to the previous
    # Idea1. Start with the Fastest, and go till the end
    # Then loop from the end and replace one by one until
    # you beat the original
    time = 0

    first_surface = A[0]


    min_time = min(TRANSPORT_DICT[first_surface])

    idx = TRANSPORT_DICT[first_surface].index(min_time)

    indexes = [idx] * len(A)

    # base idxs
    transport_array = [TRANSPORT_DICT[surface][idx] for surface in A]


    max_time = sum(transport_array)

    better_one = transport_array[::-1]

    end = len(A)-1
    for idx in range(end,-1, -1):
        sf = A[idx]

        lst = TRANSPORT_DICT[sf]
        tmp_repl_idx = 0 if idx == 1 else 1
        tmp_repl = lst[tmp_repl_idx]
        if tmp_repl < transport_array[idx]:
            better_one[idx] = tmp_repl
            t_time = sum(better_one)
            if t_time < max_time:
                max_time = t_time
            return max_time




