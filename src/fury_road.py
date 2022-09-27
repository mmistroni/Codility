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


def compute_time(idx_array, surfaces):
    zipped = list(zip(idx_array, surfaces))
    print(f'Computing:{zipped}')


    return sum([TRANSPORT_DICT[surface][idx] for idx,surface in zipped])


def solution(A):
    # Constraint here. Once you switch mean of transport,
    # you cannot go back to the previous
    #
    time = 0

    first_surface = A[0]
    min_time = TRANSPORT_DICT[first_surface][0]

    idx = TRANSPORT_DICT[first_surface].index(min_time)

    indexes = [idx] * len(A)

    minnow  = compute_time(indexes, A)

    for i in range(1,len(A)):
        alt_idx = 1 if idx == 0 else 0
        new_arr = indexes[0:i] + [alt_idx]* (len(A)-i)

        mxtime = compute_time(new_arr, A)

        if mxtime < minnow:
            minnow = mxtime

        print(f'{i}|{new_arr}|{mxtime}|{minnow}')

    return minnow



