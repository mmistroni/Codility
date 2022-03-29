'''

https://app.codility.com/c/run/training7XEK8F-27D/
'''

def check(container, size_and_dir_tpl):
    pass
def solution(A, B):
    # write your code in Python 3.6
    # https://app.codility.com/c/run/trainingUPYQM8-5MH/
    # Need two stacks, one for upstream and another for downstream
    # this is about stacks and queues
    # We can try to use a stack
    # we need to bear in mind direction

    # this might give a reference


    holder = []

    for idx, tpl in enumerate(zip(A, B)):
        size, dir = tpl
        if not holder:
            holder.append((idx, size, dir))
        else:
            current_idx, current_size, current_dir = holder[-1]
            if current_idx < idx and current_dir == 1 and dir == 0:
                if current_size > size:
                    print(f'Eating {idx},{size}, {dir}')

                else:
                    print(f'crossing each other:{current_idx},{current_size}, {current_dir} vs {idx},{size}, {dir}')

                    holder.pop(-1)
                    holder.append((current_idx, current_size, current_dir))
            else:
                holder.append((idx, size, dir))
    return len(holder)
