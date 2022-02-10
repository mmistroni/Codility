

from prefix_sums import prefix_sums

def solution(A):
    new_array = prefix_sums(A)


    # Sample problem here https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

    print('INPUT ARRAY :{}'.format(A))
    print('Prefixed sums is:{}'.format(new_array))

    holder = []

    for idx in range(2, len(new_array)):
        tpl_idx = idx - 1
        diff = idx - 2

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

