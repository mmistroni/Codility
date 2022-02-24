

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def solution(A):
    holder = []
    for i in range(0, len(A)-1):
        new_array = prefix_sums(A[i:])
        mapped = [item / idx for idx, item in enumerate(new_array) if idx > 1 ]
        holder.append((i, min(mapped)))
    sorted_holder = sorted(holder, key=lambda tpl:tpl[1])
    return sorted_holder[0]


def solution2(A):
    new_array = prefix_sums(A)
    # Sample problem here https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

    print('INPUT ARRAY :{}'.format(A))
    print('Prefixed sums is:{}'.format(new_array))

    holder = []

    for idx in range(2, len(new_array)):
        tpl_idx = idx - 1

        for idx_2, item in enumerate(new_array[idx:]):
            # To revise . we only look forward, not backwards, so we start from idx+1
            # something not quite right we should hnot have anything lower than 2..
            # we need to find the real index of the tpl

            tpl = ((tpl_idx, tpl_idx + idx_2+1), item, (item - new_array[idx - 2]) / (idx_2+2))



            print(f'item:{item} - {new_array[idx - 2]} / {idx_2+2}')

            print(f'TPL IS:{tpl}')

            print(f'Tuple start:{tpl_idx-1}, Tuple end:{tpl_idx + idx_2}')

            holder.append(tpl )

    return holder


